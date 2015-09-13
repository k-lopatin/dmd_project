import requests
import re
from Publication import Publication
import time


class BSCrawler:
    def __init__(self):
        self.base_href = "http://academic.research.microsoft.com/"

    def get_books_by_search(self, s):

        link = self.base_href + "Search?query=" + s.lower()

        response = requests.get(link)
        html = response.text
        # html = re.sub("\r", '', html)
        html = html.replace('\r\n', '')
        # print(html)

        search = re.findall('<li class="paper-item">(.*?)</li>', html)
        for s in search:
            self.get_book_from_block(s)

    def get_book_from_block(self, block):
        title = re.search('<h3>.*?<a.*?>(.*?)</a>', block)
        if title is not None:
            title = title.group(1)
        else:
            title = ""

        authors = re.findall('class="author-name-tooltip".*?>(.*?)</a>', block)
        for i, auth in enumerate(authors):
            authors[i] = re.sub('<.*?>', '', auth)

        year = re.search('class="conference">.*?<span.*? (\d{4}).*?</span>', block)
        if year is not None:
            year = year.group(1)
        else:
            year = ""

        link = re.search('<h3>.*?<a.*?href="(.*?)">', block)
        if link is not None:
            link = self.base_href + link.group(1)
        else:
            link = ""


        book = Publication(title, authors, year, link)

        desc = re.search('class="abstract">.*?<span.*?>(.*?)</span>.*?class="conference">.*?<span', block)
        if desc is not None:
            desc = desc.group(1)
            book.add_description(desc)

        publisher = re.search('class="conference">.*?</span><a.*?>(.*?)</a>', block)
        if publisher is not None:
            publisher = publisher.group(1)
            book.add_publisher(publisher)

        book.print_info()
