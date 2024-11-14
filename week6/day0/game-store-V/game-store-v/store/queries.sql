-- 1
SELECT engine_name FROM gaming_engine;

-- 2
SELECT SUM(quantity) FROM game;

-- 3
SELECT game_title FROM game WHERE price >= 30;

-- 4
SELECT game_title, quantity FROM game WHERE quantity < 20;

-- 5
SELECT COUNT(*) FROM genre_game;

--6
SELECT action_figure_title FROM action_figure WHERE price > 20 AND price <50;

--7
SELECT poster_title, price FROM poster WHERE quantity > 15 AND quantity < 30;

--8
SELECT employee_name, salary FROM employee WHERE salary > 40000;

--9
SELECT COUNT(*) FROM social_security;

--10
SELECT start_time, end_time FROM shifts;

--11 
SELECT e.employee_name, e.salary FROM employee e JOIN shifts s ON s.employee_id = e.id;

--12
SELECT * FROM action_figure WHERE quantity < 15;

--13
SELECT game_title FROM game WHERE game_title LIKE '%Warzone';

--14
SELECT COUNT(*) FROM genre;

--15
SELECT action_figure_title, quantity FROM action_figure WHERE price > 27;

--16
SELECT employee_name FROM employee WHERE position = 'IT Specialist';

--17
SELECT game_title FROM game WHERE quantity > 25;

--18
SELECT SUM(quantity) AS games FROM game;
SELECT SUM(quantity) AS action_figures FROM action_figure;
SELECT SUM(quantity) AS posters FROM poster;

SELECT SUM(g.quantity + a.quantity + p.quantity) / (100) AS total_inventory FROM game g, action_figure a, poster p;

--19
SELECT s.ssn, e.employee_name FROM employee e JOIN social_security s ON e.id = s.employee_id WHERE e.salary > 50000;

--20
SELECT poster_title, quantity FROM poster WHERE price > 10 AND price < 15;

--21
SELECT poster_title, quantity FROM poster WHERE price < 8;

--22
SELECT employee_name, salary FROM employee WHERE position IN ('Marketing Coordinator', 'Finance Analyst');

--23
SELECT SUM(quantity) AS action_figures FROM action_figure;

--24
SELECT game_title, quantity FROM game WHERE quantity > 15 AND quantity < 30;

--25
SELECT e.employee_name, e.salary FROM employee e JOIN shifts ON e.id = shifts.employee_id WHERE shifts.start_time > '2024-01-01';

--26
SELECT game_title, price FROM game WHERE price < 20;

--27
SELECT SUM(quantity) AS action_figures FROM action_figure WHERE price < 30 AND price > 25;

--28
SELECT e.employee_name, e.position FROM employee e JOIN shifts ON e.id = shifts.employee_id WHERE shifts.start_time < '2024-03-07 13:00:00';

--29
SELECT action_figure_title, quantity FROM action_figure WHERE quantity > 10;

--30
SELECT poster_title, quantity FROM poster WHERE quantity > 25;

--31
SELECT COUNT(*) FROM shifts;

--32 
SELECT e.employee_name, e.position FROM employee e JOIN shifts s ON e.id = s.employee_id WHERE s.start_time > '2024-02-02' AND s.start_time < '2024-03-07 13:00:00';

--33
SELECT game_title FROM game WHERE quantity < 20;

--34
SELECT action_figure_title, quantity FROM action_figure WHERE price > 23;

--35
SELECT SUM(quantity) AS posters FROM poster;
