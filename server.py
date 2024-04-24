from flask import Flask
from flask import render_template
from flask import Response, request

from data.learn import muscle_groups, exercises
from data.quiz import quizzes

app = Flask(__name__)

score = 0
quiz_index = 0
completed_dict = {group["name"]: False for group in muscle_groups}


def reset():
    global score, quiz_index, completed_dict
    score = 0
    quiz_index = 0
    completed_dict = {group["name"]: False for group in muscle_groups}


@app.route('/')
def home():
    reset()
    return render_template('home.html')


@app.route('/learn', methods=['GET'])
def learn():
    total = len(completed_dict)
    n_completed = sum(1 for value in completed_dict.values() if value)

    return render_template('learn.html', muscle_groups=muscle_groups, n_completed=n_completed, total=total)


@app.route('/learn/<muscle_group>/<index>', methods=['GET'])
def learn_exercise(muscle_group, index):
    index = int(index)
    total = len(exercises[muscle_group])
    exercise = exercises[muscle_group][index]

    return render_template('exercise.html', exercise=exercise, muscle_group=muscle_group, current_index=index, total=total)


@app.route('/complete', methods=['POST'])
def complete_section():
    section = request.form.get("section")
    completed_dict[section] = True

    return Response(status=204)


@app.route('/quiz', methods=['GET'])
def quiz():
    total = len(quizzes)
    if quiz_index >= total:
        return render_template('result.html', score=score)

    quiz = quizzes[quiz_index]
    return render_template('quiz.html', quiz=quiz, current_index=quiz_index, total=total)


@app.route('/submit', methods=['POST'])
def submit():
    global score, quiz_index
    
    quiz_index += 1

    scored = request.form.get("scored") == "true"
    if scored:
        score += 1

    return Response(status=204)


if __name__ == '__main__':
   app.run(debug = True)
