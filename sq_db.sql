DROP TABLE meinmenu;

CREATE TABLE mainmenu(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    url TEXT NOT NULL
);

INSERT INTO meinmenu (name, url)
VALUES ('Добавить статью', 'add_article');