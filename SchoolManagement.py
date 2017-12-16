
'''

MIS 407 Final Project: Course Management Assistance Product

Authors: Carlos Velasquez, David Boyd, Jack Roberts, Michaela Halbur
            Luke McDermott, Michael Siebert

'''
import os
from models import User, get_course_grade, get_student_course, get_todays_recent_posts, get_student_assignments
from flask import Flask, request, session, redirect, url_for, render_template, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

"""
Login page.
If username and password are valid then Session[username] is set to the entered username and they are taken to the user's dashboard.
"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not User.verify_exists(username, password):
            flash('Invalid login.')
            return render_template('index.html')
        else:
            session['username'] = username
            flash('Logged in.')
            posts = get_todays_recent_posts()
            assignments = get_student_assignments(session['username'])
            courses = get_student_course(session['username'])
            return render_template('dashboard.html', posts=posts, assignments=assignments, courses=courses)


"""
Clears all sessions and redirects back to login page
"""
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out.')
    return redirect(url_for('login'))


"""
Registers a user. This function will only be available to users with the type 'admin'.
"""
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if len(username) < 1:
            flash('Your username must be at least one character.')
        elif len(password) < 5:
            flash('Your password must be between at least 5 characters.')
        elif not User(username).register(password):
            flash('A user with that username already exists.')
        else:
            flash('Registered')
            return redirect(url_for('dashboard'))
    return render_template('register.html')


@app.route('/message_board', methods=['POST'])
def add_post():
    title = request.form['title']
    text = request.form['text']

    if not title:
        flash('You must give your post a title.')
    elif not text:
        flash('You must give your post a text body.')
    else:
        username = session['username']
        User(username,None,None,None,None,None).add_post(title, text)
    posts = get_todays_recent_posts()
    return render_template('dashboard.html', posts = posts)


@app.route('/grades', methods=['GET'])
def get_grades():
     grades = get_course_grade(session['username'])
     return render_template("grades.html", grades=grades)

@app.route('/courses', methods=['GET'])
def get_courses():
    courses = get_student_course(session['username'])
    return render_template("courses.html", courses=courses)


# run the Flask app (which will launch a local webserver)
if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(host="0.0.0.0", port=8080, debug=True)
