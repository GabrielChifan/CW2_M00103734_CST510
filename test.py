import sqlite3
from app.schema import create_user_table
from app.users import migrate_users, get_all_users
import pandas as pd



def migrate_cyber(conn):
    data = pd.read_csv("DATA/cyber_incidents.csv")
    data.to_sql('cyber_incidents', conn)

def migrate_it(conn):
    data = pd.read_csv("DATA/it_tickets.csv")
    data.to_sql('it_tickets', conn)

def migrate_metadata(conn):
    data = pd.read_csv("DATA/datasets_metadata.csv")
    data.to_sql('datasets_metadata', conn)


conn = sqlite3.connect('DATA/intelligence_platform.db')
data = pd.read_sql('SELECT * from it_tickets', conn)
print(data)
conn.close()
