# Data on the web page is 5 minutes delayed. Real time data is available for small closed circle of people. I will try to scrape historical data using selenium. BeautifulSoup can't
# handle dynamic web pages.

import datetime
import pandas as pd
import path
from bs4 import BeautifulSoup
import requests
import selenium

def save_logs_to_a_file(path, text):
    f = open(path, "a")
    f.write(text)
    f.close()

url = "https://www.binance.com/en/support/announcement/new-cryptocurrency-listing?c=48&navId=48"
html = requests.get(url)

s = BeautifulSoup(html.text, "lxml")
save_logs_to_a_file(path.scraped_data_from_webpage, str(html.content))