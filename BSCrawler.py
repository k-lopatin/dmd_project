import requests
import re
from Publication import Publication
import time


class DBLPCrawler:
    def __init__(self):
        self.base_href = "http://dblp.uni-trier.de/"
        self.base_xml_href = self.base_href + "rec/xml/"
        self.base_db_link = self.base_href + "db/"

    def get_books_by_link(self, link):
        print(link)
        response = requests.get(link)
        html = response.text
        search = re.findall('<li class="entry.*?<small>(.+?)</small>', html)
        count = 0
        count2 = 1
        for s in search:
            self.get_book_xml(s)
            print(count2)
            count2 += 1

            if count > 10:
                time.sleep(5)
                count = 0

            count += 1
            time.sleep(5)

    def get_book_xml(self, link):
        response = requests.get(self.base_xml_href + link + ".xml")
        book_from_xml(response.text)
        print()
        print()

    def get_books_by_search(self, search_str):
        link = self.base_href + "search?q=" + search_str.lower()
        self.get_books_by_link(link)


def book_from_xml(xml):
    authors = re.findall('<author>(.+?)</author>', xml)
    title = re.search('<title>(.+?)</title>', xml)

    # title
    if title is not None:
        title = title.group(1)
    else:
        title = ""

    # year
    year = re.search('<year>(.+?)</year>', xml)
    if year is not None:
        year = year.group(1)
    else:
        year = ""

    # link
    link = re.search('<ee>(.+?)</ee>', xml)
    if link is not None:
        link = link.group(1)
    else:
        link = ""

    book = Publication(title, authors, year, link)

    # contributor. It can be not existing
    contributor = re.search('<journal>(.+?)</journal', xml)
    if contributor is not None:
        contributor = contributor.group(1)
        book.add_contributor(contributor)

    book.print_info()
