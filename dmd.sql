CREATE TABLE publisher (
publisher_id int PRIMARY KEY,
name varchar(500) NOT NULL);

CREATE TABLE author (
author_id int PRIMARY KEY,
name_author1 varchar(50),
name_author2 varchar(50),
name_author3 varchar(50)
);

CREATE TABLE publication (
publication_id int PRIMARY KEY,
tittle varchar(500) NOT NULL,
lang char(2), 
year_publication int,
type_publication varchar(100) NOT NULL,
url text NOT NULL,
subject varchar(300),
description text);

CREATE TABLE related (
current_id int,
other_id int
);

