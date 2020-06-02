
import requests
from bs4 import BeautifulSoup

website = "http://www.srikanthtechnologies.com"
resp = requests.get(website)
if resp.status_code != 200:
    print("Sorry! Could not get data from srikanthtechnologies.com")
    exit(1)


bs = BeautifulSoup(resp.text,"html.parser")

for anchor in bs.find_all("a"):
    href = anchor['href']
    text = anchor.text
    if href == "#":
        continue

    if not href.startswith("http"):
        href = website + "/" + href

    if len(text.strip()) != 0:
        print(f"{text}\n{href}")
    else:
        print(href)



