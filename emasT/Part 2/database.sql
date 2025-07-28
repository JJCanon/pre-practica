CREATE TABLE items(
    id integer PRIMARY KEY AUTOINCREMENT,
    type_of text,
    title text,
    autor text,
    pages integer
    lent integer DEFAULT 0
);

CREATE TABLE loans(
    id integer PRIMARY KEY AUTOINCREMENT,
    item_id integer,
    lend_date text,
    get_back_date text,
    FOREIGN KEY(item_id) REFERENCES items(id)
);