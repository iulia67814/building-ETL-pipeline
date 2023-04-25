# Import Libraries
import os
import pandas as pd

#from dotenv import load_dotenv # use this library for testing on your machine
#load_dotenv()  # only for local testing

from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicated_values
from src.load_data_to_s3 import df_to_s3

# import from .env
dbname = os.getenv('dbname')
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key_id = os.getenv("aws_secret_access_key_id")


# extract data
ot_data = extract_transactional_data(dbname, host, port, user, password)

# transform data
ot_data_cleaned = identify_and_remove_duplicated_values(ot_data)
print(ot_data_cleaned.head())

# fix the invoice date
print("Transforming data - fixing date time")
ot_data_final = ot_data_cleaned.copy()
ot_data_final['invoice_date'] = pd.to_datetime(ot_data_final['invoice_date'])

# load data
key = 'online_transactions_transformation/final/ii_online_transactions.csv '
s3_bucket = 'waia-data-dump'
df_to_s3(ot_data_final, key, s3_bucket, aws_access_key_id, aws_secret_access_key_id)

#execution_time = datetime.now() - start_time
#print(f'')