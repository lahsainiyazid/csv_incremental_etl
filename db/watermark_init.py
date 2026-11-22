import psycopg 
from db_url import db_url 



def get_last_timestamp(url=db_url):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT max (transaction_date) from transactions;""")
            result=cur.fetchone()
            return result

def watermark_init(url=db_url):
    last_time=get_last_timestamp()
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute ("""
            INSERT INTO watermarks (pipeline,completed_at)
            VALUES (%s,%s);""",("main_pipeline",last_time))


if __name__=="__main__":
    watermark_init()
    print("Watermark successfully inserted!")
