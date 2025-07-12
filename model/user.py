from abc import ABC, abstractmethod
from datetime import datetime
from db.database import get_connection

class User(ABC):
    def __init__(self, username, role):
        self.username = username
        self.role = role

    @abstractmethod
    def display(self):
        pass


class Customer(User):
    def display(self):
        print(f"\n✅ Logged in as Customer: {self.username}")

    def book_cab(self, pick_up, drop):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT CAB_ID FROM CABS WHERE IS_AVAILABLE = 1 LIMIT 1")
        cab = cursor.fetchone()
        if not cab:
            print("❌ No cabs available.")
            return
        cab_id = cab[0]

        cursor.execute("SELECT USER_ID FROM USERS WHERE USER_NAME = ?", (self.username,))
        user = cursor.fetchone()
        if not user:
            print("❌ User not found.")
            return
        user_id = user[0]

        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            INSERT INTO BOOKINGS (USER_ID, CAB_ID, PICKUP, DROP_LOCATION, TIMESTAMP)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, cab_id, pick_up, drop, time_now))

        cursor.execute("UPDATE CABS SET IS_AVAILABLE = 0 WHERE CAB_ID = ?", (cab_id,))
        conn.commit()
        print("✅ Cab booked successfully.")

    def view_history(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT USER_ID FROM USERS WHERE USER_NAME = ?", (self.username,))
        user = cursor.fetchone()
        if not user:
            print("❌ User not found.")
            return
        user_id = user[0]

        cursor.execute("SELECT PICKUP, DROP_LOCATION, TIMESTAMP FROM BOOKINGS WHERE USER_ID = ?", (user_id,))
        bookings = cursor.fetchall()

        if not bookings:
            print("❌ No bookings found.")
            return

        print("\n📖 Your Bookings:")
        for b in bookings:
            print(f"🗺️ {b[0]} ➡️ {b[1]} 🕒 {b[2]}")


class Admin(User):
    def display(self):
        print(f"\n✅ Logged in as Admin: {self.username}")

    def view_all_bookings(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT U.USER_NAME, B.PICKUP, B.DROP_LOCATION, B.TIMESTAMP
            FROM BOOKINGS B
            JOIN USERS U ON B.USER_ID = U.USER_ID
        """)
        bookings = cursor.fetchall()

        if not bookings:
            print("❌ No bookings yet.")
            return

        print("\n📋 All Bookings:")
        for b in bookings:
            print(f"👤 {b[0]} booked 🚖 from {b[1]} ➡️ {b[2]} at 🕒 {b[3]}")
