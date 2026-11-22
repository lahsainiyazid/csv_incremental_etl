import psycopg 
from db_url import db_url 



def create_table(url=db_url):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("""CREATE  TABLE IF NOT EXISTS watermarks 
            (pipeline TEXT PRIMARY KEY,
             completed_at TIMESTAMP NOT NULL );""")


if __name__=="__main__":
    create_table()
