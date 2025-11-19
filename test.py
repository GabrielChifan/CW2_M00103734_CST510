import sqlite3
import pandas as pd
import main
import login

def create_user_table():
    curr = conn.cursor()
    sql = (""" CREATE TABLE IF NOT EXISTS users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT NOT NULL UNIQUE, 
    password_hash TEXT NOT NULL, 
     ) """)
    curr.execute(sql)
    conn.commit()





conn = sqlite3.connect("DATA/telligence_platform.db")
