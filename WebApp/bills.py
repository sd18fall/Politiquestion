#import Barebones
#from Barebones import get_json
import json
import requests
from urllib.request import urlopen

def get_json(url):
    """Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urlopen(url, 1)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    return response_data

def cut_off(name):
    return name.split(" ")[-1]

class Bill(object):
    def __init__(self, name, ID, congressnum=0, sessionnum=0, rollnum=0):
        self.name=name
        self.ID=ID
        self.rollnum= rollnum
        self.congressnum = congressnum
        self.sessionnum = sessionnum
        self.rep1_vote='No Vote'
        self.rep2_vote='No Vote'
        self.user_vote=0
        self.user_preference=1 #scale
        self.description=self.get_description()
    def __str__(self):
        print(self.name)
        print(self.description)
    def does_agree(self):
        if self.user_vote==self.rep_vote:
            return 1
        else:
            return 0
    def get_description(self):
        headers = {"X-API-Key": "a3Kt3J22sEpWhvLjXTrtWf4V560B8XExhkeOmMkD"}
        url = "https://api.propublica.org/congress/v1/"+self.congressnum+"/bills/"+self.ID+".json"
        r = requests.get(url, headers=headers)
        data = r.json()
        description = data['results'][0]['summary']
        return data['results'][0]['summary']
    def get_vote(self, reps):
        headers={'X-API-Key':'a3Kt3J22sEpWhvLjXTrtWf4V560B8XExhkeOmMkD'}
        url = "https://api.propublica.org/congress/v1/"+self.congressnum+"/senate/sessions/"+self.sessionnum+"/votes/"+self.rollnum+".json"
        r = requests.get(url, headers=headers)
        data=r.json()
        rep1_name=cut_off(reps[0])
        rep2_name=cut_off(reps[1])
        r1=len(rep1_name)
        r2=len(rep2_name)
        lists = data['results']['votes']['vote']['positions']
        for i in lists:
            if i['name'][-r1:]==rep1_name:
                self.rep1_vote=i['vote_position']
            elif i['name'][-r2:]==rep2_name:
                self.rep2_vote=i['vote_position']
        return

"""BILLS"""
bills=[
Bill('North American Energy Security and Infrastructure Act of 2016', 's2012', '114', '2', '54'),
Bill('Child Interstate Abortion Notification Act', 's403', '109', '2', '216'),
Bill('Defense of Marriage Act', 'hr3396', '104', '2', '280'),
Bill('Patient Protection and Affordable Care Act', 'hr3590', '111', '1', '396')]

#reps = ['Mike Lee', 'Ted Bundy']
#bills[0].get_vote()

#x=bills[0].rep2_vote
#print (x)
#print(cut_off("Ted Cruz Happy Joe"))
