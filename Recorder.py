import BSCrawler
import psycopg2 as db
import Publication

__author__ = 'serge'


c = db.connect(database="dmd_project", user="postgres", password="Sawyer8111998")
cu = c.cursor()
# return c

def connect():
    c = db.connect(database="dmd_project", user="postgres", password="Sawyer8111998")
    # cu = c.cursor()
    return c

def create_tables():
    try:
        cu.execute("""
        CREATE TABLE publisher (
        publisher_id SERIAL NOT NULL,
        name varchar(500) NOT NULL,
        publications_ids text
        );
    """)
        c.commit()

    except db.DatabaseError as x:
        print("Error", x)

    try:
        cu.execute("""
        CREATE TABLE keywords (
        keyword text PRIMARY KEY,
        publications_ids text
        );
    """)
        c.commit()

    except db.DatabaseError as x:
        print("Error", x)

    try:
        cu.execute("""
        CREATE TABLE author (
        author_id SERIAL PRIMARY KEY,
        name_author varchar(250),
        publications_ids text
        );
    """)
        c.commit()

    except db.DatabaseError as x:
        print("Error", x)

    try:
        cu.execute("""
        CREATE TABLE publication (
        publication_id SERIAL PRIMARY KEY,
        title varchar(500) NOT NULL,
        lang char(2),
        year_publication int,
        type_publication varchar(100) NOT NULL,
        url text NOT NULL,
        subject varchar(300),
        description text
        );
    """)
        c.commit()

    except db.DatabaseError as x:
        print("Error", x)

    try:
        cu.execute("""
        CREATE TABLE related (
        current_id int REFERENCES publication(publication_id),
        other_id int
        );
    """)
        c.commit()

    except db.DatabaseError as x:
        print("Error", x)

    c.commit()
    c.close()

def create_records(pub):
    c = connect()
    cu = c.cursor()
    cu.execute("SELECT publisher_id FROM publisher WHERE name = '" + pub.publisher + "'")
    pub_id_query = cu.fetchone()
    pub_id = 0
    if pub_id_query is not None:
        pub_id = pub_id_query[0]
    else:
        cu.execute("INSERT INTO publisher (name) VALUES ('" + pub.publisher + "') RETURNING publisher_id")
        pub_id_query = cu.fetchone()
        pub_id = pub_id_query[0]
    c.commit()

    cu.execute("INSERT INTO publication (title, lang, year_publication, type_publication, url, subject, description)"
               "VALUES ('" + pub.title + "', '" + pub.language + "', '" + pub.year + "', '" + "Science" + "', '" + pub.link + "', '" + "Subject" + "', '" + pub.description + "')")
    c.commit()

    cu.execute("SELECT author_id FROM author WHERE name_author = '" + pub.authors[0] + "'")
    author_id_query = cu.fetchone()
    author_id = 0
    if author_id_query is not None:
        author_id = author_id_query[0]
    else:
        cu.execute("INSERT INTO author (name_author) VALUES ('" + pub.authors[0] + "') RETURNING author_id")
        author_id_query = cu.fetchone()
        author_id = author_id_query[0]
    c.commit()

    c.close()

def delete_tables():
    try:
        cu.execute("""
        DROP TABLE IF EXISTS publisher CASCADE;
        DROP TABLE IF EXISTS author CASCADE;
        DROP TABLE IF EXISTS publication CASCADE;
        DROP TABLE IF EXISTS related CASCADE;
        DROP TABLE IF EXISTS keywords CASCADE;
    """)
        c.commit()

    except db.DatabaseError as x:
        print("Error", x)