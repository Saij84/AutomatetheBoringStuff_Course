import bs4
import requests

url = "https://www.amazon.com.au/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords=books&rh=n%3A4851626051%2Ck%3Abooks"

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")
for item in range(9):
    titleElems = soup.select("#result_{} > div > div > div > div.a-fixed-left-grid-col.a-col-right > "
                             "div.a-row.a-spacing-small > div:nth-child(1) > a > h2".format(item))

    paperBackPriceElems = soup.select("#result_{} > div > div > div > div.a-fixed-left-grid-col.a-col-right > "
                             "div:nth-child(2) > div.a-column.a-span7 > div:nth-child(2) > a > "
                             "span.a-size-base.a-color-price.s-price.a-text-bold".format(item))

    print(titleElems[0].text.strip())
    print(paperBackPriceElems[0].text.strip())
#centerpanelfull > ul:nth-child(3) > li:nth-child(1) > a:nth-child(3)