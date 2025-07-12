from model.user import Customer, Admin
from system.booking_system import BookingSystem
from db.database import DatabaseManager

def customer_menu(user_obj):
    while True:
        print("\n--- Customer Menu ---")
        print("1. Book Cab")
        print("2. View Booking History")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            pickup = input("Enter pickup location: ")
            drop = input("Enter drop location: ")
            user_obj.book_cab(pickup, drop)
        elif choice == '2':
            user_obj.view_history()
        elif choice == '3':
            print("Logged out.")
            break
        else:
            print("Invalid choice.")

def admin_menu(admin_obj):
    while True:
        print("\n--- Admin Menu ---")
        print("1. View All Bookings")
        print("2. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            admin_obj.view_all_bookings()
        elif choice == '2':
            print("Logged out.")
            break
        else:
            print("Invalid choice.")

def main():
    # Ensure tables exist before starting
    DatabaseManager().create_table()

    system = BookingSystem()

    while True:
        print("\n=== 🚖 Cab Booking System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            role = input("Role (customer/admin): ").lower()
            if role not in ['customer', 'admin']:
                print("Invalid role.")
                continue
            system.register(username, password, role)

        elif choice == '2':
            username = input("Username: ")
            password = input("Password: ")

            user_obj = system.login(username, password)
            if user_obj:
                user_obj.display()
                if isinstance(user_obj, Customer):
                    customer_menu(user_obj)
                elif isinstance(user_obj, Admin):
                    admin_menu(user_obj)
            else:
                print("Login failed.")

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
