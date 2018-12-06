#import Barebones
#from Barebones import get_json
import json
import requests
from urllib.request import urlopen

#from congress import Congress
X_API_Key = 'a3Kt3J22sEpWhvLjXTrtWf4V560B8XExhkeOmMkD'
api_url_base = "https://api.propublica.org/congress/v1/"
#congress = Congress(a3Kt3J22sEpWhvLjXTrtWf4V560B8XExhkeOmMkD)

def get_json(url):
    """Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urlopen(url, 1)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    return response_data

class Bill(object):
    def __init__(self, name, ID, congressnum=0, sessionnum=0, rollnum=0):
        self.name=name
        self.ID=ID
        self.congressnum = congressnum
        self.sessionnum = sessionnum
        self.rep1_vote='Yes'
        self.rep2_vote='No'
        self.user_vote=0
        self.user_preference=1 #scale
        self.description=self.get_description()
    def __str__(self):
        print(self.name)
        # if self.rep_vote==self.user_vote:
        #     print("You and your representative agree!")
        # else:
        #     print("Your representative voted differently than you")
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
    def get_vote(self):
        headers={'X_API_Key':'a3Kt3J22sEpWhvLjXTrtWf4V560B8XExhkeOmMkD'}
        url = ("https://api.propublica.org/congress/v1/"+self.congressnum+"/senate/sessions/"+self.sessionnum+"/votes/"+self.rollnum+".json", headers)
        r = requests.get(url, headers=headers)
        data= r.json()
        list = data['results']['votes']['vote']['positions']
        for i in list:
            if i['name']==reps[0]:
                self.rep1_vote=i['vote_position']
            elif i['name']==reps[1]:
                self.rep2_vote=i['vote_position']
            return
#
"""BILLS"""
bills=[
Bill('North American Energy Security and Infrastructure Act of 2016', 's2012', '114', '2', '54'),
Bill('Child Interstate Abortion Notification Act', 's403', '109', '2', '216'),
Bill('Defense of Marriage Act', 'hr3396', '104', '2', '280'),
Bill('Patient Protection and Affordable Care Act', 'hr3590', '111', '1', '396')]

reps = ['Lamar Alexander', 'Michael Bennet']
bills[0].get_vote

print(bills[0].rep1_vote)
