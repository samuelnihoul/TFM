
# #Count the number of words in all the Nasa articles
# from bs4 import BeautifulSoup	
# import httplib2
# http=httplib2.Http()
# count=0
# with open ('nasaLinks.md', 'r') as a:
#     for line in a:
#         with open('fineTuningData.jsonl', 'a+') as f:
#             status,response=http.request(line)
#             soup=BeautifulSoup(response, 'html.parser')
#             for p in soup.find_all('p'):
#                 count+=len(p.text.split())

#     print(count)
#     #349827

#Count the number of words in the 3 .md files
f1='/IPPC/GlobalWarmingClean.md'
f2='IPCC/UnitedScienc2021clean.md'
f3='IPCC/UnitedScience2020Clean.md'
count=0
for f in (f1,f2,f3):
    with open(f, 'r') as a:
        for line in a:
            count+=len(line.split())
print(count)

