import bs4
import requests

url = "https://www.amazon.com.au/Python-Playground-Mahesh-Venkitachalam/dp/1593276044/ref=sr_1_2?ie=UTF8&qid=1547583199&sr=8-2&keywords=automate+the+boring+stuff+with+python"

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")
elems = soup.select("#priceblock_ourprice")

titleElems = soup.select("#productTitle")

print((titleElems[0].text).strip(), (elems[0].text).strip())
