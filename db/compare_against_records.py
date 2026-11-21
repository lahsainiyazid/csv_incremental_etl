import psycopg
import csv 
from db_url import db_url 

def get_db_ids(url=db_url):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT transaction_id from transactions;")
            ids=cur.fetchall()
            return ids



if __name__=="__main__":
    db_ids=get_db_ids()
    print(db_ids)

