import httplib2
http=httplib2.Http()
from bs4 import BeautifulSoup

for i in range(53,80):
    status,response=http.request(f'https://climate.nasa.gov/newsletters/{i}')
    for link in BeautifulSoup(response,'html.parser').find_all('a', href=True):
        
        if link['href'].startswith('https://climate.nasa.gov/'):
            with open ('nasaLink.md', 'a+') as a:
                a.write(link['href']+'\n')
                