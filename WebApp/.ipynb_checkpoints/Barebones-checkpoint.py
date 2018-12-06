"""" This file contains the functions that the web app will use to display
information to the user and to calculate similarity to representative votes.
"""

from urllib.request import urlopen
import json
from pprint import pprint
reps=[]
ID=0
session=0

class bill(object):
    def __init__(self, name, ID, congressnum=0):
        self.name=name
        self.ID=ID
        self.congressnum = congressnum
        self.rep_vote='Yes'
        self.user_vote=0
        self.user_preference=1 #scale
    def does_agree(self):
        if self.user_vote==self.rep_vote:
            return 1
        else:
            return 0

comparing_votes=[bill("Billington", ID, session), bill("Billsby", ID, session), bill("Billard", ID, session)] #import bills list from bills.py


def get_json(url):
    """Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urlopen(url)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    return response_data

def get_rep(zipcode):
    """Given a zipcode, can look up the user's representatives using an API
    """
    url= "https://www.googleapis.com/civicinfo/v2/representatives?filter[role][legislatorUpperBody]&address="+zipcode+"&key=AIzaSyB9AuQfeJ2TRNSfE8GEHyBfwpgKaISJ7WI"
    data=get_json(url)
    i=2 #skip prez and vice-prez
    while i < 4:
        repyboi=rep(data["officials"][i]['name'])
        reps.append(repyboi)
        i+=1
    return reps

def compare_opinions():
    """Generates results based on comparing the opinions with weight to user priorities
    """
    passion=0
    similarity=0
    for bill in comparing_votes:
        passion+=bill.user_preference #get the total perference votes to guage relative preference
    for bill in comparing_votes:
        similarity+=bill.does_agree()*(bill.user_preference/passion) #multiply relative preference by binary of agreement
    return "Similarity score of "+str(similarity*100)[:5]+"%" #turns score into percentage with 2 past decimal

def give_me_things():
    """Turns info into format for HTML"""
    #descriptions=bills.get_descriptions()
    #i=0
    #while i< len(comparing_votes):
        #description.append(comparing_votes[i].name+': '+comparing_votes[i].description)
        #i+=1
    #return descriptions
    return ['bill 1', 'bill 2', 'bill 3']

"""USER INPUT"""

def get_user_answers(answers):
    i=0
    while i< len(comparing_votes):
        comparing_votes[i].user_vote=answers[i]
        i+=1

def get_rep_answers():
    """Turns info into format for HTML"""
    #answers=bills.getreppy()
    #i=0
    #while i< len(comparing_votes):
        #answers.append(i.rep_vote)
        #i+=1
    #return answers
    return ['Yes', 'Yes', 'Yes']



""" This is Main Page Code"""
from flask import Flask
app = Flask(__name__)

from flask import render_template
from flask import redirect, url_for, request

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
    Votes= give_me_things()
    answers=[]
    i = 1
    #while i < len(Votes):
        #answers+= request.form['Q'+ str(i)]
    answers.append(request.form['Q1'])
    answers.append(request.form['Q2'])
    answers.append(request.form['Q3'])
    #get_user_answers(answers)
    rep_answers = ['Yes', 'Yes', 'No']
    Score= compare_opinions()

    return render_template('Results2.html', Score=Score, UserScore1=answers[0], RepScore1=rep_answers[0], UserScore2=answers[1], RepScore2= rep_answers[1], UserScore3=answers[2],RepScore3=rep_answers[2], Vote1=Votes[0], Vote2=Votes[1], Vote3=Votes[2])
    #return "Success"

if __name__ == '__main__':
    app.run()
