import pandas as pd
from datetime import datetime
import time
from bs4 import BeautifulSoup as BS
import sys
from pytz import timezone
import get_stock_data_etl as ETL
import config

stock_data_tabular = {}
base_search_query = 'https://www.google.com/search?q='
time_ = time.strftime("%Y%m%d, %H%M%S", time.localtime()).split(',')[1].strip()
s3client = AWS_S3('StocksBucket',access_key=config.access_key, secret_key=config.secret_key)
s3client.download_from_bucket('stocks.txt','stock_list.txt')
with open('stock_list.txt, 'r') as file:
    stock = f.readline().strip('\n')
    while stock:
        if stock not in stock_data_tabular:
            stock_data_tabular[stock] = pd.DataFrame()
        pipe = ETL.Pipeline(stock)
        pipe.get_data(base_search_query+stock+'stock')
        con = sqlite3.connect('Data.db')
        curr = con.cursor()
        for row in curr.execute('SELECT * FROM '+stock+' ORDER BY  Time DESC LIMIT 1'):
            stock_data_tabular[stock] = stock_data_tabular[stock].append(pd.DataFrame([[row[0], row[-1]]], columns=['Stock_Points', 'Time']),  ignore_index=True)
            stock_data_tabular[stock] = stock_data_tabular[stock].reset_index(drop=True)
        con.close()
        stock = f.readline().strip('\n')
s3client.upload_to_bucket('Data.db','Data.db')
