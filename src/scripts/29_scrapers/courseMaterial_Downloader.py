import requests
from bs4 import BeautifulSoup as bs
import urllib3

vid_url = 'http://people.csail.mit.edu/costan/mit6006/lectures/'
_URL = 'https://courses.csail.mit.edu/6.006/fall11/lectures/'

# functional


def getNameLinks(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    urls = []
    names = []

    for i, link in enumerate(soup.findAll('a')):
        dlLink = url + link.get('href')
        if dlLink.endswith('.pdf') or dlLink.endswith('.zip') or dlLink.endswith('.webm'):
            urls.append(dlLink)
            names.append(soup.select('a')[i].attrs['href'])
    print(urls)
    print(names)
    return urls, names

getNameLinks(vid_url)


# names_urls = zip(names, urls)
#
# for name, url in names_urls:
#     print(url)
#     rq = urllib3.Request(url)
#     res = urllib3.urlopen(rq)
#     pdf = open("pdfs/" + name, 'wb')
#     pdf.write(res.read())
#     pdf.close()