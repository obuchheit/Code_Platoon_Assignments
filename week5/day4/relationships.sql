--one to one 

DROP TABLE IF EXISTS employees CASCADE; --CASCADE allows for droping dependant tables

CREATE TABLE employees(
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL
)

DROP TABLE IF EXISTS social_securities;

CREATE TABLE social_securities(
    ssn_id SERIAL PRIMARY KEY,
    employee_id INT UNIQUE, --makes the employee only able to have 1 ssn
    ssn VARCHAR(11) UNIQUE NOT NULL, 
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

INSERT INTO employees(employee_name) VALUES('owen');
INSERT INTO social_securities(employee_id, ssn) VALUES(1, '222-54-5678')



--many to one

DROP TABLE IF EXISTS university CASCADE;

CREATE TABLE university(
    university_id SERIAL PRIMARY KEY,
    university_name VARCHAR(50) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS students;

CREATE TABLE students(
    stud_id SERIAL PRIMARY KEY,
    stud_name VARCHAR(50) NOT NULL,
    university_id INT,
    FOREIGN KEY (university_id) REFERENCES university(university_id)
);

INSERT INTO university(university_name) VALUES('Code-Platoon');
INSERT INTO students(stud_name, university_id) VALUES('Sam', 1);
INSERT INTO students(stud_name, university_id) VALUES('Owen', 1);
INSERT INTO students(stud_name, university_id) VALUES('James', 1);
INSERT INTO students(stud_name, university_id) VALUES('Jacob', 1);

--many-to-many

DROP TABLE IF EXISTS university CASCADE;



DROP TABLE IF EXISTS students CASCADE;

CREATE TABLE students(
    stud_id SERIAL PRIMARY KEY,
    stud_name VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS courses CASCADE;

CREATE TABLE courses(
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS course_studs;

CREATE TABLE course_studs(
    course_studs_id SERIAL PRIMARY KEY,
    stud_id INT,
    course_id INT,
    FOREIGN KEY(stud_id) REFERENCES students(stud_id),
    FOREIGN KEY(course_id) REFERENCES courses(course_id)
);

INSERT INTO students(stud_name) VALUES('Tristan');
INSERT INTO students(stud_name) VALUES('Owen');
INSERT INTO students(stud_name) VALUES('Gary');
INSERT INTO students(stud_name) VALUES('Ryan');
INSERT INTO students(stud_name) VALUES('Jake');

INSERT INTO courses(course_name) VALUES('Python');
INSERT INTO courses(course_name) VALUES('Javascript');

INSERT INTO course_studs(stud_id, course_id) VALUES(1, 2);
INSERT INTO course_studs(stud_id, course_id) VALUES(2, 2);
INSERT INTO course_studs(stud_id, course_id) VALUES(2, 1);
INSERT INTO course_studs(stud_id, course_id) VALUES(3, 2);
INSERT INTO course_studs(stud_id, course_id) VALUES(4, 1);
INSERT INTO course_studs(stud_id, course_id) VALUES(5, 1);
INSERT INTO course_studs(stud_id, course_id) VALUES(5, 2);




