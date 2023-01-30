---
toc: true
layout: post
description: This blog discusses my plan for my portion of the Create Performance Task (CPT).
categories: [extra]
title: Individual CPT Outline/Plan
image: /images/college-board-logo.png
comments: true
---


## Overview of Our Project

The name of our project is called "Theee Arcade", and it is intended to serve as an arcade for users to provide them with an immersive, fun experience. The users will have multiple games to choose from and will even be able to view a leader board to see where they are compared to other registered users. On Thursday, we were to present our project idea to the class, but due to the time constraint of 3-5 minutes, we were not quite able to say everything that we wanted to present. This blog serves to talk about our project but in more detail, with heavy emphasis on my individual part of the project.

## Team Member Roles

We have assigned each member of our team a page of the project for them to complete so that everybody's CPT submission will be different but still be based on the same idea. Below is a table that shows the team members, their roles, and their part of the project that they are to complete:

|Team Member|Scrum Team Role|Assigned Part of the Project|Purpose|
|-----------|-----------|-----------|-----------|
|Christopher Albertson|Frontend Developer|Guess the Number!|To help everyone learn their numbers in a fun way.|
|Prasith Chilla |Backend Developer|Sports Jeopardy|To entertain the user by having them answer questions regarding sports for points.|
|Vyaan Gautam|DevOps|Tic-Tac-Toe|To provide the user with an immersive, fun experience by allowing them to play against a fellow registered player or even a computer player. |
|Emaad Mir me)|Frontend Developer|Hangman|To entertain the user and allow them to expand their vocabulary in a fun way.|
|Chinmay Ramamurthy|Scrum Master|Guess the Countries|To challenge the user by testing their knowledge of countries around the world and seeing how fast they can name countries that start with a certain letter.|


# My Part 

Now that you have had the chance to look at what my other teammates are doing, the rest of the blog will focus solely on what I am doing and what my plan is for my part of the project.

## Wire Frames/Rough Draft

Below is a model of what I want the Hangman page to look when the user views it (please excuse the terrible Google Drawing, this is just to give me an idea of how it should appear):

![]({{site.baseurl}}/images/wireframe.png "https://github.com/Emaad-Mir/emaad-fastpages")

In this VERY rough model, you can see that at the very top, there is a link to every single game that the user can play (mine in bold to indicate that this is for the hangman page). This is essentially how we want to present the other games to the users if they decide they want to play something else. For my page specifically, I plan to have the blanks displayed as well as a letter bank so that the user knows which letters they have already guessed. The hangman will also be shown, with more body parts (head, arms, legs, etc.) appearing as the number of incorrect guesses increases. While this is not specifically in the rough model above, I also am thinking of implementing a time elapsed clock (no time limit, though), as the time taken to guess a certain word would fit well with the leader board that we want to include.


## Sample Code

Below is an image of a code segment in Python that basically shows how I want the hangman game to function (only limited to terminal for now). While this may not be a submission that could earn full credit for the Create Performance Task, it definitely meets some of the main College Board criteria. Comments are added to explain not only what the line does but to also show how it could meet the criteria:

![]({{site.baseurl}}/images/cptcodesegment.png "https://github.com/Emaad-Mir/emaad-fastpages")


## Sample Code: Explanation

While the functionality of the code is pretty self-explanatory, there are some thing worth noting about the above code segment. The blanks list is what allows you to see the number of blanks in the output box that corresponds to the number of letters in the randomly chosen word from word_list. I also added the user_input.lower so that it does not matter if the user inputs an upper case or lower case letter. Once the user has guessed all of the letters in the word correctly, the code will exit and the user will be presented with a "You Win!" message (might be a separate screen for the real deal).


## Application of CRUD

A few weeks ago, Mr. Mortensen had a tech talk about CRUD and its importance in view and frontend coding. To recap, here is what each of the letters in CRUD mean:

- C - Create
- R - Read
- U - Update
- D - Delete

Here is how my specific project follows each of these:

- Create: Each round, a new word for the user to guess will be randomly chosen from a list, and the blanks and progress made by the user will be initialized as well.
- Read: A new letter will be added to the blank if the user guesses a letter correctly, and if the user guesses incorrectly, the number of lives remaining will decrease/the number of incorrect guesses will increase.
- Update: If the user guesses a letter correctly, the letters displayed on the blanks will be updated. If the user guesses wrong, however, there will be one more body part of the man that will be hanged.
- Delete: For every letter that the user guesses, that letter will be crossed out or removed from the provided letter bank. Once the user has won and guessed the word or has lost all of their lives and lost the game, a new game will be made with another random word generated.


## Application of College Board Criteria

Here is how the sample code above meets the criteria and how it will meet the criteria that it has not quite yet met:

|Row on the rubric|Application to my project|
|-----------|-----------|
|Program Purpose and Function|The purpose of my project is to entertain and challenge the user by having them guess a word with no hints provided. |
|Data Abstraction|My project uses several lists (blanks and progress) to store the number of letters that the user has guessed correctly to be in the word (two code segments to be determined)|
|Managing Complexity|The project uses lists to store the user's entries, which is far more efficient and less time consuming than making a variable for every single entry that the user inputs correctly.|
|Procedural Abstraction|The procedure update_progress uses sequencing, selecting, and iteration to keep track of the user's progress in guessing the word. Once the progress made is equal to the word randomly generated, the user has officially won.|
|Algorithm Implementation|My project will call the procedure as described above, although I will continue to figure out more ways to make the algorithm have more depth and complexity to it (not inefficient).|
|Testing|A new word will be randomly generated each round with differing results for each of the two test runs (still figuring this row out as well)|

While I am still in the process of figuring out how I can apply my project to the rubric, I believe that what I have right now is a good start and that I will continue to build off of what I have so far leading up to N@tM and when the CPT is actually due.


# Plans for the Video

When we were grading the sample CPT submissions for the past few weeks, we saw many videos of the submissions' code working, with the written response describing what was shown in the video and beyond. 

For my project, there are several things that I will need to show in my video submission. Below is again the rough model of my page created earlier, as that will likely be the first thing that the graders see when they look into my submission:

![]({{site.baseurl}}/images/wireframe.png "https://github.com/Emaad-Mir/emaad-fastpages")

Some of the things that will likely be necessary for my video include...
- A screen that gives the user an option to press the "play" button (or something similar)
- Once the user (me) has pressed play, a screen similar to the rough model above will be shown.
- Showing me choosing a letter from the word bank and seeing if the letter turned out to be a part of the word or not
- Showing the number of chances/lives that I have remaining
- Showing specific messages for the user depending on if they have won or lost a game
- My video will likely run this program twice, each with different results:
    - One in which I win the game
    - One in which I lose the game
    - By winning one game and losing another, the graders will be able to at least see what each screen would look like for every possible result
    - The graders can also see what it looks like when a new round has started/new random word is generated
- Showing the parts hanged being added to the hanger if I guess a letter incorrectly
- The "You Win!" message or "You Lost! The word was (word)" message
- Overall, the video should show the user input, output, and functionality associated with the program that will be described in the written response

As mentioned before, I am still trying to figure everything out, but some of these bullets will definitely be taken into consideration when I get to making the actual video submission for the Create Performance Task.


## Things I am Happy With/Concerned About for My Part of the Project (So Far)

While we are not expected to have the final project ready at this time, there are several things that I am happy with and am looking forward to when I create my project. However, there are also some aspects that I am concerned about implementing/incorporating into my CPT submission.

### What I am Happy With
- My code sample does actually meet some of the College Board Criteria, and this will definitely be helpful as the deadline for our CPT begins approaching
- I can describe in enough detail how my code works, which will be important when I write my written response
- My wire frame for the project actually gives me a great idea of how I want everything to be presented to the user and will be a good reference to keep with me as I make more progress on it

### What I am Concerned About
- Although what I have thus far is a good start, I am worried that the end product will not have enough depth or complexity to it (not necessarily inefficiency), which can be problematic if I want to get full points on the CPT
- My sample code mainly lacks algorithm implementation, and I am concerned that I will not be able to properly incorporate that into the final submission and that I will not be able to describe it in enough detail so that someone else could recreate it
- With games such as Hangman, there is no complex mathematical algorithm that goes into fulfilling the overall functionality of the program, as most of it just involves words or letters. I am therefore worried that by not having some mathematical component involved in the algorithm, my algorithm will not include the necessary sequencing, selection, and iteration, thus preventing me from getting the point for that row.

# Reflection

Overall, even though there are several setbacks and limitations to the plan that I have, what I have so far is a great start and is definitely something that I can work with so that it can be improved or more refined. I will make sure to clear up the concerns that I have by maybe researching algorithms that go into making these kinds of games and using it as a source of inspiration (and citing it, of course). By doing this, I will feel much more confident about incorporating the algorithm into my program and modifying it so that it has more depth to it. While my part of the project is very important, my teammates also have their own projects to work on, and I will make sure that I help them if needed, as we will all need to present our parts for N@tM. In essence, I think I have a great idea for how I want my program to turn out in the end and can explain how it meets the College Board criteria to someone who may not be familiar with how the project was made, the rubric, or even both. 