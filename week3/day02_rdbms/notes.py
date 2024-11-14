'''
char vs varchar:
varchar uses less memory


file.sql will allow you to run sql queries.
DROP TABLE if lll

CREATE TABLE db_name(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    grade CHAR(1)
    );

#\COPY <db_name> FROM './csv_file.csv' DELIMETER ',' CSV_HEADER;
INSERT INT <db_name>(first_name, last_name, age, grade) VALUES

SELECT * FROM db_name;
SELECT *FROM 
    
Go into terminal

$ psql opens psql terminal
$ \l lists all databases
$ CREATE DATABADE <name> creates a database
$ \c <database_name> connects to a database
$ CREATE TABLE 
$ \d


$ select * from student_id_seq ;

'''