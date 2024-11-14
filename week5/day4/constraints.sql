DROP TABLE IF EXISTS students;

CREATE TABLE students(
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(50),
    student_email VARCHAR(255) UNIQUE

);

INSERT INTO students(student_name, student_email) VALUES('james', 'james@james.com');

DROP TABLE IF EXISTS movies;

CREATE TABLE movies(
    movie_id SERIAL PRIMARY KEY,
    movie_name VARCHAR(255) UNIQUE CHECK(movie_name ~ '^[A-Z][a-z]*$'), --UNIQUE CHECK ensures alpha chars are utilized by using regex
    age_limit INT CHECK (age_limit >= 0 AND age_limit <= 18) --(age_limit BETWEEN 0 AND 18) (age_limit IN (13, 15, 18))
);

INSERT INTO movies(movie_name, age_limit) VALUES('Python', 15);
INSERT INTO movies(movie_name, age_limit) VALUES('It', 18);

DROP TABLE IF EXISTS product;

CREATE TABLE product(
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) UNIQUE NOT NULL, --prvents empty values being inserted
    quantity INT CHECK(quantity >= 0)
);

--CHECKs can go at the bottom of the schema

