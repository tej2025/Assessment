create database SQLAssessment;
use SQLAssessment;

create table users(
user_id int primary key,
name varchar(20),
country varchar(15));

INSERT INTO users (user_id, name, country) VALUES
(1, 'Amit', 'India'),
(2, 'Sara', 'USA'),
(3, 'John', 'UK'),
(4, 'Priya', 'India'),
(5, 'Ali', 'UAE'),
(6, 'Emma', 'Canada'),
(7, 'Rahul', 'India'),
(8, 'Lucas', 'Brazil'),
(9, 'Noah', 'USA'),
(10, 'Mia', 'Australia');

create table movies(
movie_id int primary key,
title varchar(20),
genre varchar(25),
release_year year);

INSERT INTO movies (movie_id, title, genre, release_year) VALUES
(101, 'Inception', 'Sci-Fi', 2010),
(102, 'Avatar 2', 'Sci-Fi', 2022),
(103, 'KGF', 'Action', 2021),
(104, 'Titanic', 'Romance', 1997),
(105, 'Avengers', 'Action', 2019),
(106, 'Interstellar', 'Sci-Fi', 2014),
(107, 'Dangal', 'Drama', 2016),
(108, 'RRR', 'Action', 2022),
(109, 'Notebook', 'Romance', 2021),
(110, 'Future War', 'Sci-Fi', 2023);

create table ratings(
user_id int ,
movie_id int,
rating tinyint,
rating_date date);

INSERT INTO ratings (user_id, movie_id, rating, rating_date) VALUES
(1, 101, 5, '2023-01-10'),
(1, 102, 4, '2023-01-12'),
(1, 103, 5, '2023-01-15'),
(2, 101, 4, '2023-02-10'),
(2, 105, 5, '2023-02-12'),
(3, 106, 5, '2023-03-01'),
(3, 102, 5, '2023-03-05'),
(4, 107, 4, '2023-01-20'),
(5, 108, 5, '2023-02-18'),
(6, 109, 3, '2023-03-12'),
(7, 103, 5, '2023-04-01'),
(8, 101, 4, '2023-04-10'),
(9, 102, 5, '2023-05-02'),
(10, 110, 5, '2023-06-01');

create table watch_history(
user_id int,
movie_id int,
watch_date date);

INSERT INTO watch_history (user_id, movie_id, watch_date) VALUES
(1, 101, '2023-01-01'),
(1, 103, '2023-01-05'),
(1, 103, '2023-01-20'),
(2, 101, '2023-02-01'),
(2, 105, '2023-02-05'),
(3, 106, '2023-03-01'),
(4, 107, '2023-01-15'),
(5, 108, '2023-02-10'),
(6, 109, '2023-03-10'),
(7, 103, '2023-04-01'),
(8, 101, '2023-04-05'),
(9, 102, '2023-05-01');

#---Q1---
SELECT country, genre, COUNT(*) AS watch_count
FROM users u
JOIN watch_history w ON u.user_id = w.user_id
JOIN movies m ON w.movie_id = m.movie_id
GROUP BY country, genre
ORDER BY watch_count asc;

#---Q2---
SELECT user_id, COUNT(*) AS total_ratings
FROM ratings
GROUP BY user_id
HAVING COUNT(*) > 20;

#---Q3---
SELECT m.title
FROM movies m
LEFT JOIN watch_history w ON m.movie_id = w.movie_id
WHERE m.release_year > 2020
AND w.movie_id IS NULL;

#---Q4---
SELECT genre, AVG(rating) AS avg_rating
FROM movies m
JOIN ratings r ON m.movie_id = r.movie_id
GROUP BY genre;

#---Q5---
SELECT r.user_id, m.genre
FROM ratings r
JOIN movies m ON r.movie_id = m.movie_id
GROUP BY r.user_id, m.genre
HAVING MIN(r.rating) = 5;

#---Q6---
SELECT m.title
FROM movies m
JOIN watch_history w ON m.movie_id = w.movie_id
JOIN users u ON w.user_id = u.user_id
GROUP BY m.movie_id
HAVING COUNT(DISTINCT u.country) >= 5;

#---Q7---
SELECT user_id,
       COUNT(movie_id) / COUNT(DISTINCT MONTH(watch_date)) AS avg_movies_per_month
FROM watch_history
GROUP BY user_id;

#---Q8---
SELECT user_id, movie_id, COUNT(*) AS watch_times
FROM watch_history
GROUP BY user_id, movie_id
HAVING COUNT(*) > 1;

#---Q9---
SELECT DISTINCT m.title
FROM movies m
JOIN ratings r ON m.movie_id = r.movie_id
LEFT JOIN watch_history w ON m.movie_id = w.movie_id
WHERE w.movie_id IS NULL;

#---Q10---
SELECT genre, AVG(five_star_count) AS avg_five_star
FROM (
    SELECT m.genre, COUNT(*) AS five_star_count
    FROM ratings r
    JOIN movies m ON r.movie_id = m.movie_id
    WHERE r.rating = 5
    GROUP BY m.genre
) t
GROUP BY genre
ORDER BY avg_five_star DESC
LIMIT 1;