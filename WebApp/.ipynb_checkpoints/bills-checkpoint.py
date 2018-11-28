import Barebones
import json
import requests

#from congress import Congress
X_API_Key = 'a3Kt3J22sEpWhvLjXTrtWf4V560B8XExhkeOmMkD'
api_url_base = "https://api.propublica.org/congress/v1/"
#congress = Congress(a3Kt3J22sEpWhvLjXTrtWf4V560B8XExhkeOmMkD)

class bill(object):
    def __init__(self, name, ID, congressnum=0):
        self.name=name
        self.ID=ID
        self.congressnum = congressnum
        #self.rep_vote=get_vote(self)
        self.user_vote=0
        self.user_preference=1 #scale
    def __str__(self):
        print(self.name)
        if self.rep_vote==self.user_vote:
            print("You and your representative agree!")
        else:
            print("Your representative voted differently than you")
        print(self.description)
    def does_agree(self):
        if self.user_vote==self.rep_vote:
            return 1
        else:
            return 0
    def get_description(self):
        header = {'X_API_Key':'a3Kt3J22sEpWhvLjXTrtWf4V560B8XExhkeOmMkD'}
        url=("https://api.propublica.org/congress/v1/"+self.congressnum+"/bills/"+self.id+".json", header)
        print (url)
        data=get_json(url)
        return data[description]
    def get_vote(self):
        headers={'X_API_Key':'a3Kt3J22sEpWhvLjXTrtWf4V560B8XExhkeOmMkD'}
        url = ("https://api.propublica.org/congress/v1/"+self.congressnum+"/bills/"+self.id+".json", headers)
        data=get_json(url)
        list = data[results][votes][vote][positions]
        for i in list:
            if i['name']==rep:
                self.rep_vote=i['vote_position']
            return


"""BILLS"""
bills=[
bill('North American Energy Security and Infrastructure Act of 2016', 's2012', '114'),
bill('Child Interstate Abortion Notification Act', 's403'),
bill('Defense of Marriage Act', 'hr3396')]
listi=[]
def get_descriptions():
    for bill in bills:
        listi+=bill.get_description()
    return dicti