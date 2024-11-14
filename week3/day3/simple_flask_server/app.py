from flask import Flask, jsonify

app = Flask('server')


students = [
        {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
        {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
        {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
        {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
        {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
        {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
        {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
        {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
        {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
        {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
    ]

'''Returns students with an age over 20'''
@app.route("/old_students/", methods=['GET'])
def old_students():
    old_students = []
    for dict in students:
        if dict['age'] > 20:
            old_students.append(dict)
    return jsonify(old_students)

'''Returns students with an age under 21'''
@app.route("/young_students/", methods=['GET'])
def young_students():
    young_students = []
    for obj in students:
        if obj['age'] < 21:
            young_students.append(obj)
    return jsonify(young_students)

'''Returns students with an grade of A and an age under 21'''
@app.route("/advance_students/", methods=['GET'])
def advance_students():
    advance_students = []
    for obj in students:
        if obj['age'] < 21 and obj['grade'] == 'A':
            advance_students.append(obj)
    return advance_students

'''Returns all Student names'''
@app.route("/student_names/", methods=['GET'])
def student_names():
    student_names = []
    for obj in students:
        student_names.append({'first_name': obj['first_name'], 'last_name': obj['last_name']})
    return jsonify(student_names)

'''Returns all student names and ages'''
@app.route("/student_ages/", methods=['GET'])
def student_ages():
    student_ages = []
    for obj in students:
        student_ages.append({"student_name": (obj['first_name'], obj['last_name']), 'age': obj['age']})
    return jsonify(student_ages)

'''Returns all student dictionaries'''
@app.route("/students/", methods=["GET"])
def student():
    return students


app.run(debug=True, port=8000)
