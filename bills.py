import Barebone.py
user_answers= []#get user answers as list from WebApp code
i=0
while i <len(user_answers): #convert that list into attributes of the bills
    if user_answers[i]='yes':
        comparing_votes[i].user_vote=1
    else:
        comparing_votes[i].user_vote=-1
    i+=1

class bill(object):
    def __init__(self, name, id):
        self.name=name
        self.id=id
        self.congress = congress
        self.description=get_description(self)
        self.rep_vote=get_vote(self)
        self.user_vote=0
        self.user_preference=1 #scale
    def __str__(self):
        print(self.name)
        if self.rep_vote=self.user_vote:
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
        url= "https://json?id="+self.id+"&key=""
        data=get_json(url)
        return data[description]
     def get_vote(self):
        url = "https://api.propublica.org/congress/v1/"+self.congress+"/bills/"+self.id+".json&key=a3Kt3J22sEpWhvLjXTrtWf4V560B8XExhkeOmMkD"
        data=get_json(url)
        list = data[results][votes][vote][positions]
        for i in list:
            if i['name']==rep:
                self.rep_vote=i['vote_position']
            return


"""BILLS"""
bills=[
bill('North American Energy Security and Infrastructure Act of 2016', s2012, 114),
bill('Child Interstate Abortion Notification Act', s403),
bill('Defense of Marriage Act', hr3396)]
