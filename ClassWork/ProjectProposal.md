Bailey, Rocky, Miguel

The Big Idea: What is the main idea of your project? What topics will you explore and what will you generate? What is your minimum viable product? What is a stretch goal?
The main idea of our project is to create a political alignment survey that utilizes data on your specific congressional representatives and tells you how well you align with your delegate.  In this project, we will explore web/database scraping, data parsing, user input, and geolocation.  Our minimum viable product is a (potentially) handmade database with a few representatives and voting patterns of a few key topics of contention for users to choose alignment from.  A stretch goal would be having all 50 states be represented in our survey, with a more advanced scraped database.  

Learning Goals: 

Bailey: I want to work on web based apps, or maybe a downloadable app. I want to learn how to NOT go down rabbit holes!!! I also want to learn more about using data in a way that provides value. 

Miguel: I would like to learn about handling user inputs and having the program react to what the user is doing.  This may involve using decision trees and getting more inputs than just variables.

Rocky: I would like to learn skills applicable to a project I want to work on after this. Those skills would be in database management, geolocation, and web app development. If I learn skills or even just get experience in these fields I will feel more confident and comfortable in my own project. 

Implementation Plan: This will probably be pretty vague initially. Perhaps at this early juncture you will have identified a library or a framework that you think will be useful for your project. If you don’t have any idea how you will implement your project, provide a rough plan for how you will determine this information.

This “survey” would begin with the user inputting their zip code or congressional district number.  After seeing what referendums their delegate has voted on, we will ask the user similar questions to gauge their opinion on the topic.  We may implement a user information input section that gives an alignment score total for each type of policy as well as a grand total. A answer that is the same as the representative could be +1 neutral 0 and different view could be -1.  After taking the survey, it will tell the user how well their delegate’s views aligns with theirs and encourages them to vote! 

Project schedule: You have 6 weeks (roughly) to finish the project. Sketch out a rough schedule for completing the project. Depending on your project, you may be able to do this in great specificity or you may only be able to give a broad outline. Additionally, longer projects come with increased uncertainty, and this schedule will likely need to be refined along the way.

Pieces of the project: 
User input zip code
Pull which representatives belong to this user
User inputs survey answers
Calculation of similarity using senator vote data, and user inputs
Output a view of similarity scores
Create a database of senators and votes on controversial issues
Create questions centered around issues

Nov. 5th - Find a usable datasource for the political votes of representatives and decide on 2-3 topics for the survey
Week 1 - Find a usable datasource for the political votes of representatives and decide on 2-3 topics for the survey. Use the user’s zip-code to geolocate their congressional district
Week 2 - Collecting representative voting records and results
Week 3 - Sorting voting records into a useable database
Week 4 - Barebones user interface and start figuring out calculation method
Week 5 - Polished user interface with connection to database results
Week 6 - Debugging and completed Project

Collaboration plan: How do you plan to collaborate with your teammates on this project? Will you split tasks up, complete them independently, and then integrate? Will you pair program the entire thing? Make sure to articulate your plan for successfully working together as a team. This might also include information about any software development methodologies you plan to use (e.g. agile development). Make sure to make clear why you are choosing this particular organizational structure.

We will work together at the same time. This makes communication easier so we don’t duplicate work. We will have regular meetings. This will be fairly easy due to living in the same building. We will work on the project modularly so that the components are working before integration. 

Risks: What do you view as the biggest risks to the success of this project? Since you’ve identified them, how will you mitigate them?

The biggest risks to the success of this project is the data we collect on voting results.  The voting topics we are pulling from have to include a multitude of representatives, a clear issue, and a decisive choice between one side and another that can also be made by the user, with minimal information.  

Additional Course Content: What are some topics that we might cover in class that you think would be especially helpful for your project?
Web design and scraping techniques would be useful.
Model view controller could be a helpful concept to segregating user interface and database work.
Toolboxes that would be useful include: Geocoding and Web Apps

