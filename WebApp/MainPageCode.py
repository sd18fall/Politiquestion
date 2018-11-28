from flask import Flask
app = Flask(__name__)

from flask import render_template
from flask import redirect, url_for, request

#import Barebones
#from Barebones import get_rep, compare_opinions, give_me_things


ZIPcode=0

@app.route('/')
def zipentry():
    return render_template('zipcode3.html')

@app.route('/ZIP', methods =['POST', 'GET'])
def ZIP():
    Zip = request.form['ZIP']
    global ZIPcode
    ZIPcode = Zip
    get_rep(ZIPcode)
    return redirect(url_for('questions'))

@app.route('/questions', methods = ['POST'])
def questions():
    Votes= give_me_things()
    return render_template('ZIPquestionaire2.html', Vote1=Votes[0], Vote2=Votes[1], Vote3=Votes[2])

@app.route('/results', methods = ['POST'])
def results():
#    Votes= give_me_things()
    answers=[]
    i = 1
    #while i < len(Votes):
        #answers+= request.form['Q'+ str(i)]
    answers+= request.form['Q1']
    answers+= request.form['Q2']
    answers+= request.form['Q3']
    #get_user_answers(answers)
    rep_answers = ['Yes', 'Yes', 'No']
    Score= "66%"

    return render_template('Results2.html', Score=Score, UserScore1=answers[0], RepScore1=rep_answers[0], UserScore2=answers[1], RepScore2= rep_answers[1], UserScore3=answers[2],RepScore3=rep_answers[2], Vote1=Votes[0], Vote2=Votes[1], Vote3=Votes[2])

if __name__ == '__main__':
    app.run()
