""""This file contains the class that the web app will use to hold information on the bills and its relevant functions
Authors: Rockwell Gulassa, Bailey Wolfe, Miguel Castillo
APIs: ProPublica, Google Civic API
"""
import json
import requests
from urllib.request import urlopen

def get_json(url):
    """Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request."""
    f = urlopen(url, 1)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    return response_data

def cut_off(name):
    """Gets last name"""
    return name.split(" ")[-1]

class Bill(object):
    """These are the bills, each of which has votes from your representatives and a page on the congress website"""
    def __init__(self, name, link, ID, congressnum=0, sessionnum=0, rollnum=0, question=""):
        self.name=name
        self.link=link
        self.ID=ID
        self.rollnum= rollnum
        self.congressnum = congressnum
        self.sessionnum = sessionnum
        self.rep1_vote='No Vote'
        self.rep2_vote='No Vote'
        self.user_vote=0
        self.user_preference=1 #scale
        self.question=question
        self.description=self.get_description()
    def __str__(self):
        print(self.name)
        print(self.description)
    def get_vote(self, reps):
        """API lookup that gets the representatives votes on this bill and puts them in the attributes"""
        headers={'X-API-Key':'PROPUBLICA_KEY'}
        url = "https://api.propublica.org/congress/v1/"+self.congressnum+"/senate/sessions/"+self.sessionnum+"/votes/"+self.rollnum+".json"
        r = requests.get(url, headers=headers)
        data=r.json()
        rep1_name=cut_off(reps[0])
        rep2_name=cut_off(reps[1]) #just looking up based on last name to avoid middle name bugs
        r1=len(rep1_name)
        r2=len(rep2_name)
        lists = data['results']['votes']['vote']['positions']
        for i in lists:
            if i['name'][-r1:]==rep1_name: #checking the last n letters where n is the length of their last name
                self.rep1_vote=i['vote_position']
            elif i['name'][-r2:]==rep2_name:
                self.rep2_vote=i['vote_position']
        return
    def get_description(self):
        """This method is an API reference that gets bill descriptions for us more modularly but they were too long to be accessible to the average user as is, so we wrote our own descriptions and linked to more information
        headers = {"X-API-Key": "PROPUBLICA_KEY"}
        url = "https://api.propublica.org/congress/v1/"+self.congressnum+"/bills/"+self.ID+".json"
        r = requests.get(url, headers=headers)
        data = r.json()
        description = data['results'][0]['summary']
        #description = cut_off2(description)
        return data['results'][0]['summary']"""
        pass
