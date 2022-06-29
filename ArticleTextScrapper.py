
# get the text from the links in nasaLinks.md
# each link should be printed in a new file
from bs4 import BeautifulSoup	
import httplib2
http=httplib2.Http()
with open ('GreenPeace/links.md', 'r') as a:
    for line in a:
        with open('fineTuningData.jsonl', 'a+') as f:
            status,response=http.request(line)
            soup=BeautifulSoup(response, 'html.parser')
            f.write("{\"prompt\":\"\",\"completion\":\"")
            for p in soup.find_all('p'):
                f.write(p.text)
            f.write("\"}\n")