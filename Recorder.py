import BSCrawler
import psycopg2 as db

__author__ = 'serge'

bsc = BSCrawler.BSCrawler()

# Connection conn = DriverManager.getConnection(5432, "postgres", "Sawyer8111998")
# Statement s = conn.createStatement();
# ResultSet r;

c = db.connect(database = "dmd_project",  user = "postgres", password = "Sawyer8111998")
cu = c.cursor()

def create_tables():
    try:
        cu.execute("""
        CREATE TABLE publisher (
        publisher_id int PRIMARY KEY,
        name varchar(500) NOT NULL,
        publications_ids text(50)
        );
    """)
    except db.DatabaseError as x:
        print("Error", x)

    try:
        cu.execute("""
        CREATE TABLE keywords (
        keyword text PRIMARY KEY,
        publications_ids text(50)
        );
    """)

    except db.DatabaseError as x:
        print("Error", x)

    try:
        cu.execute("""
        CREATE TABLE author (
        author_id int PRIMARY KEY,
        name_author1 varchar(50),
        name_author2 varchar(50),
        name_author3 varchar(50),
        publications_ids text(50)
        );
    """)
    except db.DatabaseError as x:
        print("Error", x)

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
        print("Error", x)

    try:
        cu.execute("""
        CREATE TABLE related (
        current_id int REFERENCES publication(publication_id),
        other_id int
        );
    """)

    except db.DatabaseError as x:
        print("Error", x)

    c.commit()
    c.close()

def create_records(pub):
    cu.executemany("""
    INSERT INTO publisher (name)
    VALUES (""" + pub.publisher + """);""")
    cu.executemany("""
    INSERT INTO publication (tittle, lang, year_publication, type_publication, url, subject, description)
    VALUES (""" + pub.title + """, """ + pub.language + """, null, """ + pub.link + """, null,""" +
                   pub.description + """);""")
    # cu.executemany("""
    # INSERT INTO related (current_id, other_id)
    # VALUES (Publication.publication_id,
    # """)
    c.commit()
    c.close()

