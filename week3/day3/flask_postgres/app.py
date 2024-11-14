from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask("server")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://owen:RadioRecon@localhost/owens_school'

db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key= True) 
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))


@app.route("/", methods=['GET'])
def home():
    message = "Welcome!"
    return render_template('index.html', message=message)

@app.route("/students/", methods=['GET'])
def students():
    students = [{
        'id': stud.id,
        'first_name': stud.first_name,
        'last_name': stud.last_name,
        'age': stud.age,
        'grade': stud.grade
    } for stud in Students.query.all()]
    return jsonify(students)

'''Returns Students over the age of 20'''
@app.route("/old_students/", methods=['GET'])
def old_students():
    old_studs = []
    for stud in Students.query.all():
        if stud.age>20:
            old_studs.append({
                'id': stud.id,
                'first_name': stud.first_name,
                'last_name': stud.last_name,
                'age': stud.age,
                'grade': stud.grade
            })
    return jsonify(old_studs)

'''Returns students with an age under 21'''
@app.route("/young_students/", methods=['GET'])
def young_students():
    young_students = []
    for stud in Students.query.all():
        if stud.age < 21:
            young_students.append({
                'id': stud.id,
                'first_name': stud.first_name,
                'last_name': stud.last_name,
                'age': stud.age,
                'grade': stud.grade})
    return jsonify(young_students)

'''Returns students with an grade of A and an age under 21'''
@app.route("/advance_students/", methods=['GET'])
def advance_students():
    advance_students = []
    for stud in Students.query.all():
        if stud.age < 21 and stud.grade == 'A':
            advance_students.append({
                'id': stud.id,
                'first_name': stud.first_name,
                'last_name': stud.last_name,
                'age': stud.age,
                'grade': stud.grade})
    return advance_students

'''Returns all Student names'''
@app.route("/student_names/", methods=['GET'])
def student_names():
    student_names = []
    for stud in Students.query.all():
        student_names.append({'first_name': stud.first_name, 'last_name': stud.last_name})
    return jsonify(student_names)

'''Returns all student names and ages'''
@app.route("/student_ages/", methods=['GET'])
def student_ages():
    student_ages = []
    for stud in Students.query.all():
        student_ages.append({"student_name": f'{stud.first_name} {stud.last_name}', 'age': stud.age})
    return jsonify(student_ages)

app.run(debug=True, port=8000)

