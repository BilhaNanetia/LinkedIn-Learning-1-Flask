from application import app
from flask import render_template, request

courseData = [
    {"id": 1, "title": "Introduction to Python", "description": "Learn the basics of Python programming.", "credits": 3, "term": "Fall 2024"},
    {"id": 2, "title": "Data Structures", "description": "Understand data structures and their applications.", "credits": 4, "term": "Spring 2024"},
    {"id": 3, "title": "Web Development", "description": "Learn how to build web applications using Flask.", "credits": 3, "term": "Fall 2024"},
    {"id": 4, "title": "Machine Learning", "description": "Introduction to machine learning concepts.", "credits": 4, "term": "Spring 2024"},
    {"id": 5, "title": "Database Systems", "description": "Learn about relational databases and SQL.", "credits": 3, "term": "Fall 2024"},
    {"id": 6, "title": "Operating Systems", "description": "Study the design and implementation of operating systems.", "credits": 4, "term": "Spring 2024"}
]

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', index=True)

@app.route('/login')
def login():
    return render_template('login.html', login=True)

@app.route('/courses/')
@app.route('/courses/<term>')
def courses(term="Spring 2019"):
    return render_template('courses.html', courseData=courseData, courses=True, term=term)
 
@app.route('/register')
def register():
    return render_template('register.html', register=True)

@app.route('/enrollment', methods=['GET','POST'])
def enrollment():
    id = request.form.get('courseID')
    title = request.form['title']
    term = request.form.get('term')
    return render_template('enrollment.html', enrollment=True, data={"id": id, "title": title, "term": term})



