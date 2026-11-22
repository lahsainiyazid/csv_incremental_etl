import csv
import psycopg  
from psycopg.rows import dict_row
from datetime import datetime 
from decimal import Decimal 
from db_url import db_url


def get_watermark_main(url=db_url):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT * from watermarks 
            where pipeline='main_pipeline' ;""")
            row=cur.fetchone()
            return row

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
    cleaned_rows=[]
    for row in rows:
        transaction_id=row[0]
        transaction_timestamp=datetime.timestamp(row[1])
        account_id=row[2]
        amount=Decimal(row[3])
        cleaned_rows.append([transaction_id,transaction_timestamp,account_id,amount])
    return cleaned_rows



if __name__=="__main__":
    my_r =validate()
    print(my_r)
