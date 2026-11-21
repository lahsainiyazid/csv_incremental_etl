import psycopg 
from db_url import db_url 


def get_watermark(url=db_url):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            SELECT max(transaction_date) from transactions; 
                        """)
            result=cur.fetchone()
            return result 

    

if __name__=="__main__":
    water=get_watermark()
    print(water)
