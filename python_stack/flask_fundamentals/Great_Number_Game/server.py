from flask import Flask, render_template, request, redirect, session, flash
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def randomGenerate():
    session['num'] = random.randrange(0, 101)

@app.route('/')
def index():
    try:
        session['num']
    except KeyError:
        randomGenerate()
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def checkNum():
    guessed = request.form['num_guess']
    right = None
    wrong = None
    if int(guessed) > session['num']:
        flash('Number is too high!', 'toohigh')
    elif int(guessed) < session['num']:
        flash('Number is too low!', 'toolow')
    elif int(guessed) == session['num']:
        flash('Just right!', 'right')
    else:
        flash('try again!', 'wrong')
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    randomGenerate()
    return redirect('/')

app.run(debug=True)