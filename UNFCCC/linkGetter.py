#Scraps all the articles from https://unfccc.int/news?field_page_main_text_body_value=2022,
#https://unfccc.int/news?field_page_main_text_body_value=2021 and 
#https://unfccc.int/news?field_page_main_text_body_value=2020 using Selenium and BeautifulSoup.
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()
import requests
from bs4 import BeautifulSoup,SoupStrainer
import httplib2
from selenium import webdriver;
from selenium.webdriver.chrome.service import Service
s=Service("/usr/bin/chromedriver")
driver=webdriver.Chrome(service=s)

http=httplib2.Http()
for year in range(2022,2023):
    driver.get("https://unfccc.int/news?field_page_main_text_body_value="+str(year))
    soup = BeautifulSoup(driver.page_source,'html')
    with open ('UNFCCC/links.md', 'a+') as f:
        for a in soup.find_all('a', href=True):
            if (a['href'].startswith("https://unfccc.int/news/")):
                f.write(a['href']+'\n')
        f.close()
    