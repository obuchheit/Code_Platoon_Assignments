import csv

students_table = 'students'
teachers_table = 'teachers'
subjects_table = 'subjects'

with open('./data/student.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        sql_insert = f"INSERT INTO {students_table} (id, first_name, last_name, age, subject) VALUES ({int(row['id'])}, '{row['first_name']}', '{row['last_name']}', {int(row['age'])}, {int(row['subject'])});"
        print(sql_insert)  

with open('./data/teachers.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        sql_insert = f"INSERT INTO {teachers_table} (id, first_name, last_name, age, subject) VALUES ({int(row['id'])}, '{row['first_name']}', '{row['last_name']}', {int(row['age'])}, {int(row['subject'])});"
        print(sql_insert)  

with open('./data/subjects.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        sql_insert = f"INSERT INTO {subjects_table} (id, subject) VALUES ({int(row['id'])}, '{row['subject']}');"
        print(sql_insert)  # Print or save the SQL statement