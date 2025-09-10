USE movies;

INSERT INTO movie_list(title,genre,release_year) VALUES ('The Matrix', 'Sci-Fi',1999),
('Gladiator', 'Action', 2000),
('Jurassic Park', 'Sci-Fi', 1993),
('The Fugitive', 'Action', 1993);


SELECT title FROM movie_list WHERE genre = 'Drama'
ORDER BY release_year ASC LIMIT 1;

SELECT title, release_year FROM movie_list WHERE genre = 'Action' AND release_year > 2000
ORDER BY release_year DESC
LIMIT 1;

SELECT * FROM movie_list WHERE genre IN ('Sci-Fi', 'Action') AND release_year IN (select release_year from movie_list where genre = "Drama");

select * from movie_list WHERE (genre = "Sci-Fi") AND release_year > (SELECT AVG(release_year) from movie_list WHERE genre = "Action");

select * from movie_list WHERE genre != "Action" AND release_year = ( SELECT min(release_year) from movie_list where genre = "Action")