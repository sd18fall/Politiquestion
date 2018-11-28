"""" This file contains the functions that the web app will use to display
information to the user and to calculate similarity to representative votes.
"""

import bills
from urllib.request import urlopen
import json
from pprint import pprint
reps=[]
comparing_votes=[bill("Billington", ID, session), bill("Billsby", ID, session), bill("Billard", ID, session), bill("Billiam", ID, session), bill("Bill", ID, session), bill("Billy", ID, session)] #import bills list from bills.py


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
    return "Similarity score of "+str(similarity*100)+"%"

def give_me_things():
    """Turns info into format for HTML"""
    descriptions=bills.get_descriptions()
    #i=0
    #while i< len(comparing_votes):
        #description.append(comparing_votes[i].name+': '+comparing_votes[i].description)
        #i+=1
    #return descriptions
    return ['hello', 'this', 'is', 'a', 'list']

"""USER INPUT"""

def get_user_answers(answers):
    i=0
    while i< len(comparing_votes):
        comparing_votes[i].user_vote=answers[i]
        i+=1

def get_rep_answers():
    """Turns info into format for HTML"""
    answers=[]
    i=0
    while i< len(comparing_votes):
        answers.append(i.rep_vote)
        i+=1
    #return answers
    return ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'No']
