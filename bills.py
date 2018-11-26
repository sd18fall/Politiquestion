#get user answers as list from WebApp code
while i <len(user_answers): #convert that list into attributes of the bills
    if user_answers[i]='yes':
        comparing_votes[i].user_vote=1
    else:
        comparing_votes[i].user_vote=-1
    i+=1

class bill(object):
    def __init__(self, name):
        self.name=name
        self.description= #lookup on API based on name
        self.rep_vote=0
        self.user_vote=0

"""BILLS"""

bill('name')
bill('name')
