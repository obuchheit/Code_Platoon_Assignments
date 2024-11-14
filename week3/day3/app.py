from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy



app = Flask("server") #creates an instance of the class Flask

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://owen:RadioRecon@localhost/school'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key= True) # id SERIAL PRIMARY KEY
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))


@app.route("/students/", methods=['GET'])
def student():
    print(Student.query.all()) # select * from student;
    students = [{
        'id': stud.id,
        'first_name': stud.first_name,
        'last_name': stud.last_name,
        'age': stud.age,
        'grade': stud.grade
    } for stud in Student.query.all()]
    return jsonify(students)


@app.route("/", methods=['GET']) #CRUD methods
def home():
    return "<h1>Hello Owen</h1>"

app.run(debug=True, port=8000) #method that belongs to the Flask class that takes 2 arguments: dubug and the port
