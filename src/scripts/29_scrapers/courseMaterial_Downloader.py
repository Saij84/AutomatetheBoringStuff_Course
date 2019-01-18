import requests
import certifi
from bs4 import BeautifulSoup as bs
import urllib3
import os

vid_url = 'http://people.csail.mit.edu/costan/mit6006/lectures/'
fileUrl = 'https://courses.csail.mit.edu/6.006/fall11/lectures/'

# functional

class DownloadFiles:
    def __init__(self, url, searchExtensionList, path):
        """
        :param url: url address, type -> str
        :param searchExtensionList: ie: ('.mp4', '.jpg'), type -> tuples
        :param save path, type -> str
        """
        self.path = path
        self.url = url
        self.r = requests.get(self.url)
        self.soup = bs(self.r.text, 'html.parser')
        self.searchExtensionList = searchExtensionList
        self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
                                        ca_certs=certifi.where())

    def getLinks(self):
        urls = []

        for link in self.soup.findAll('a'):
            dlLink = self.url + link.get('href')
            if dlLink.endswith(self.searchExtensionList):
                urls.append(dlLink)
        return urls

    def getNames(self):
        names = []

        for index, link in enumerate(self.soup.findAll('a')):
            dlLink = self.url + link.get('href')
            if dlLink.endswith(self.searchExtensionList):
                names.append(self.soup.select('a')[index].attrs['href'])
        return names

    def downloadFile(self):

        names_urls = zip(self.getNames(), self.getLinks())

        for name, url in names_urls:
            print(name, url)
            rq = self.http.request('GET', url, preload_content=False)
            with open(self.path + name, 'wb') as out:
                while True:
                    data = rq.read(1024)
                    if not data:
                        break
                    out.write(data)
            rq.release_conn()


path = r"C:\tools\AutomatetheBoringStuff_Course\src\scripts\29_scrapers\pdfs"
dlf = DownloadFiles(fileUrl, ('pdf'), 'pdfs/')

dlf.downloadFile()


