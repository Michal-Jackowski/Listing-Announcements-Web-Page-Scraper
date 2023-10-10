# Data on the web page is 5 minutes delayed. Real time data is available for small closed circle of people. I will try to scrape historical data using Selenium.

# Add function to append xlsx file with new articles when there will be something new
# Filter data (text + date) => Listing Spot, Listing Futures
# Save all data to one file => xlsx file
# Save all results to one file => pdf file

from xml.dom.pulldom import END_ELEMENT
import pandas as pd
import path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
from lxml import etree
import datetime

def save_logs_to_a_file(path, text):
    f = open(path, "a", encoding="utf-8")
    f.write(text)
    f.close()

def reject_cookies():
    cookies_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/div/div[1]/div/div[2]/div/button[2]')))
    cookies_button.click()

def scroll_page_down():
    time.sleep(1.25)
    driver.execute_script("window.scrollTo(0, 1000)")

def select_page_number(page_number):
    i = 12
    while i >= 7:
        i -= 1
        try:
            print("Looking for another page." + " [Page number = " + str(page_number) + "]")
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/main/div[2]/div[2]/div[2]/section/div/div[2]/button[' + str(i) + ']')))
            button.click()
            break
        except:
            pass

df = pd.DataFrame()
chrome_driver_PATH = "C:/Program Files (x86)/chromedriver.exe"
URL = "https://www.binance.com/en/support/announcement/new-cryptocurrency-listing?c=48&navId=48"

driver = webdriver.Chrome(chrome_driver_PATH)
driver.get(URL)
driver.maximize_window()
time.sleep(2.5)
soup = BeautifulSoup(driver.page_source, 'html.parser')
dom = etree.HTML(str(soup))
reject_cookies()
time.sleep(1)
driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(1)
number_of_pages = dom.xpath("/html/body/div[3]/div/div/main/div[2]/div[2]/div[2]/section/div/div[2]/button[6]//text()")
driver.execute_script("window.scrollTo(0, 0)")
list_index_out_of_range = False

for y in range(1, (int(number_of_pages[0]) + 1)):
    if y != 1:
        time.sleep(1)
        scroll_page_down()
        select_page_number(y)
    # To prevent "HTTP ERROR 429" wait 15 minutes after 3 pages is scraped
    if y % 4 == 0:
        print("15 minutes cooldown." + " [Page number = " + str(y) + "]")
        time.sleep(60*15)
    for x in range(1, 21):
        try:
            if (list_index_out_of_range):
                # Try to get data from previous aricles
                x -= 1
                print("15 minutes cooldown." + " [Page number = " + str(y) + "]")
                time.sleep(60*15)
                list_index_out_of_range = False
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            if (x > 0):
                time.sleep(1.25)
                annoucement_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/main/div[2]/div[2]/div[2]/section/div/div[1]/div[" + str(x) + "]/a"))).get_attribute('href')
            if y != 1:
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
            if (x > 0):
                driver.get(str(annoucement_link))
                time.sleep(2.5)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                dom = etree.HTML(str(soup))
                article_header = dom.xpath("/html/body/div[3]/div/div/main/div/div[2]/div/div[2]/div/h1//text()")
                date = dom.xpath("/html/body/div[3]/div/div/main/div/div[2]/div/div[2]/div/div[2]//text()")
                data = {"Date" : str(date[0]), "Article Header" : str(article_header[0])}
                temp_df = pd.DataFrame(data, index=[1])
                df = df._append(temp_df)
                time.sleep(1.25)
            if y == 1:
                driver.back()
            else:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
        except NoSuchElementException:
            print("No such element found exception.")
            break 
        except IndexError:
            #Couldn't get data from list because of "HTTP ERROR 429
            list_index_out_of_range = True
        except TimeoutException:
            #Couldn't get another article because there aren't more
            print("I can't find an item at a specific time.")
            break 

    if int(number_of_pages[0]) == y:
        break

writer = pd.ExcelWriter(path.scraped_data_from_webpage_excel.format(datetime.date.today()), engine='xlsxwriter')
df.to_excel(writer, sheet_name="MySheet", index=False)

workbook = writer.book
worksheet = writer.sheets['MySheet']

for i, col in enumerate(df.columns):
    width = max(df[col].apply(lambda x: len(str(x))).max(), len(col))
    worksheet.set_column(i, i, width)

writer._save()
driver.close()
print("Saving to the xlsx file was successful.")