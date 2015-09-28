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
        name_author1 varchar(50),
        name_author2 varchar(50),
        name_author3 varchar(50),
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
        tittle varchar(500) NOT NULL,
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
    cu.execute("INSERT INTO publisher (name) VALUES ('" + pub.publisher + "') RETURNING publisher_id")
    # cu.execute("INSERT INTO publisher (name) SELECT '" + pub.publisher + "'"
    #             "WHERE NOT EXISTS (SELECT 1 FROM publisher WHERE publisher.name = '" + pub.publisher + "') LIMIT 1;")
    # cu.execute("CREATE OR REPLACE FUNCTION «public».«get_server» (varchar, integer) RETURNS integer AS"
    #            "newId int"
    #            "BEGIN;"
    #            "SELECT publisher_id FROM publisher "
    #            "WHERE publisher.name = $1"
    #
    #            )
    # currentID = cu.execute("SELECT publisher_id FROM publisher WHERE publisher.name = '" + pub.publisher + "'")
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