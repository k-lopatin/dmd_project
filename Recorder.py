__author__ = 'serge'
import BSCrawler
import Publication

bsc = BSCrawler.BSCrawler()

import psycopg2 as db
c = db.connect(database="dmd_project")
cu = c.cursor()

def create_tables(self):
    try:
        cu.execute("""
        CREATE TABLE publisher (
        publisher_id int PRIMARY KEY,
        name varchar(500) NOT NULL
        );
    """)
    except db.DatabaseError as x:
        print ("Error", x)
        c.commit()

    try:
        cu.execute("""
        CREATE TABLE author (
        author_id int PRIMARY KEY,
        name_author1 varchar(50),
        name_author2 varchar(50),
        name_author3 varchar(50)
        );
    """)
    except db.DatabaseError as x:
        print ("Error", x)
        c.commit()

    try:
        cu.execute("""
        CREATE TABLE publication (
        publication_id int PRIMARY KEY,
        tittle varchar(500) NOT NULL,
        lang char(2),
        year_publication int,
        type_publication varchar(100) NOT NULL,
        url text NOT NULL,
        subject varchar(300),
        description text
        );
    """)
    except db.DatabaseError as x:
        print ("Error", x)
        c.commit()

    try:
        cu.execute("""
        CREATE TABLE related (
        current_id int REFERENCES publication(publication_id),
        other_id int
        );
    """)

    except db.DatabaseError as x:
        print ("Error", x)
        c.commit()

        c.close()

def create_records(Publication):
    c.commit()
    cu.executemany("""
    INSERT INTO publisher (name)
    VALUES (Publication.publisher);""")
    cu.executemany("""
    INSERT INTO publication (tittle, lang, year_publication, type_publication, url, subject, description)
    VALUES (Publication.title, Publication.language, null, Publication.link, null, Publisher.description);""")
    # cu.executemany("""
    # INSERT INTO related (current_id, other_id)
    # VALUES (Publication.publication_id,
    # """)

    c.commit()

