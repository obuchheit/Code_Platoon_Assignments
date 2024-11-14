
DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(255) CHECK (employee_name ~ '^[a-zA-Z\s]+$') NOT NULL,
    position VARCHAR(255) CHECK (position IN ('Sales Associate', 'Store Manager', 'Inventory Clerk', 'Customer Service Representative', 'IT Specialist', 'Marketing Coordinator', 'Assistant Manager', 'Finance Analyst', 'Security Officer', 'HR Coordinator')),
    salary DECIMAL(8, 2)
);

\COPY employees FROM './data/employees.csv' WITH CSV HEADER;
SELECT setval('employees_employee_id_seq', (SELECT MAX(employee_id) FROM employees));

DROP TABLE IF EXISTS action_figures;

CREATE TABLE action_figures (
    action_figure_id SERIAL PRIMARY KEY,
    action_figure_title VARCHAR(255) UNIQUE CHECK (action_figure_title ~ "^[a-zA-Z0-9-]+$") NOT NULL,
    quantity INT CHECK (quantity >= 1 AND quantity <= 30),
    price DECIMAL(5, 2) CHECK (price >= 10.00 AND price <= 100.00)
);

\COPY action_figures FROM './data/action_figure.csv' WITH CSV HEADER;
SELECT setval('action_figures_action_figure_id_seq', (SELECT MAX(action_figure_id) FROM action_figures));

DROP TABLE IF EXISTS posters;

CREATE TABLE posters (
    poster_id SERIAL PRIMARY KEY,
    poster_title VARCHAR(255) CHECK (poster_title ~ '^[a-zA-Z\s]+$') NOT NULL,
    quantity INT CHECK (quantity >= 1 AND quantity <= 30),
    price DECIMAL(5, 2)
);

\COPY posters FROM './data/poster.csv' WITH CSV HEADER;
SELECT setval('posters_poster_id_seq', (SELECT MAX(poster_id) FROM posters));