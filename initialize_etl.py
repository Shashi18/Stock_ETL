import pandas as pd
from datetime import datetime
import time
from bs4 import BeautifulSoup as BS
import sys
from pytz import timezone
import get_stock_data_etl as ETL

stock_data_tabular = {}
time_ = time.strftime("%Y%m%d, %H%M%S", time.localtime()).split(',')[1].strip()
marketOpen = 9
marketClose = 15
time_tokyo = int(datetime.now(timezone('Asia/Tokyo')).strftime('%H'))
time_tokyo_HM = int(datetime.now(timezone('Asia/Tokyo')).strftime('%H%M'))

with open('stock_lixt.txt, 'r') as file:
    stock = f.readline()
    while stock:
        if stock not in stock_data_tabular:
            stock_data_tabular[stock] = pd.DataFrame([[0, 0]])
            stock_data_tabular[stock].columns = [stock+'_Points','Time']
        pipe = ETL.Pipeline(stock)
        pipe.get_data('https://www.google.com/search?q='+stock+'stock')
        con = sqlite3.connect('Data.db')
        curr = con.cursor()
        for row in curr.execute('SELECT * FROM NIK_STOCK'):
            stock_data_tabular[stock] = stock_data_tabular[stock].append(pd.DataFrame([[time_tokyo_HM, row[-1]]], columns=['NIK', 'Time']),  ignore_index=True)
        con.close()
        time_tokyo = int(datetime.now(timezone('Asia/Tokyo')).strftime('%H'))
        stock = f.readline()
