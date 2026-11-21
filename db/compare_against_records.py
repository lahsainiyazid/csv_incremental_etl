import psycopg
from psycopg.rows import dict_row 
import csv 
from db_url import db_url 
from decimal import Decimal   
def get_db_ids(url=db_url):
    with psycopg.connect(url,row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT transaction_id from transactions;")
            ids=cur.fetchall()
            return ids

def get_csv_ids():
    ids=[]
    with open("/home/yazid/incremental_etl/data/transactions.csv","r",encoding="utf-8") as f :
        reader=csv.reader(f)
        count=0 
        for row in reader:
            count+=1 
            if count==1:
                continue 
            ids.append(row)

        return ids
def insert_row(row,url=db_url):
    with psycopg.connect(url=db_url) as conn:
        with conn.cursor() as cur:
            cur.exectue("""INSERT INTO transactions 
            (transaction_id,transaction_date,account_id,transaction_type) 
            values (%s,%s,%s,%s) ;""",(row[0],row[1],row[2],row[3]))

if __name__=="__main__":
    db_ids=get_db_ids()
    my_csv=get_csv_ids()
    print (my_csv)

