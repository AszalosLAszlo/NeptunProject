Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
db = SQLAlchemy(app)

# Modellek definiálása
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)

# Útvonalak definiálása
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses')
def courses():
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    if request.method == 'POST':
        course_id = request.form['course']
        # Itt implementálhatja a beiratkozási logikát...
        return redirect(url_for('index'))
    courses = Course.query.all()
    return render_template('enroll.html', courses=courses)

if __name__ == '__main__':
    db.create_all()  # Adatbázis táblák létrehozása, ha még nem léteznek
    app.run(debug=True)
