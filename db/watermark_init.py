import psycopg 
from db_url import db_url 



def get_last_info(url=db_url):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT (transaction_id,transaction_date) from transactions
            order by transaction_id DESC 
            LIMIT 1 ;""")
            result=cur.fetchone()
            return result[0]

def watermark_init(url=db_url):
    last_info=get_last_info()
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute ("""
            INSERT INTO watermarks (pipeline,last_id,last_timestamp)
            VALUES (%s,%s,%s);""",("main_pipeline",last_info[0],last_info[1]))


if __name__=="__main__":
   watermark_init()
   print("Watermark table successufly initialized!")

