import sqlite3
import pandas as pd

conn = sqlite3.connect("DATA/telligence_platform.db")


def add_user(conn, name, hash_str):
    curr = conn.cursor()
    sql = (""" INSERT INTO users (username, password_hash) VALUES (?, ?) """)

    param = (name, hash_str)
    curr.execute(sql, param)
    conn.commit()

def get_all_users(conn):
    curr = conn.cursor()
    sql = ("""SELECT * FROM user""")
    curr.execute(sql)
    user = curr.fetchall()
    conn.close()
    return user



def get_all_users_pandas():
    query = "SELECT * FROM user"
    df = pd.read_sql(query, conn)
    return(df)