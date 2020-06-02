
import requests
from bs4 import BeautifulSoup

URL = "http://www.srikanthtechnologies.com/rss.xml"
resp = requests.get(URL)
if resp.status_code != 200:
    print("Sorry! Could not get data from srikanthtechnologies.com")
    exit(1)


bs = BeautifulSoup(resp.text,"lxml-xml")

for item in bs.find_all("item"):
    title = item.find("title")
    pubDate = item.find("pubDate")
    if '2020' in pubDate.text:
        print(title.text.strip())
        print(pubDate.text)
        print('-' * 70)



