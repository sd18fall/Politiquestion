# Introduction to the problem we are trying to solve
Bailey Wolfe, Miguel Castillo, and Rockwell Gulassa are three undergraduate students taking courses at Olin College of Engineering. In Fall of 2018 they joined together to try to empower democracy in the US using the software design skills they had acquired.

Driven by the high-stakes 2018 midterm elections, the students set out to empower the everyday voter by connecting them back to the very legislature that their congress members are supposed to be representing their interests in voting on. By allowing the everyday user to evaluate their representatives actual choices on the job we could minimize ideological fog and connect the voters back to the legislative process.

With that goal in mind the project was conceived as a web app that would utilize public APIs to connect the voter with their representatives based on their Zip code. From there we started research, development, and iteration.

# Versions and iterations

### Iteration 1

To start, we had separate files and functionality for the web app and the API pulls. The API pulls worked on gathering data and using that data to get the next API information. While the web app was not connected to that information, and just was created to have pre-filled templates display fake data. We did this as a first step in order to let the two pieces be developed simultaneously.

### Iteration 2

In our next iteration we tested the functionality of several main functions in Barebones.py but inputted fake data, in order to give the API coding more time. We used this iteration to add variables into the web app templates and to create more interactions in between the two pieces that were previously disconnected.

### Iteration 3

Next, we connected the APIs. We started by connecting the descriptions API. this let us have questions to display. We then got the votes of the senators from the API, but still did not have the ZIP code reading and finding senators from that functionality. Instead we used hard coded senator names to search for the votes.

### Iteration 4

Next, we connected the ZIP code API, in order to find who the user's senators were based on the ZIP code entered. This proved to be a challenge because the resulting output of names did not always match the API database of votes. In order to counter this we wrote a function that compares only the last name of the senators to each other, with no spaces or other words. This allowed us to more effectively find senator's votes.

### Iteration 5

After that, we realized that the descriptions that were being pulled from the API were pages long and we considered either just using the first 5 sentences or writing our own questions based on the bills. Instead of either option we chose middle ground. We added links, to the website where we had been pulling the descriptions from, in our questionnaire, and created our own questions for the user to answer.

### Iteration 6

Last, we decided to add an API call that got the senators personal websites and displayed that information in the results page. This was added so that the user could get more information about their senators and contact them from there if they so desired.

# The final product

# We have a demonstration video and some screenshots of our final code at the link below.

# [Results](https://sd18fall.github.io/Politiquestion/Results)
