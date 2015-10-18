__author__ = 'lk1195'

class Publication:

    title = ""
    authors = ""
    year = ""
    link = ""
    description = ""
    language = ""
    publisher = ""
    rights = ""

    def __init__(self, title, authors, year, link):
        self.title = title
        self.authors = authors
        self.year = year
        self.link = link

    def add_description(self, description):
        self.description = description

    def add_publisher(self, publisher):
        self.publisher = publisher

    def rights(self, rights):
        self.rights = rights

    def print_info(self):
        print(self.title)
        for author in self.authors:
            # print(author)
            print(u'author')
        print(self.year)
        print(self.link)
        print(self.publisher)