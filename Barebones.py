from urllib.request import urlopen
import json
from pprint import pprint

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
    reps=[]
    i=0
    while i < len(data["officials"]):
        reps.append(data["officials"][i]['name'])
        i+=1
    return reps

def get_votes(rep):
    """Given a representative, uses APIs to get their voting history
    """
    #url=
    #data=get_json(url)
    pass

def vote_to_opinion(votes):
    """Coverts voting data into a form that can be computed
    """
    pass

def compare_opinions(user, rep):
    """Generates results based on comparing the opinions with weight to user priorities
    """
    pass
print(get_rep('02457'))
