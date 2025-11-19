import sqlite3
import pandas as pd
from app.users import add_user

def migrate_users(conn):
    with open ("DATA/users.txt","r") as f:
        users = f.readlines()

    for users in user:
        name, hash_str = users.strip().split(",")

def migrate_cyber_incidents(conn):
    data1 = pd.read_csv("DATA/cyber_incidents.csv")
    data1.to_sql( 'cyber_incidents', conn, if_exists='append', index=False )
    print("Data load")

def migrate_it_tickets(conn):
    data1 = pd.read_csv("DATA/it.tickets.csv")
    data1.to_sql('it_tickets', conn, if_exists='append', index=False)
    print("Data load")
