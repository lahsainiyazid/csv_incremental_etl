import psycopg
from psycopg.rows import dict_row 
import csv 
from db_url import db_url 
from decimal import Decimal   


def get_csv_rows():
    records=[]
    with open("/home/yazid/incremental_etl/data/transactions.csv","r",encoding="utf-8") as f:
        rows=csv.reader(f)
        row_count=0 
        for row in rows:
            row_count+=1 
            if (row_count==1):
                    continue
            records.append(row)
        return records
def insert_rows(url=db_url):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            rows=get_csv_rows()
            for row in rows:
                cur.execute("""
                INSERT INTO transactions 
                (transaction_id,transaction_date,account_id,transaction_type,amount)
                values (%s,%s,%s,%s,%s);
                            """,(row[0],row[1],row[2],row[3],row[4]))


if __name__=="__main__":
    insert_rows()
