import sqlite3

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('cabbook.db')
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT UNIQUE NOT NULL,
                password TEXT,
                role TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS CABS (
                CAB_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                CAB_TYPE TEXT,
                IS_AVAILABLE INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS BOOKINGS (
                BOOKING_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USER_ID INTEGER,
                CAB_ID INTEGER,
                PICKUP TEXT,
                DROP_LOCATION TEXT,
                TIMESTAMP TEXT,
                FOREIGN KEY (USER_ID) REFERENCES Users(USER_ID),
                FOREIGN KEY (CAB_ID) REFERENCES CABS(CAB_ID)
            )
        ''')

        self.conn.commit()

def get_connection():
    conn = sqlite3.connect('cabbook.db')
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
