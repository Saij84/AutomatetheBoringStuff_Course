import bs4
import requests

url = "https://courses.csail.mit.edu/6.006/fall11//lectures/"
req = requests.get(url)
req.raise_for_status()

soup = bs4.BeautifulSoup(req.text, features="html.parser")

items = soup.find("href")
print(items)
for item in items:
    print(item)