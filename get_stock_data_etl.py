import requests
import sqlite3
from datetime import date

# !pip install selenium
# !apt-get update 
# !apt install chromium-chromedriver
# !cp /usr/lib/chromium-browser/chromedriver /usr/bin
# !pip install pyvirtualdisplay
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
import time
#!pip3 install requests requests selectorlib
#!pip install beautifulsoup4
from bs4 import BeautifulSoup as BS
price = []
increase = []
percent = []

def scrollDown(browser, numberOfScrollDowns):
    body = browser.find_element_by_tag_name("body")
    while numberOfScrollDowns >=0:
        body.send_keys(Keys.PAGE_DOWN)
        numberOfScrollDowns -= 1
    return browser

import os

class Pipeline():
    def __init__(self, table_name):
        dt = time.strftime("%Y%m%d, %H:%M:%S", time.localtime()).split(',')
        self.date = dt[0].strip()
        self.time = dt[1].strip()
        self.table = table_name
        self.createTable(table_name)
    
    def createTable(self, table):
        self.con = sqlite3.connect('Data.db')
        self.curr = self.con.cursor()
        self.curr.execute("CREATE TABLE IF NOT EXISTS "+table+" (Price float, Increase float, Percent text, Date text, Time datetime);")
        self.con.commit()
        self.con.close()

    def get_data(self, site):
        self.extract(site)
        self.transform()
        self.load_database()

    def extract(self, link):
        r = requests.get(link)
        self.site = BS(r.content, 'html.parser')
    
    def transform(self):
        data = self.site.find('div', class_='BNeawe iBp4i AP7Wnd').text.split(' ')
        price.append(float(''.join(data[0].split(','))))
        increase.append(float(data[1]))
        percent.append(data[2][1:5])
    
    def load_database(self):
        self.con = sqlite3.connect('Data.db')
        self.curr = self.con.cursor()
        self.time = time.strftime("%Y%m%d, %H:%M:%S", time.localtime()).split(',')[1].strip()
        self.date = time.strftime("%Y%m%d, %H:%M:%S", time.localtime()).split(',')[0].strip()
        self.curr.execute("INSERT OR IGNORE INTO "+self.table+" VALUES (?, ?, ?, ?, ?)", [price[-1], increase[-1], percent[-1], self.date, self.time])
        self.con.commit()
        self.con.close()

#pipe = Pipeline('NIK_STOCK')
#pipe.get_data('https://www.google.com/search?q=nikkei+stock')
