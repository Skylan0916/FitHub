from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

from data.learn import muscle_groups, exercises
from data.quiz import quizzes

app = Flask(__name__)

completed_dict = {group["name"]: False for group in muscle_groups}
current_quiz_index = 0


@app.route('/')
def home():
    return render_template('home.html') 


@app.route('/learn', methods=['GET', 'POST'])
def learn():
    completed_section = request.form.get("completed_section")
    if completed_section:
        completed_dict[completed_section] = True

    n_completed = sum(1 for value in completed_dict.values() if value)
    total = len(completed_dict)

    return render_template('learn.html', muscle_groups=muscle_groups, n_completed=n_completed, total=total)


@app.route('/learn/<muscle_group>/<index>')
def learn_exercise(muscle_group, index):
    index = int(index)
    total = len(exercises[muscle_group])
    exercise = exercises[muscle_group][index]

    return render_template('exercise.html', exercise=exercise, muscle_group=muscle_group, current_index=index, total=total)


@app.route('/quiz/<index>', methods=['GET', 'POST'])
def quiz(index):
    index = int(index)
    quiz = quizzes[index]
    total = len(quizzes)

    return render_template('quiz.html', quiz=quiz, current_index=index, total=total) 


if __name__ == '__main__':
   app.run(debug = True)
