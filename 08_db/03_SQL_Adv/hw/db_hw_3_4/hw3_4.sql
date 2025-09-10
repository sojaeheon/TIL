use library_db;

SELECT
  books.title as book_title,
  authors.name as book_author,
  genres.genre_name as book_genre
FROM books
INNER JOIN authors ON books.author_id = authors.id
INNER JOIN genres ON books.genre_id = genres.id;


CREATE INDEX idx_authors_name ON authors(name);

CREATE INDEX idx_genres_genre_name ON genres(genre_name);

SELECT 
    books.title AS book_title,
    authors.name AS author_name,
    genres.genre_name AS genre_name
FROM books
INNER JOIN authors ON books.author_id = authors.id
INNER JOIN genres ON books.genre_id = genres.id
WHERE authors.name = 'J.K. Rowling'
  AND genres.genre_name = 'Fantasy';