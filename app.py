from db_manager import register_user, login_user, update_address, update_password, delete_account
from exceptions import UserExistsError, InvalidCredentialsError

current_user = None  # Logged in user data

def show_main_menu():
    print("+----------------------------------+")
    print("|         USER MANAGEMENT APP      |")
    print("+----------------------------------+")
    print("| 1. Login                         |")
    print("| 2. Register                      |")
    print("| 3. Logout                        |")
    print("| 4. Exit the App                  |")
    print("+----------------------------------+")

def show_user_menu():
    print(f"\n+----------------------------------+")
    print(f"|    Welcome, {current_user['name']}!              |")
    print("+----------------------------------+")
    print(f"| ID       : {current_user['id']}")
    print(f"| Name     : {current_user['name']}")
    print(f"| Username : {current_user['username']}")
    print(f"| Address  : {current_user['address']}")
    print("+----------------------------------+")
    print("| 1. Change Password               |")
    print("| 2. Change Address                |")
    print("| 3. Delete My Account             |")
    print("| 4. Logout                        |")
    print("+----------------------------------+")

def main():
    global current_user

    while True:
        if current_user is None:
            show_main_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                try:
                    current_user = login_user(username, password)
                    print(f"\n  Login successful! Welcome {current_user['name']}!\n")
                except InvalidCredentialsError as e:
                    print(" X ", e)

            elif choice == '2':
                name = input("Enter name: ")
                username = input("Enter username: ")
                password = input("Enter password: ")
                address = input("Enter address: ")
                try:
                    print(register_user(name, username, password, address))
                except UserExistsError as e:
                    print(" X ", e)

            elif choice == '3':
                print("! You are not logged in yet!")

            elif choice == '4':
                print(" Exiting the app... Goodbye!")
                break

            else:
                print(" Invalid choice, please try again!")

        else:
            show_user_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                new_password = input("Enter new password: ")
                print(update_password(current_user['id'], new_password))

            elif choice == '2':
                new_address = input("Enter new address: ")
                print(update_address(current_user['id'], new_address))

            elif choice == '3':
                confirm = input("Are you sure you want to delete your account? (y/n): ")
                if confirm.lower() == 'y':
                    print(delete_account(current_user['id']))
                    current_user = None
                else:
                    print("Account deletion cancelled.")

            elif choice == '4':
                print(f" Logged out from {current_user['username']}.")
                current_user = None

            else:
                print(" Invalid choice, please try again!")

if __name__ == "__main__":
    main()
