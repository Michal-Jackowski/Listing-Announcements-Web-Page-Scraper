# Data on the web page is 5 minutes delayed. Real time data is available for small closed circle of people. I will try to scrape historical data using Selenium. BeautifulSoup can't
# handle dynamic web pages. After some time Selenium is even worste that BeautifulSoup.

# Get annoucement concrete date and save to file [In progress] (select_page_number is broken, actual order [1, 3, 5, 7] => wrong)
# Filter data (text+date)
# Save all data to one file

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
from bs4 import BeautifulSoup
import time
from lxml import etree

def save_logs_to_a_file(path, text):
    f = open(path, "a", encoding="utf-8")
    f.write(text)
    f.close()

def reject_cookies():
    driver.implicitly_wait(5)
    cookies_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/div/div[1]/div/div[2]/div/button[2]')))
    cookies_button.click()

def scroll_page_down():
    time.sleep(1.25)
    driver.execute_script("window.scrollTo(0, 1000)")

def select_page_number(page_number):
    if page_number <= 5:
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/main/div[2]/div[2]/div[2]/section/div/div[2]/button[' + str(y+page_number) + ']')))
    else:
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/main/div[2]/div[2]/div[2]/section/div/div[2]/button[7]')))
    button.click()

chrome_driver_PATH = "C:/Program Files (x86)/chromedriver.exe"
URL = "https://www.binance.com/en/support/announcement/new-cryptocurrency-listing?c=48&navId=48"

driver = webdriver.Chrome(chrome_driver_PATH)
driver.get(URL)
driver.maximize_window()
time.sleep(2.5)
soup = BeautifulSoup(driver.page_source, 'html.parser')
dom = etree.HTML(str(soup))
driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(1)
number_of_pages = dom.xpath("/html/body/div[3]/div/div/main/div[2]/div[2]/div[2]/section/div/div[2]/button[6]//text()")
driver.execute_script("window.scrollTo(0, 0)")
reject_cookies()

for y in range(1, int(number_of_pages[0])):
    if y != 1:
        scroll_page_down()
        select_page_number(y)
    for x in range(1, 21):
        try:
            time.sleep(1.25)
            annoucement_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div/main/div[2]/div[2]/div[2]/section/div/div[1]/div[" + str(x) + "]/a"))).get_attribute('href')
            if y != 1:
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
            driver.get(str(annoucement_link))
            time.sleep(2.5)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            dom = etree.HTML(str(soup))
            article_header = dom.xpath("/html/body/div[3]/div/div/main/div/div[2]/div/div[2]/div/h1//text()")
            date = dom.xpath("/html/body/div[3]/div/div/main/div/div[2]/div/div[2]/div/div[2]//text()")
            save_logs_to_a_file(path.scraped_data_from_webpage, str(article_header[0]) + "\n" + str(date[0]) + "\n\n")
            time.sleep(1.25)
            if y == 1:
                driver.back()
            else:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
        except NoSuchElementException:
            break

    if int(number_of_pages[0]) == y:
        break