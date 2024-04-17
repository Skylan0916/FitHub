from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

app = Flask(__name__)


# ROUTES
@app.route('/')
def home():
    return render_template('home.html') 


@app.route('/learn')
def learn():
    title = "Workout Exercises"
    data = None
    return render_template('learn.html', title=title, data=data)


@app.route('/learn/<muscle_group>')
def learn_exercise(muscle_group):
    title = "{} Exercises".format(muscle_group)
    data = None
    return render_template('learn.html', title=title, data=data) 


@app.route('/quiz')
def quiz():
    data = None
    return render_template('quiz.html', data=data) 


# AJAX FUNCTIONS



if __name__ == '__main__':
   app.run(debug = True)
