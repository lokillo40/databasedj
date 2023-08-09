### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

A relational database management system used to store and manage data in structured tables.

- What is the difference between SQL and PostgreSQL?

SQL is a standardized programming language used for managing and manipulating relational databases, while PostgreSQL is a specific relational database management system (RDBMS) that uses SQL to interact with data. In other words, SQL is the language you use to interact with systems like PostgreSQL

- In `psql`, how do you connect to a database?

psql my_database_name


- What is the difference between `HAVING` and `WHERE`?

The WHERE clause in SQL is used to filter records before grouping and aggregation, while the HAVING clause is used to filter results after grouping and aggregation. Essentially, WHERE is used before GROUP BY and HAVING is used after GROUP BY

- What is the difference between an `INNER` and `OUTER` join?

In SQL, an INNER JOIN returns only the rows where there is a match in both tables being joined, while an OUTER JOIN returns all the rows from one table and the matched rows from the second table. If there is no match, the result for the second table in the OUTER JOIN is NULL.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

In SQL, a LEFT OUTER JOIN returns all the rows from the left table, and the matched rows from the right table. If there is no match, the result for the right table is NULL.
Conversely, a RIGHT OUTER JOIN returns all the rows from the right table, and the matched rows from the left table. If there is no match, the result for the left table is NULL.

- What is an ORM? What do they do?

An ORM, or Object-Relational Mapping, is a programming technique that allows you to interact with your database, like you would with SQL. In other words, it's a way to create, retrieve, update, and delete from your database using an object-oriented paradigm in your preferred programming language, without needing to write SQL code. It essentially maps your database tables to classes or objects in your program, making data manipulation more intuitive and less error-prone.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

AJAX is based on JavaScript and is used in the browser, while requests is a Python library and is used in a Python environment. AJAX being client-side does not have direct access to the database, whereas server-side languages like Python do. You would typically not expose direct database operations to the client-side for security reasons.

- What is CSRF? What is the purpose of the CSRF token?

A CSRF token is a security measure used to prevent CSRF attacks. It's a unique, random value associated with a user's session and is typically embedded within a web form. When the form is submitted, the server checks the submitted token against the one stored in the user's session. If they match, the request is considered legitimate. If they don't match or if the token is missing, the request is rejected, preventing potential CSRF attacks.

- What is the purpose of `form.hidden_tag()`?

Generates hidden CSRF tokens in a form to validate form submissions and protect against Cross-Site Request Forgery (CSRF) attacks.

