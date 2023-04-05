import psycopg2
import pandas as pd

def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("connection to redshift made")

    return connect

def extract_transactional_data(dbname, host, port, user, password):
    connect = connect_to_redshift(dbname, host, port, user, password)
    query = '''select o.*,
                      case when s.description = '?' or s.description is null then 'Unknown' else s.description end as description
                from bootcamp1.online_transactions o
                left join bootcamp1.stock_description s 
                on o.stock_code = s.stock_code
                where o.customer_id <> ''
                and o.quantity > 0
                and o.stock_code not in ('BANK CHARGES', 'POSTAGE', 'D', 'M', 'CRUK')
               '''
    online_trans = pd.read_sql(query, connect)
    print ('This number of invoices extracted { online_trans.shape[0]}')

    return online_trans