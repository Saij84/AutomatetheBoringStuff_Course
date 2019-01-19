"""
a somple downloader intended to scrape a given webpage, find links and download file based on file format
"""

import os
import urllib3
import certifi
import requests
from bs4 import BeautifulSoup as bs

class DownloadFiles:
    def __init__(self, url, searchExtensionList, path):
        """
        :param url: url address, type -> str
        :param searchExtensionList: ie: ('.mp4', '.jpg'), type -> tuple
        :param save path, type -> str
        """
        self.path = path
        self.url = url
        self.r = requests.get(self.url)
        self.soup = bs(self.r.text, 'html.parser')
        self.searchExtensionList = searchExtensionList
        self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

    def checkDir(self):
        if os.path.exists(self.path):
            return True
        else:
            return False

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
        if self.checkDir() == False:
            os.makedirs(self.path)

        names_urls = zip(self.getNames(), self.getLinks())
        for fileName, url in names_urls:
            rq = self.http.request('GET', url, preload_content=False)
            with open(self.path + fileName, 'wb') as out:
                print('Downloading: {}'.format(fileName))
                while True:
                    data = rq.read(1024)
                    if not data:
                        break
                    out.write(data)
            print('Your file: {} has been downloaded from {}'.format(fileName, url))
            rq.release_conn()

vid_url = 'http://people.csail.mit.edu/costan/mit6006/lectures/'
fileUrl = 'https://courses.csail.mit.edu/6.006/fall11/lectures/'

dlf = DownloadFiles(vid_url, ('webm'), 'algo/video/')

dlf.downloadFile()