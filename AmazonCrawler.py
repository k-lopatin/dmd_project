import requests
import re
from Book import Book


class AmazonCrawler:
    base_href = "http://dblp.uni-trier.de/"
    base_xml_href = base_href + "rec/xml/"
    base_db_link = base_href + "db/"

    def __init__(self):
        self.response = requests.get('http://dblp.uni-trier.de/db/journals/corr/corr1501.html')

    def get_html(self):
        print self.response.text

    def get_titles(self):
        print self.response
        html = self.response.text
        search = re.findall('div class="data".+?class="title".+?>(.+?)</span>', html)
        if search:
            return search
        else:
            return None

    def get_titles(self):
        html = self.response.text
        search = re.findall('div class="data".+?class="title".+?>(.+?)</span>', html)
        if search:
            return search
        else:
            return None

    def get_book_xml_link(self):
        html = self.response.text
        search = re.findall('<li class="entry.*?<small>(.+?)</small>', html)
        count = 0
        for s in search:
            self.get_book_xml(s)
            if count > 10:
                break
            count += 1

    def get_book_xml(self, link):
        response = requests.get(self.base_xml_href + link + ".xml")
        self.book_from_xml(response.text)
        print
        print

    def book_from_xml(self, xml):
        authors = re.findall('<author>(.+?)</author>', xml)
        title = re.search('<title>(.+?)</title>', xml)
        if title != None:
            title = title.group(1)
        else:
            title = ""

        year = re.search('<year>(.+?)</year>', xml)
        if year != None:
            year = year.group(1)
        else:
            year = ""
        link = re.search('<ee>(.+?)</ee>', xml)
        if link != None:
            link = link.group(1)
        else:
            link=""
        book = Book(title, authors, year, link)
        book.print_info()
