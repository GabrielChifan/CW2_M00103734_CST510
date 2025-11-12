import bcrypt
import login
from login import register_user, login_user

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. STOP")
        choice = input("Choose (1 2 3): ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("GOOD BYE!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
