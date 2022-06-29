#Scraps all the articles from https://unfccc.int/news?field_page_main_text_body_value=2022,
#https://unfccc.int/news?field_page_main_text_body_value=2021 and 
#https://unfccc.int/news?field_page_main_text_body_value=2020 using Selenium and BeautifulSoup.

import requests
from bs4 import BeautifulSoup,SoupStrainer
import httplib2
from selenium import webdriver;
http=httplib2.Http()
for year in range(2020,2022):
    status,res=http.request(f'https://unfccc.int/news?field_page_main_text_body_value={year}')
    soup = BeautifulSoup(res, features='html.parser')
    with open ('GreenPeace/links.md', 'a+') as f:
        for a in soup.find_all('a', href=True):
            
            f.write(a['href']+'\n')
f.close()
    