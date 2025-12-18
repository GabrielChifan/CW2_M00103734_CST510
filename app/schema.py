


def create_user_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS users ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        username TEXT NOT NULL UNIQUE, 
        password_hash TEXT NOT NULL ) 
        """)
    conn.commit()
    print("User table created successfully!")


