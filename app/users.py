from app.db import get_connection
import bcrypt

conn = get_connection()


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def verify_password(stored_password: str, provided_password: str) -> bool:
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))


def user_registration(conn):
    # exist = False
    name = input('Enter username: ')
    password = input('Enter password: ')
    hash = hash_password(password)
    set_user(conn, name, hash)
    print('User Registerd Successfuly')


def user_login(conn, name, password) -> bool:
    #name = input('Enter your name to log in: ')
    #password = input('Enter your password: ')
    id, name, hash = get_one_user(conn, name)
    print(f'Welcome {name}!')

    if name == name and verify_password(hash, password):
        return True
    else:
        return False


def set_user(conn, name, hash):
    curr = conn.cursor()
    sql = """INSERT INTO users (username, password_hash) VALUES (?,?)"""
    param = (name, hash)
    curr.execute(sql, param)
    conn.commit()


def get_all_users(conn):
    curr = conn.cursor()
    sql = """SELECT * FROM users"""
    curr.execute(sql)
    all_users = curr.fetchall()
    '''
    for i in all_users:
        print(i)
    user = curr.execute()
    '''
    return all_users


def get_one_user(conn, name):
    curr = conn.cursor()
    sql = """SELECT * FROM users WHERE username = ?"""
    param = (name,)
    curr.execute(sql, param)
    user = curr.fetchone()
    return (user)


def delete_user(conn, name):
    curr = conn.cursor()
    sql = """DELETE FROM users  WHERE username = ?"""
    param = (name,)
    curr.execute(sql, param)
    conn.commit()
    print(f'{name} was successfully deleted!')


def update_user(conn, old_name, new_name):
    curr = conn.cursor()
    sql = """UPDATE users SET user_name = ? WHERE user_name = ?"""
    param = (new_name, old_name)
    curr.execute(sql, param)
    conn.commit()


def migrate_users(conn):
    with open('DATA/users.txt', 'r') as f:
        users = f.readlines()
        for user in users:
            name, hash = user.strip().split(':')
            set_user(conn, name, hash)
       # conn.close()

    migrate_users(conn)