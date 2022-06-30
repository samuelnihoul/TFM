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
with open ('GreenPeace/links.md', 'r') as a:
    for line in a:
        with open('data2.jsonl', 'a+') as f:
            driver.get(line)
            soup=BeautifulSoup(driver.page_source, 'html.parser')
            f.write("{\"prompt\":\"\",\"completion\":\"")
            for p in soup.find_all('p'):
                f.write(p.text.replace('\"','\uff02'))
            f.write("\"}\n")