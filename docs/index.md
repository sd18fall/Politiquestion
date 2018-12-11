# To be Completed:
## Readme (Where to input API keys)
## Add images and screenshots for implementation page
## Remove keys
## Check which packages we utilize

# Inspiration
Bailey Wolfe, Miguel Castillo II, and Rockwell Gulassa are three undergraduate students taking courses at Olin College of Engineering. In Fall of 2018 they joined together to try to empower democracy in the US using the software design skills they had acquired.

Driven by the high-stakes 2018 midterm elections, the students set out to empower the everyday voter by connecting them back to the very legislature that their congress members are supposed to be representing their interests in voting on. By allowing the everyday user to evaluate their representatives actual choices on the job we could minimize ideological fog and connect the voters back to the legislative process.

With that goal in mind the project was conceived as a web app that would utilize public APIs to connect the voter with their representatives based on their zip code. From there we started research, development, and iteration.

***

# Iteration

## Version 1

To start, we had separate files and functionality for the web app and the API pulls. The API pulls worked on gathering data and using that data to get the next API information. While the web app was not connected to that information, and just was created to have pre-filled templates display fake data. We did this as a first step in order to let the two pieces be developed simultaneously.

## Version 2

In our next iteration we tested the functionality of several main functions in Barebones.py but inputted fake data, in order to give the API coding more time. We used this iteration to add variables into the web app templates and to create more interactions in between the two pieces that were previously disconnected.

## Version 3

Next, we connected the APIs. We started by connecting the descriptions API. this let us have questions to display. We then got the votes of the senators from the API, but still did not have the ZIP code reading and finding senators from that functionality. Instead we used hard coded senator names to search for the votes.

## Version 4

Next, we connected the ZIP code API, in order to find who the user's senators were based on the ZIP code entered. This proved to be a challenge because the resulting output of names did not always match the API database of votes. In order to counter this we wrote a function that compares only the last name of the senators to each other, with no spaces or other words. This allowed us to more effectively find senator's votes.

## Iteration 5

After that, we realized that the descriptions that were being pulled from the API were pages long and we considered either just using the first 5 sentences or writing our own questions based on the bills. Instead of either option we chose middle ground. We added links, to the website where we had been pulling the descriptions from, in our questionnaire, and created our own questions for the user to answer.

## Version 6

Last, we decided to add an API call that got the senators personal websites and displayed that information in the results page. This was added so that the user could get more information about their senators and contact them from there if they so desired.

***

# Implementation

![alt text](https://github.com/sd18fall/Politiquestion/tree/master/docs/images/ "Title")



***

# Topics

## Abortion
Abortion is a medical procedure that results in the termination of a human pregnancy. Abortion has been a controversial issue not only in the United States, but across the world.  The topic has been typically split into two sides, Pro-Life, outlawing abortion except for the most extreme circumstances, and Pro-Choice, supporting a woman's ability to choose if and when she wants to undergo an abortion.

[Abortion bill](https://www.congress.gov/bill/109th-congress/senate-bill/403?q=%7B)

## Environmentalism
With concerns over climate change, many people and governments alike have been pushing for more sustainable solutions to energy, production, and consumption.

[Energy Bill](https://www.congress.gov/bill/114th-congress/senate-bill/2012?q=%7B)

## LGBTQ+ Rights
This topic covers issues from same sex marriage to LGBT adoption rights. Much of the public still condemns gay marriage, while others are pushing the frontier of equality for this emerging population

[LGBTQ+ Rights Bill](https://www.congress.gov/bill/104th-congress/house-bill/3396)

## Defense Budget
Military spending has for decades been the United States' biggest source of spending. Now, the military budget makes up more than half of all government spending and continues to increase yearly.

[Defense Budget Bill](https://www.congress.gov/bill/114th-congress/house-bill/5293?q=%7B)

## Government Subsidized Health Care
With the introduction of the Affordable Care Act, health care has become a requirement for most citizens and subsidized by the U.S. government to provide cheaper and more accessible options for everyone.  The tax penalty for not having health care and ineffectiveness of the health care system has been a main concern for critics.

[Health Care Bill](https://www.congress.gov/bill/111th-congress/house-bill/3590?q=%7B%22search%22%3A%5B)

## Opioid Crisis
The opioid crisis is a spreading pandemic of the use and abuse of prescription pain relievers, heroin, and fentanyl. Use of opioids has only increased in recent years, causing increases in addiction, overdoses, and the spread of infection diseases like HIV.

[Opioid Response Bill](https://www.congress.gov/bill/115th-congress/house-bill/6?q=%7B)

## Tax cuts
Taxes throughout history have been a point of contention for governments and citizens. Some advocate for higher taxes as a means of wealth distribution, while others view taxes as the government seizing hard earned private property.

[Tax Cuts and Jobs Act](https://www.congress.gov/bill/115th-congress/house-bill/1)

## Bank Deregulation
After the 2008 financial crisis, regulation of banks has been a high-profile subject for politicians and economists. While many have argued to have banks heavily regulated in order to prevent this from happening again, others say the banks have been over regulated in response to the crash, so much so that we are stifling economic growth.

[Bank Deregulation Bill](https://www.congress.gov/bill/115th-congress/senate-bill/2155)

***

# How to download our program

You can download all the files for Politiquestion from the GitHub. To run the program please run the Barebones.py file from the terminal.

## What packages you will need to run it

The Python packages needed to run this program is as follows:
* Requests 
    $ pipenv install requests
* json
    built in module
* pprint
    built in module
* Flask
    $ pip install Flask
* urllib.request
    built in module

## What API's we will use and how to get an API Key

Google Civic Informaiton API - Follow the intructions on Google's [Credentials page](https://console.developers.google.com/apis/credentials) to recieve an API key

ProPublica API - You can sign up to request an API key at [ProPublica's Data Store](https://www.propublica.org/datastore/api/propublica-congress-api)
