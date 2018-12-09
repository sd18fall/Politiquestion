# Introduction to the problem we are trying to solve

We are Politiquestion. We have a survey that will help you see how well your senators are representing YOUR views.

We are trying to solve the problem that often what politicians say doesn't line up with what they vote. We want the common voter to be able to go on our web app, and find out what their senators are actually doing, and how well it aligns with their viewpoint.

# How we got the inspiration for this project

We knew we wanted to do something related to social justice, and as we were starting this project the midterm elections were coming up. We realized that we could make an impact in future elections be creating this web app.

# Walkthrough of versions and iterations

In our first iteration we had separate files and functionality for the web app and the API pulls. The API pulls worked on gathering data and using that data to get the next API information. While the web app was not connected to that information, and just was created to have pre-filled templates display fake data. We did this as a first step in order to let the two pieces be developed simultaneously.

In our next iteration we tested the functionality of several main functions in Barebones.py but inputted fake data, in order to give the API coding more time. We used this iteration to add variables into the web app templates and to create more interactions in between the two pieces that were previously disconnected.

The third iteration was when we connected the APIs. We started by connecting the descriptions API. this let us have questions to display. We then got the votes of the senators from the API, but still did not have the ZIP code reading and finding senators from that functionality. Instead we used hard coded senator names to search for the votes.

Next, we connected the ZIP code API, in order to find who the user's senators were based on the ZIP code entered. This proved to be a challenge because the resulting output of names did not always match the API database of votes. In order to counter this we wrote a function that compares only the last name of the senators to each other, with no spaces or other words. This allowed us to more effectively find senator's votes.

After that, we realized that the descriptions that were being pulled from the API were pages long and we considered either just using the first 5 sentences or writing our own questions based on the bills. Instead of either option we chose middle ground. We added links, to the website where we had been pulling the descriptions from, in our questionnaire, and created our own questions for the user to answer. 

Last, we decided to add an API call that got the senators personal websites and displayed that information in the results page. This was added so that the user could get more information about their senators and contact them from there if they so desired.

# The final product
