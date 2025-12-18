import sqlite3
import pandas as pd
from app.db import get_connection
conn = get_connection()


def migrate_datasets_metadata(conn):
    path = r"DATA\datasets_metadata.csv"
    df = pd.read_csv(path)
    print(df.head())
    df.to_sql('datasets_metadata', conn, if_exists='append', index=False)
    print('Data loaded successfully !')

def migrate_it_tickets(conn):
    path = r"DATA\it_tickets.csv"
    df = pd.read_csv(path)
    print(df.head())
    df.to_sql('it_tickets', conn, if_exists='append', index=False)
    print('Data loaded successfully !')

#--------------get data-----------------

migrate_it_tickets(conn)
migrate_datasets_metadata(conn)