""" This file is the web app. Right now it is a hard coded version. 
This will eventually reference the functions in order to display user information. 
This uses HTML files Results1, ZIPquestionaire1, and zipcode1 as the pages of the webapp. 
Results1.html displays your vote on an issue, the reps vote on the issue, and your similarity score. 
ZIPquestionaire1.html displays the form that has bills(1 question rn) that the user "votes" on. 
zipcode1.html lets the user input their zip code in order to find their rep. 
"""
from flask import Flask
app = Flask(__name__)

from flask import render_template
from flask import redirect, url_for, request
ZIP=0
@app.route('/')
def zipentry():
    return render_template('zipcode3.html')
    
@app.route('/ZIP', methods =['POST', 'GET'])
def ZIP():
    global ZIP
    ZIP = request.form['ZIP']
    return redirect(url_for('questions'))

@app.route('/questions', methods = ['POST'])
def questions():
    return render_template('ZIPquestionaire1.html')

#@app.route('/questions1', methods = ['POST', 'GET'])    
#def questions1():
       # Q1 = request.form['Q1']
        #return redirect(url_for('results', Q1=Q1))
    
@app.route('/results', methods = ['POST', 'GET'])
def results():
    Q1 = request.form['Q1']
    score = "input variable here"
    return render_template('Results1.html', Score=score, UserScore=Q1, RepScore="yes")

if __name__ == '__main__':
    app.run()
