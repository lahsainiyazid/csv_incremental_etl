import os 
from dotenv import load_dotenv,find_dotenv 


_=load_dotenv(find_dotenv())

db_url=os.environ.get("DB")
print(db_url)
