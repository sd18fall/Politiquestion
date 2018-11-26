
Background and Context
The main idea of our project is to create a political alignment survey that utilizes data on your specific congressional representatives and tells you how well you align with your delegate.  In this project, we will explore web/database scraping, data parsing, user input, and geolocation.  Our minimum viable product is a (potentially) handmade database with a few representatives and voting patterns of a few key topics of contention for users to choose alignment from.  A stretch goal would be having all 50 states be represented in our survey, with a more advanced scraped database of questions. 

This breaks into 5 main functions: 
1. Find_My_Rep: uses APIs/geocoding to find the representative of an individual based on their zip code 
	Technical challenges: Finding good and easy to use APIs 
2. Find_Votes: Uses APIs to find the voting records of your representative
Technical challenges: It may end up being a hardcoded set of data due to time restraints, this would make Summarize_Opinions easier to create as well due to comparative records being used. 
3. Summarize_Opinions: converts database data (votes) into comparable viewpoints
	Technical challenges: Pulling the same or similar referendums for each representative.
4. User_Opinions: takes user input and converts it into comparable viewpoints
Technical challenges: Writing questions that can get good user input while still being computationally comparable to the output from Sumarize_Opinions.
5. Compare_Opinions: prints readable comparison between individual and their representative
Technical challenges: if we want to make it understandable for the user we might need more visualization code

Key Questions
In what ways might we assign roles/tasks to each person and work in tandem or jointly? 
Is scraping most important or should we focus elsewhere to begin?
Are there technical challenges you think we may have missed?
Do you see there being a more structurally efficient system architecture than this?
Where would make sense for us to start coding at?
How do we turn representative votes into answerable questions for the user?
What topics do you care about in a survey of politics?
What features or functionality would you like to see or do you not need?

Agenda for technical review session
In this session we plan to do a quick overview of our project, then start asking questions around basic project scoping, specifically scraping voting and bill information off government records. After that if we have time, we will go into a more technical set of questions. We will send out the survey last. 

Feedback Form (https://goo.gl/forms/2P7dq5T4ETTfieqt2)
