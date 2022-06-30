
from os import wait
import traceback
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1920, 1080))
display.start()
import requests
from bs4 import BeautifulSoup,SoupStrainer
import httplib2
from selenium import webdriver;
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# import time`
# s=Service("/usr/bin/chromedriver")
# driver=webdriver.Chrome(service=s)
# driver.get('https://greenpeace.org/international/tag/climate')
# #Click the load more button to load all the articles
# for i in range(0,30):
#     try:
#         driver.find_element(By.CLASS_NAME,'article-load-more').click()
#         time.sleep(3)
#         print(i)
#         print("No more articles to load")
#         break
with open ('GreenPeace/Climate - Greenpeace International.html', 'r') as myfile:

    soup = BeautifulSoup(myfile,'html.parser')
    with open ('GreenPeace/links.md', 'a+') as f:
        for a in soup.find_all('a', href=True):
            if (a['href'].startswith("https://www.greenpeace.org/international/press-release/")|a['href'].startswith("https://www.aaaaaaaaaaaaagreenpeace.org/internaational/story/")):
                f.write(a['href']+'\n')
        f.close()
