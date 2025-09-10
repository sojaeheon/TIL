USE movies;

select * from movie_list;

select * from movie_list where release_year BETWEEN 2000 and 2010;

select * from movie_list where LEFT(title, 1) BETWEEN 'A' AND 'M';

SELECT * FROM movie_list WHERE genre = 'Drama'
  AND release_year BETWEEN 1990 AND 2000;

SELECT * from movie_list WHERE (release_year BETWEEN 2015 and 2020) AND (genre ="Sci-Fi" OR genre = "Action");

SELECT * FROM movie_list WHERE release_year > 2005 AND release_year < 2015;