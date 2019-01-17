import requests
from bs4 import BeautifulSoup as bs
import urllib3

vid_url = 'http://people.csail.mit.edu/costan/mit6006/lectures/'
fileUrl = 'https://courses.csail.mit.edu/6.006/fall11/lectures/'

# functional

class DownloadFiles:
    def __init__(self, url, searchFormatList):
        self.url = url
        self.r = requests.get(self.url)
        self.soup = bs(self.r.text, 'html.parser')
        self.searchFormatList = searchFormatList

    def getLinks(self):
        urls = []

        print(self.searchFormatList)
        for i, link in enumerate(self.soup.findAll('a')):
            dlLink = self.url + link.get('href')
            if dlLink.endswith(('.pdf', '.zip')):
                urls.append(dlLink)
        return urls

    def getNames(self):
        names = []

        for i, link in enumerate(self.soup.findAll('a')):
            dlLink = self.url + link.get('href')
            if dlLink.endswith('.pdf') or dlLink.endswith('.zip') or dlLink.endswith('.webm'):
                names.append(self.soup.select('a')[i].attrs['href'])
        return names

dlf = DownloadFiles(vid_url, ('.pdf', '.zip'))

names = dlf.getLinks()

print(names)

# names_urls = zip(names, urls)
#
# for name, url in names_urls:
#     print(url)
#     rq = urllib3.Request(url)
#     res = urllib3.urlopen(rq)
#     pdf = open("pdfs/" + name, 'wb')
#     pdf.write(res.read())
#     pdf.close()