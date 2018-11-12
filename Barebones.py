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
    #url=
    #data=get_json(url)
    pass

def get_votes(rep):
    """Given a representative, uses APIs to get their voting history
    """
    pass

def vote_to_opinion(votes):
    """Coverts voting data into a form that can be computed
    """
    pass

def compare_opinions(user, rep):
    """Generates results based on comparing the opinions with weight to user priorities
    """
    pass
