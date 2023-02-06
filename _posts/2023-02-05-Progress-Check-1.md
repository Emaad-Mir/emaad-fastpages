---
toc: true
layout: post
description: This blog goes over what we have done so far for the CPT as well as the plans for the future.
categories: [extra]
title: CPT Progress Check 1
image: /images/college-board-logo.png
comments: true
---

# Overview

This blog serves as a status on our CPT project so far, and includes important things such as what I have done so far, what I plan to do for next week onwards, and much more. I hope that the content here helps anyone who may be struggling to think of a plan for their project.

# Recap: What is Our Project?

The name of our project is called "Theee Arcade", and it is intended to serve as an arcade for users to provide them with an immersive, fun experience. The users will have multiple games to choose from and will even be able to view a leader board to see where they are compared to other registered users.

In addition to what our project actually is, below is a table that connects what we are doing to College Board's six criteria for the Create Performance Task: 

|Row on the rubric|Application to my project|
|-----------|-----------|
|Program Purpose and Function|The purpose of my project is to entertain and challenge the user by having them guess a word with no hints provided. |
|Data Abstraction|My project uses several lists (blanks and progress) to store the number of letters that the user has guessed correctly to be in the word (two code segments to be determined)|
|Managing Complexity|The project uses lists to store the user's entries, which is far more efficient and less time consuming than making a variable for every single entry that the user inputs correctly.|
|Procedural Abstraction|The procedure update_progress uses sequencing, selecting, and iteration to keep track of the user's progress in guessing the word. Once the progress made is equal to the word randomly generated, the user has officially won.|
|Algorithm Implementation|My project will call the procedure as described above, although I will continue to figure out more ways to make the algorithm have more depth and complexity to it (not inefficient).|
|Testing|A new word will be randomly generated each round with differing results for each of the two test runs (still figuring this row out as well)|

# What Progress Have I Made Thus Far?

For the first week, we were given a few coding hours in class to begin working on our project for both N@tM and the CPT. The rest of this blog goes into detail on some of the tangibles that I have thus far for this week, as well as any problems/concerns that I have regarding it.


# Tangible 1: Flask/JavaScript Table

Below is an image of two of the same table, with one made in Flask and one made in JavaScript. The table that is made with Flask or JavaScript is clearly labeled at the top of each table:

![]({{site.baseurl}}/images/tangible1.png "https://github.com/Emaad-Mir/emaad-fastpages")

The table made above serves almost as a menu of games for the user to choose from once they go to our main arcade page. It will kind of resemble an entrance to a real life arcade. When the user gets to this page, they will be able to see the name of each game, the description of each game, and when the game was made. While this is not visible in the image above, I will also be adding a column that includes the link to each game in the table. Once the user clicks on the link to whatever game they choose, they will then be presented with the main page corresponding to that game created by one of us (ex. they could be brought to the Hangman page created by me!).

## What I am Concerned About

While I have a pretty solid idea on how I want to implement this table into our project, I am concerned about how I will make the table look nice when it is presented to the user. Even though design should be the least of my worries at this point, I still would like to make those who test this application excited when they first look at the page with this table. This way, they will be more drawn into the games and will look forward to seeing how everything works out. In addition to the "cosmetics" of table, I am also worried about figuring out how to add the borders to the table so that it looks like an actual table, but this should hopefully be an easy fix. 

# Tangible 2: JavaScript Code

Last week, I showed some sample code that I wrote in Python that I plan to use for my CPT project. This week, I have the same code performing the same functions but in JavaScript, and this is the language that I plan to use in creating the actual page for my part of the project. If you would like to see the video of the code segment running, you can click on the image of hangman below, where you will see a few test runs of the project. 

[![Lol]({{site.baseurl}}/images/hangman.png)]({{site.baseurl}}/images/videos/Tangible for CPT.mp4 "monkey")

## Explanation of the Video + What I am Concerned About

While the functionality demonstrated in the video is pretty self-explanatory, there are a couple of things worth nothing. The blanks list is what allows you to see the number of blanks in the output box that corresponds to the number of letters in the randomly chosen word from word_list. I also added the user_input.lower so that it does not matter if the user inputs an upper case or lower case letter. Once the user has guessed all of the letters in the word correctly, the code will exit and the user will be presented with a "You Win!" message (might be a separate screen for the real deal). 

One problem that I have with this, however, is that the randomly generated word begins with much more blanks than it really has, which could mislead the user into thinking that the word is really long. I have tried changing certain lines of code, mainly the lines regarding the blanks array, but no matter what I do, I either I have one big blank or many small blanks, which is an issue that I hope to resolve by the end of this week. For me to fix this issue, I will need to use Google or consider asking my teammates for help or, just in case, I could ask Mr. Yeung or Mr. Mortensen and walk them through what I have tried to do. 

# Plans for Next Week Onwards!

This week is looking to be a very busy week, as we have multiple work days according to the schedule on the APCSP blog. With the very busy week that we have ahead of us, as well as the week after leading up to when we present our N@tM project, we plan to get a lot of things done with our project. Below are some things that we would like to finish for the week of February 6 to February 10:

- Getting our project deployed (AWS): In order for us to connect the frontend and backend portions of the project, we need to deploy our flask on AWS so that the process of the data being collected and stored can occur without error. We hope to get this done pretty early in the week, as we will likely be expected to have both parts connected by the end of this week.

![]({{site.baseurl}}/images/aws.png "https://github.com/Emaad-Mir/emaad-fastpages")


- Begin working on our actual pages (using family reunion repo): Now that our entire team has the code that we would like to use ready to go, we need to actually create the pages that the user will see depending on which game they choose from the table mentioned earlier in Tangible 1. For our frontend portion of the project, we will be using Mr. Mortensen's Leuck Family Reunion as a template/starting point for our project, and we hope to have all, if not most of our pages created by the end of this week. To recap, this is what the default template for Mr. Mortensen's family reunion looked like (we will make many changes to this and may even do a before and after kind of thing!):

![]({{site.baseurl}}/images/leuck.png "https://github.com/Emaad-Mir/emaad-fastpages")

- Style the flask/JavaScript table (will decide which one I want to use): As mentioned earlier, I created two of the same table, with one made in Flask and one made in JavaScript. While this will likely be done last, I do believe that it is important that I consider the overall "cosmetics" of our project to demonstrate that some effort was put in to making the website look nice and not just into the code. Below is an example that I could take inspiration from in styling my able in CSS/HTML/JavaScript:

![]({{site.baseurl}}/images/leuck.png "https://github.com/Emaad-Mir/emaad-fastpages")


# Overall Reflection

I will continue to make these blogs that document the progress that we make each week (or even day!), as this way, people who are on my team can have a review in front of them of what we have done and what we still need to do. I also feel that these blogs will be useful for myself, as if I ever want to look back at a project like this and see what led up to this, I can always turn to these progress blogs to see how we built up to our final project. Clearly, from doing this blog, I realize that I have some strengths and weaknesses in what we have so far. For me personally, some positives are that I have a plan on how I would like to implement my tangibles, I know what code I will be using, and I have a good idea of what I (as the Scrum Master) should do to get our team to complete what we want to complete. Some negatives, however, are that compared to other teams, we may be a bit behind, as we do not quite have our actual pages/features on the family reunion just yet. However, we will make sure that we will use the time in class to finish that part of the project so that we will not have to wait until the last minute to finally put something out for N@TM. 