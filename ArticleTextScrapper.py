
# get the text from the links in nasaLinks.md
# each link should be printed in a new file
import bs4 as BeautifulSoup	
import httplib2
http=httplib2.Http()
with open ('nasaLinks.md', 'r') as a:
    for line in a:
        with open('fineTuningData.jsonl', 'a+') as f:
            status,response=http.request(line)
            soup=BeautifulSoup(response, 'html.parser')
            for p in soup.find_all('p'):
                f.write("{\"prompt\":\"\",\"completion\":\""+p.text+"\"}\n")