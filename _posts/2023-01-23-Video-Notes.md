---
toc: true
layout: post
description: This blog explains what it is shown in the video as well as reflects some of the challenges I faced while doing this week's hacks.
categories: [extra]
title: Videos Explanation/Reflection
image: /images/college-board-logo.png
comments: true
---

# Overview: What Am I Talking About?
This week, we were all assigned to use what we learned from the tech talks about API/Control and Database/Model to create two videos that demonstrate the following:

# Videos

## API/Control Video
- Includes create and read API endpoints for the project
- Tests the api endpoints with test cases in Postman (adding entry, removing entry, etc.)
- Frontend for Create and Read endpoints
- No more than 30-60 seconds long

## Database/Model Video
- Shows the use of sqlite extensions/command line to update data in the table (adding and/or removing rows)
- Shows that you created your own .py file (for me, it was games.py)
- No more than 30-60 seconds in length

# So, How Was the Experience? Difficult? Really Easy?

For the most part, as shown in both of my videos, I was able to demonstrate everything asked for while staying within the constrained time frame of 30-60 seconds. However, I experienced many challenges as I made my way through this week's hacks, but with what I was able to turn in, I think the challenges helped me learn a lot about myself.

# Challenges

## Challenge 1: Having to Get the New Version of Flask

During the tech talk that Mr. Yeung gave about Postman, he demonstrated copying and pasting the link into whichever request it was, whether it was GET or POST (this is also shown in my API/Control video). Many people, including me, began to notice how Yeung's port number (8086) was different from ours (5000). It turned out that the version of flask from the last trimester was old, and we would need to clone the repository with the new version of flask. Thankfully, this was not too difficult of a task, but I found it interesting about how there was now a completely new version of flask with a new port number.

## Challenge 2: Link to Application Would Show Error

Right after cloning the repository, I made sure that my python interpreter was set to base (anaconda) and that I had flask installed using the command pip install flask. However, upon clicking on the link given in the terminal, I came across this error:

![]({{site.baseurl}}/images/operationerror.png "https://github.com/Emaad-Mir/emaad-fastpages")

When I asked Mr. Yeung about it, he told me that I needed to follow the instructions in the readme file in the new version of the flask application. Thankfully, when I followed the instructions, the application showed up like it should have, shown below:

![]({{site.baseurl}}/images/yay.png "https://github.com/Emaad-Mir/emaad-fastpages")

I began to notice, however, that each time I open VSCode (before it was previously not on), I end up having to follow the exact same steps over and over again. Fortunately, the more times I did it, the less work it was to me, and it ended up becoming much less of a burden over time :).

## Challenge 3: Many Rows Would Be Added to the Table Unintentionally

When I began to work on adding data to the table and list on the web application, I noticed something very strange. First off, the class I created was a Games class, with three attributes: name, description, and date made. Previously, I had two entries in the table, with both being Hangman. Sometimes, however, if I tried to add something else that was not hangman (POST) and made a GET request proceeding the POST request, not only did it add the new entry, but it also added multiple Hangman entries at the same time, making most of the table filled with the exact same information about Hangman (10 times). Thankfully, once I realized how to make a delete request (which also took some time!), I was able to remove all extra entries and make it so that only the entry I made a POST request for would show up after the GET request.


# Reflection

As shown by the three challenges above, I did not have an easy time completing this. However, I think that these challenges really helped me learn a lot, and I hope that the two videos I made will serve as a helpful study/recap tool for both myself and other students taking this class. Even though the process was quite rough, I still enjoyed the feeling I got when I was able to get everything working the way it was supposed to. Also, if I ever play Hangman, I will always be reminded of doing this project!


![]({{site.baseurl}}/images/hangman.png "https://github.com/Emaad-Mir/emaad-fastpages")





