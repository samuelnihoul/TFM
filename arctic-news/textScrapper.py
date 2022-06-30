#Scrap the text from the articles using Selenium and BeautifulSoup.
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

import httplib2
http=httplib2.Http()
for year in range(2020,2023):
    with open('data2.jsonl', 'a+') as f:
        driver.get(f'https://arctic-news.blogspot.com/{year}/')
        soup=BeautifulSoup(driver.page_source, 'html.parser')
        f.write("{\"prompt\":\"\",\"completion\":\"")
        for p in soup.find_all('div'):
            f.write("{\"prompt\":\"\",\"completion\":\"")
            f.write(p.text.replace('\"','\uff02'))
            f.write("\"}\n")
        f.close()