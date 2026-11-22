import csv
import psycopg  
from psycopg.rows import dict_row
from datetime import datetime 
from decimal import Decimal 
from db_url import db_url


def get_watermark_main(url=db_url):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT last_timestamp from watermarks 
            where pipeline='main_pipeline' ;""")
            row=cur.fetchone()
            return row[0]

def read():
    with open ("/home/yazid/incremental_etl/data/transactions_batch_2.csv","r",encoding="utf-8") as f:
        rows=csv.reader(f)
        row_count=0 
        my_rows=[]
        for row in rows:
            row_count+=1 
            if (row_count==1):
                continue
            my_rows.append(row)
        return my_rows
def validate():
    rows=read()
    watermark=get_watermark_main()
    cleaned_rows=[]
    for row in rows:
        if (datetime.fromisoformat(row[1])<watermark):
            continue 
        transaction_id=row[0]
        transaction_timestamp=datetime.fromisoformat(row[1])
        account_id=row[2],
        transaction_type=row[3]
        amount=Decimal(row[4])
        cleaned_rows.append([transaction_id,transaction_timestamp,account_id,amount])
    return cleaned_rows

def insert_clean_valid_rows(url=db_url):
    clean=validate()
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.executemany("""
            INSERT INTO transactions (transaction_id,transaction_date,
            account_id,transaction_type,amount)
            values (%s,%s,%s,%s,%s);
                            """,clean)



if __name__=="__main__":
    insert_clean_valid_rows()
    print("Successfully inserted clean rows!")


