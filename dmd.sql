CREATE TABLE publisher (
publisher_id serial NOT NULL,
name varchar(500) NOT NULL,
publications_ids text(50),
CONSTRAINT pub_id PRIMARY KEY (publisher_id)
);

CREATE TABLE author (
author_id int PRIMARY KEY,
name_author1 varchar(50),
name_author2 varchar(50),
name_author3 varchar(50),
publications_ids text(50)
);

CREATE TABLE publication (
publication_id int PRIMARY KEY,
title varchar(500) NOT NULL,
lang varchar(2),
year_publication int,
type_publication varchar(100),
url text NOT NULL,
subject varchar(300),
description text);

CREATE TABLE related (
current_id int,
other_id int
);

CREATE TABLE keywords (
keyword text PRIMARY KEY,
publications_ids text(50)
);
