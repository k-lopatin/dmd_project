__author__ = 'lk1195'

class Book:
    title = ""
    authors = ""
    year = ""
    link = ""

    def __init__(self, title, authors, year, link):
        self.title = title
        self.authors = authors
        self.year = year
        self.link = link

    def print_info(self):
        print self.title
        for author in self.authors:
            print author
        print self.year
        print self.link