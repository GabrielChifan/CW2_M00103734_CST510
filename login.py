import bcrypt

def hash_password(pwd):
    hashed = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')  # store as UTF-8 string

def validate_password(pwd, hashed):
    try:
        hashed_bytes = hashed.encode('utf-8')
        return bcrypt.checkpw(pwd.encode('utf-8'), hashed_bytes)
    except ValueError:
        return False

def register_user():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    hashed_password = hash_password(password)

    f = open("users.txt", "a")
    try:
        f.write(f"{username}:{hashed_password}\n")
    finally:
        f.close()

    print("User registered successfully!\n")

def login_user():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    try:
        f = open("users.txt", "r")
        try:
            lines = f.readlines()
        finally:
            f.close()
    except FileNotFoundError:
        print("No users found. Please register first.")
        return

    for line in lines:
        line = line.strip()
        if not line or ":" not in line:
            continue

        u_name, hash_str = line.split(":", 1)
        u_name = u_name.strip()
        hash_str = hash_str.strip()

        if u_name == username and validate_password(password, hash_str):
            print(f"Welcome, {username}!")
            return

    print("Invalid username or password.")
