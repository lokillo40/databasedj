Make sure you download the starter code and run the following:

```sh
  psql < movies.sql
  psql movies_db
```

In markdown, you can place a code block inside of three backticks (```) followed by the syntax highlighting you want, for example

\```sql

SELECT \* FROM users;

\```

Using the `movies_db` database, write the correct SQL queries for each of these tasks:

1.  The title of every movie.

\```sql

SELECT title FROM movies;

\```

2.  All information on the G-rated movies.

\```sql

SELECT * FROM movies WHERE rating='G';

\```

3.  The title and release year of every movie, ordered with the
    oldest movie first.

\```sql

SELECT title, release\_year FROM movies ORDER BY release\_year ASC;

\```
    
4.  All information on the 5 longest movies.

\```sql

SELECT * FROM movies ORDER BY runtime DESC LIMIT 5;

\```

5.  A query that returns the columns of `rating` and `total`, tabulating the
    total number of G, PG, PG-13, and R-rated movies.

\```sql

SELECT rating, COUNT(*) as total FROM movies WHERE rating IN ('G', 'PG', 'PG-13', 'R') GROUP BY rating;

\```


6.  A table with columns of `release_year` and `average_runtime`,
    tabulating the average runtime by year for every movie in the database. The data should be in reverse chronological order (i.e. the most recent year should be first).

\```sql

SELECT release\_year, AVG(runtime) as average\_runtime
FROM movies GROUP BY release\_year ORDER BY release\_year DESC;

\```

7.  The movie title and studio name for every movie in the
    database.

\```sql

SELECT movies.title, studios.name AS studio\_name FROM movies JOIN studios ON movies.studio\_id = studios.id
ORDER BY movies.title ASC;

\```

8.  The star first name, star last name, and movie title for every
    matching movie and star pair in the database.

\```sql

SELECT stars.first\_name, stars.last\_name, movies.title
FROM roles JOIN stars ON roles.star\_id = stars.id
JOIN movies ON roles.movie\_id = movies.id;

\```

9.  The first and last names of every star who has been in a G-rated movie. The first and last name should appear only once for each star, even if they are in several G-rated movies. *IMPORTANT NOTE*: it's possible that there can be two *different* actors with the same name, so make sure your solution accounts for that.

\```sql

SELECT stars.first\_name, stars.last\_name FROM stars JOIN roles ON stars.id = roles.star\_id JOIN movies ON roles.movie\_id = movies.id WHERE movies.rating = 'G'
GROUP BY stars.id, stars.first\_name, stars.last\_name;

\```

10. The first and last names of every star along with the number
    of movies they have been in, in descending order by the number of movies. (Similar to #9, make sure
    that two different actors with the same name are considered separately).

\```sql

SELECT stars.first\_name, stars.last\_name, COUNT(movies.id) AS num\_movies FROM stars JOIN roles ON stars.id = roles.star\_id
JOIN movies ON roles.movie\_id = movies.id
GROUP BY stars.id, stars.first\_name, stars.last\_name
ORDER BY num\_movies DESC;


\```

### The rest of these are bonuses

11. The title of every movie along with the number of stars in
    that movie, in descending order by the number of stars.

12. The first name, last name, and average runtime of the five
    stars whose movies have the longest average.

13. The first name, last name, and average runtime of the five
    stars whose movies have the longest average, among stars who have more than one movie in the database.

14. The titles of all movies that don't feature any stars in our
    database.

15. The first and last names of all stars that don't appear in any movies in our database.

16. The first names, last names, and titles corresponding to every
    role in the database, along with every movie title that doesn't have a star, and the first and last names of every star not in a movie.
