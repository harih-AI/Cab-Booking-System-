from db.database import get_connection
from model.user import Customer, Admin

class BookingSystem:

    def register(self, username, password, role='customer'):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Users (user_name, password, role) VALUES (?, ?, ?)",
                (username, password, role)
            )
            conn.commit()
            print("✅ Registration successful.")
            return True
        except Exception as e:
            print("❌ Error during registration:", e)
            return False
        finally:
            conn.close()

    def login(self, username, password):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT role FROM Users WHERE user_name = ? AND password = ?",
                (username, password)
            )
            result = cursor.fetchone()
            if result:
                role = result[0].lower()
                print("✅ Login successful.")
                return Admin(username, role) if role == 'admin' else Customer(username, role)
            print("❌ Invalid username or password.")
            return None
        finally:
            conn.close()
