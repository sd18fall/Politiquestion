"""" This file contains the functions that the web app will use to display information to the user and to calculate similarity to representative votes.
Authors: Rockwell Gulassa, Bailey Wolfe, Miguel Castillo
APIs: ProPublica, Google Civic API
"""
import requests
import bills
from urllib.request import urlopen
import json
from pprint import pprint
from bills import Bill

from flask import Flask
app = Flask(__name__)

from flask import render_template
from flask import redirect, url_for, request

"""GLOBAL LISTS"""
reps=[]
webpages=[]

"""BILL LIST"""
comparing_votes=[
Bill('Child Interstate Abortion Notification Act', 'https://www.congress.gov/bill/109th-congress/senate-bill/403?q=%7B', 's403', '109', '2', '216', "Should it be a crime to knowingly transport a minor across a state line to obtain an abortion without satisfying a parental involvement law in the minor's resident state?"),
Bill('North American Energy Security and Infrastructure Act of 2016', 'https://www.congress.gov/bill/114th-congress/senate-bill/2012?q=%7B', 's2012', '114', '2', '54', "Do you want our power grid to move toward more sustainable options?"),
Bill('Defense of Marriage Act', 'https://www.congress.gov/bill/104th-congress/house-bill/3396', 'hr3396', '104', '2', '280', "Do you support LGBTQ+ rights in relation to marriage?"),
Bill('Patient Protection and Affordable Care Act', 'https://www.congress.gov/bill/111th-congress/house-bill/3590?q=%7B%22search%22%3A%5B', 'hr3590', '111', '1', '396', "Do you approve of the Affordable Care Act (Obamacare)?"),
Bill('Support for Patients and Communities Act', 'https://www.congress.gov/bill/115th-congress/house-bill/6?q=%7B', 'hr6', '115', '2', '210', "Should the United States finance a response to the Opioid Crisis?"),
Bill('Tax Cuts and Jobs Act', 'https://www.congress.gov/bill/115th-congress/house-bill/1?q=%7B', 'hr1', '115', '1', '323', "Do you promote comprehensive tax cuts, especially for corporations?"),
Bill('Economic Growth, Regulatory Relief, and Consumer Protection Act', 'https://www.congress.gov/bill/115th-congress/senate-bill/2155', 's2155', '115', '2', '54', "Should banks be deregulated?"),
Bill('Department of Defense Appropriations Act, 2017', 'https://www.congress.gov/bill/114th-congress/house-bill/5293?q=%7B', 's5293', '114', '2', '136', "Should the U.S. allocate more funds to the military budget ($583.7 billion)?")]
#Bill("Countering America's Adversaries Through Sanctions Act",'https://www.congress.gov/bill/115th-congress/house-bill/3364', 'hr3364', '115', '1', '175', "Should the United States continue to sanction Russia, North Korea, and Iran?")

"""API FUNCTIONS"""

def get_json(url):
    """Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request."""
    f = urlopen(url)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    return response_data

def get_rep(zipcode):
    """Given a zipcode, can look up the user's representatives using an API while also grabbing their website url"""
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

def get_rep_answers():
    """Gathers the representatives votes from the attributes of the Bill objects into lists that Flask can use"""
    representatives=reps
    rep1_answers=[]
    rep2_answers=[]
    for Bill in comparing_votes:
        Bill.get_vote(representatives) #API calls
        rep1_answers.append(Bill.rep1_vote)
        rep2_answers.append(Bill.rep2_vote)
    return [rep1_answers, rep2_answers]

"""PASSING INFO TO FLASK"""

def get_links():
    """Grabs links from Bill object attributes and turns them into a list that Flask can use"""
    links=[]
    for Bill in comparing_votes:
        links.append(Bill.link)
    return links

def give_me_things():
    """Turns the question info into format for HTML"""
    descriptions=[]
    i=0
    while i< len(comparing_votes):
        descriptions.append(comparing_votes[i].name+': '+comparing_votes[i].question) #question is a shortened version of API info that get_description would output, we decided the API descriptions were too long
        i+=1
    return descriptions

"""USER INPUT"""

def get_user_answers(answers):
    """takes a list of answers and puts them into the attributes of the bills"""
    i=0
    while i< len(answers):
        comparing_votes[i].user_vote=answers[i]
        i+=1

"""COMPUTATION"""

def compare_opinions(rep):
    """Generates numeric results based on comparing the opinions with weight to user priorities"""
    passion=0
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
    similarity=agree/passion
    return "Similarity score of "+str(similarity*100)+" % with representative "+ reps[rep-1]

"""WEBAPP-FLASK"""

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
    return render_template('ZIPquestionaire2.html', Vote1=Votes[0], Vote2=Votes[1], Vote3=Votes[2], Vote4=Votes[3], Vote5=Votes[4], Vote6=Votes[5], Vote7=Votes[6], Vote8=Votes[7], link1=links[0], link2=links[1], link3=links[2], link4=links[3], link5=links[4], link6=links[5], link7=links[6], link8=links[7])

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
    answers.append(request.form['Q7'])
    answers.append(request.form['Q8'])

    get_user_answers(answers)
    rep_answers = get_rep_answers()
    Score1= compare_opinions(1)
    Score2= compare_opinions(2)
    return render_template('Results2.html', Score1=Score1, Score2=Score2, UserScore1=answers[0], Rep1Score1=rep_answers[0][0], Rep1Score2=rep_answers[0][1], Rep1Score3=rep_answers[0][2], Rep1Score4=rep_answers[0][3], Rep1Score5=rep_answers[0][4], Rep1Score6=rep_answers[0][5], Rep1Score7=rep_answers[0][6], Rep1Score8=rep_answers[0][7], UserScore2=answers[1], UserScore3=answers[2], UserScore4=answers[3], UserScore5=answers[4], UserScore6=answers[5], UserScore7=answers[6], UserScore8=answers[7], Rep2Score1=rep_answers[1][0], Rep2Score2=rep_answers[1][1], Rep2Score3=rep_answers[1][2],  Rep2Score4=rep_answers[1][3], Rep2Score5=rep_answers[1][4], Rep2Score6=rep_answers[1][5], Rep2Score7=rep_answers[1][6], Rep2Score8=rep_answers[1][7], Vote1=Votes[0], Vote2=Votes[1], Vote3=Votes[2], Vote4=Votes[3], Vote5=Votes[4], Vote6=Votes[5], Vote7=Votes[6], Vote8=Votes[7], Rep1Page=webpages[0], Rep2Page=webpages[1], Rep1Name=reps[0], Rep2Name=reps[1])

if __name__ == '__main__':
    app.run()
