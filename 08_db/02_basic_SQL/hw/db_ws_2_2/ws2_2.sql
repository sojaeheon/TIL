USE movies;

select * from movie_list WHERE release_year >= 2010;

select * from movie_list WHERE genre = "Action";

select * from movie_list WHERE title LIKE 'The%';

select * from movie_list WHERE release_year BETWEEN 2008 and 2014;

select * from movie_list WHERE release_year is NULL