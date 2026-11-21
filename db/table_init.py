import psycopg 
from db_url import db_url 


def create_table(url=db_url):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS transactions 
            (transaction_id TEXT PRIMARY KEY  ,transaction_date TIMESTAMP NOT NULL  ,
        account_id TEXT NOT NULL  ,transaction_type TEXT NOT NULL ,
        amount NUMERIC(14,2) NOT NULL);
                        """)

if __name__=="__main__":
    create_table()
