"""" This file contains the functions that the web app will use to display
information to the user and to calculate similarity to representative votes.
"""
import requests
import bills
from urllib.request import urlopen
import json
from pprint import pprint
from bills import Bill
reps=[]
webpages=[]

"""Essential Info for API Bill Lookup"""
comparing_votes=[
Bill('Child Interstate Abortion Notification Act', 'https://www.congress.gov/bill/109th-congress/senate-bill/403?q=%7B', 's403', '109', '2', '216', "This bill is about stuff", ),
Bill('North American Energy Security and Infrastructure Act of 2016', 'https://www.congress.gov/bill/114th-congress/senate-bill/2012?q=%7B', 's2012', '114', '2', '54', "This bill is about stuff"),
Bill('Defense of Marriage Act', 'https://www.congress.gov/bill/104th-congress/house-bill/3396', 'hr3396', '104', '2', '280', "This bill is about stuff"),
Bill('Patient Protection and Affordable Care Act', 'https://www.congress.gov/bill/111th-congress/house-bill/3590?q=%7B%22search%22%3A%5B', 'hr3590', '111', '1', '396', "This bill is about stuff"),
Bill('Support for Patients and Communities Act', 'https://www.congress.gov/bill/115th-congress/house-bill/6?q=%7B', 'hr6', '115', '2', '210', "This bill is about stuff"),
Bill('Tax Cuts and Jobs Act', 'https://www.congress.gov/bill/115th-congress/house-bill/1?q=%7B', 'hr1', '115', '1', '323', "This bill is about stuff")]
#Bill('Economic Growth, Regulatory Relief, and Consumer Protection Act', 's2155', '115', '2',),
#Bill('Countering America's Adversaries Through Sanctions Act', 'hr3364', '115', '1', '175')

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
    i=2
    while i <4: #positions 2-4 are the senators
        repyboi=data["officials"][i]['name']
        global reps
        reps.append(repyboi)
        website=data["officials"][i]['urls'][0] #get the reps website so the user can reach out
        global webpages
        webpages.append(website)
        i+=1
    return reps

def compare_opinions(rep):
    """Generates results based on comparing the opinions with weight to user priorities"""
    passion=0
    #for Bill in comparing_votes:
        #passion+=Bill.user_preference #get the total perference votes to guage relative preference
    similarity=0
    agree=0
    for Bill in comparing_votes:
        if rep==1:
            if Bill.rep1_vote!='No Vote' and Bill.rep1_vote!='Not Voting':
                passion+=1
                if Bill.rep1_vote==Bill.user_vote:
                    agree+=1
        elif rep==2:
            if Bill.rep2_vote!='No Vote' and Bill.rep2_vote!='Not Voting':
                passion+=1
                if Bill.rep2_vote==Bill.user_vote:
                    agree+=1
    if passion==0:
        passion=1
    similarity=agree/passion# use later*(Bill.user_preference/passion) #multiply relative preference by binary of agreement
    return "Similarity score of "+str(similarity*100)+" % with representative "+ reps[rep-1]

    """Generates results based on comparing the opinions with weight to user priorities

    passion=0
    similarity=0
    for bill in comparing_votes:
        passion+=bill.user_preference #get the total perference votes to guage relative preference
    for bill in comparing_votes:
        similarity+=bill.does_agree()*(bill.user_preference/passion) #multiply relative preference by binary of agreement
    return "Similarity score of "+str(similarity*100)[:5]+"%" #turns score into percentage with 2 past decimal"""

def give_me_things():
    """Turns info into format for HTML"""
    descriptions=[]
    i=0
    while i< len(comparing_votes):
        descriptions.append(comparing_votes[i].name+': '+comparing_votes[i].question) #shortened version of API info
        i+=1
    return descriptions

"""USER INPUT"""

def get_user_answers(answers):
    """takes a list of answers and puts them into the attributes of the bills"""
    i=0
    while i< len(answers):
        comparing_votes[i].user_vote=answers[i]
        i+=1

def get_rep_answers():
    """Gathers the representatives votes from the attributes of the Bill objects into lists that Flask can use"""
    representatives=reps
    rep1_answers=[]
    rep2_answers=[]
    print(representatives)
    for Bill in comparing_votes:
        Bill.get_vote(representatives) #API calls
        rep1_answers.append(Bill.rep1_vote)
        rep2_answers.append(Bill.rep2_vote)
    print (rep1_answers, " ", rep2_answers)
    return [rep1_answers, rep2_answers]
    #return [["Yes", "Yes", "Yes", "Yes"],["No","No","No", "No"]]

def get_links():
    """Grabs links from Bill object attributes and turns them into a list that Flask can use"""
    links=[]
    for Bill in comparing_votes:
        links.append(Bill.link)
    return links

""" This is Main Page Code"""
from flask import Flask
app = Flask(__name__)

from flask import render_template
from flask import redirect, url_for, request

ZIPcode=0

@app.route('/')
def zipentry():
    return render_template('zipcode3.html')

@app.route('/ZIP', methods =['POST'])
def ZIP():
    Zip=""
    Zip = request.form['ZIP']
    reps=get_rep(Zip)
    return redirect(url_for('questions'))

@app.route('/questions', methods = ['POST', 'GET'])
def questions():
    Votes= give_me_things()
    links= get_links()
    return render_template('ZIPquestionaire2.html', Vote1=Votes[0], Vote2=Votes[1], Vote3=Votes[2], Vote4=Votes[3], Vote5=Votes[4], Vote6=Votes[5], link1=links[0], link2=links[1], link3=links[2], link4=links[3], link5=links[4], link6=links[5])

@app.route('/results', methods = ['POST'])
def results():
    Score=""
    Votes= give_me_things()
    answers=[]
    i = 1
    answers.append(request.form['Q1'])
    answers.append(request.form['Q2'])
    answers.append(request.form['Q3'])
    answers.append(request.form['Q4'])
    answers.append(request.form['Q5'])
    answers.append(request.form['Q6'])
    get_user_answers(answers)
    rep_answers = get_rep_answers()
    Score1= compare_opinions(1)
    Score2= compare_opinions(2)
    return render_template('Results2.html', Score1=Score1, Score2=Score2, UserScore1=answers[0], Rep1Score1=rep_answers[0][0], Rep1Score2=rep_answers[0][1], Rep1Score3=rep_answers[0][2], Rep1Score4=rep_answers[0][3], Rep1Score5=rep_answers[0][4], Rep1Score6=rep_answers[0][5], UserScore2=answers[1], UserScore3=answers[2], UserScore4=answers[3], UserScore5=answers[4], UserScore6=answers[5], Rep2Score1=rep_answers[1][0], Rep2Score2=rep_answers[1][1], Rep2Score3=rep_answers[1][2],  Rep2Score4=rep_answers[1][3], Rep2Score5=rep_answers[1][4], Rep2Score6=rep_answers[1][5], Vote1=Votes[0], Vote2=Votes[1], Vote3=Votes[2], Vote4=Votes[3], Vote5=Votes[4], Vote6=Votes[5], Rep1Page=webpages[0], Rep2Page=webpages[1], Rep1Name=reps[0], Rep2Name=reps[1])

if __name__ == '__main__':
    app.run()
    #print (get_rep('02457'))
