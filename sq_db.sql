DROP TABLE mainmenu;

CREATE TABLE mainmenu(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    url TEXT NOT NULL
);

INSERT INTO mainmenu (name, url)
VALUES ('Добавить статью', 'add_article');

CREATE TABLE IF NOT EXISTS posts (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
text text NOT NULL,
time integer NOT NULL
);