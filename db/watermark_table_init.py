import psycopg 
from db_url import db_url 




def water_mark_init(url=db_url):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS watermarks 
            (watermark_id int PRIMARY KEY NOT NULL,
            transaction_id TEXT references transactions(transaction_id),
            created_at TIMESTAMP) ;""")


if __name__=="__main__":
    water_mark_init()

