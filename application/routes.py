from application import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/courses')
def courses():
    courseData = [
    {"id": 1, "title": "Introduction to Python", "description": "Learn the basics of Python programming.", "credits": 3, "term": "Fall 2024"},
    {"id": 2, "title": "Data Structures", "description": "Understand data structures and their applications.", "credits": 4, "term": "Spring 2024"},
    {"id": 3, "title": "Web Development", "description": "Learn how to build web applications using Flask.", "credits": 3, "term": "Fall 2024"},
    {"id": 4, "title": "Machine Learning", "description": "Introduction to machine learning concepts.", "credits": 4, "term": "Spring 2024"},
    {"id": 5, "title": "Database Systems", "description": "Learn about relational databases and SQL.", "credits": 3, "term": "Fall 2024"},
    {"id": 6, "title": "Operating Systems", "description": "Study the design and implementation of operating systems.", "credits": 4, "term": "Spring 2024"}
]
    print(courseData)
    return render_template('courses.html', courseData=courseData)
 
@app.route('/register')
def register():
    return render_template('register.html')

