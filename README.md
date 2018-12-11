## Politiquestion

This is a web app that gives questions that the user can answer and find out who their senators are and how they voted on issues.  

### Authors: 
  Rocky, Miguel, Bailey

### APIs: 

  Google Civic Information API - Follow the instructions on Google's [Credentials page](https://console.developers.google.com/apis/credentials) to recieve an API key

  ProPublica API - You can sign up to request an API key at [ProPublica's Data Store](https://www.propublica.org/datastore/api/propublica-congress-api)

## Running the Code:

### First download all files in repository. 

### The Python packages needed to run this program are as follows:

* Requests 

    $ pipenv install requests
* Flask

    $ pip install Flask

### Add your API keys into the code:

Google Civic Information API goes into line 45 in Barebones.py where it says "Google Civic Key". Leave the quotes when you add the key in.

The ProPublica key goes into lines 40 and 57 in bills.py where it says "ProPublica Key". Leave the quotes when you add the key in. 

### Once these are downloaded and installed, the web app only requires you to run the Barebones.py file in the WebApp folder. 

The web app is in the file named Barebones.py, in the folder called WebApp. This file will start the web app when run. Click on the link in the terminal to use the web app.
