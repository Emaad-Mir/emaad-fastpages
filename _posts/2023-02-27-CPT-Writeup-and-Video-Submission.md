---
toc: true
layout: post
description: This blog showcases the writeup for the CPT as well as the video demonstrating the functionality of my project.
categories: [extra]
title: CPT Written Response and Video Submission
image: /images/college-board-logo.png
comments: true
--- 

# Link to Full Code
If you would like to see all of the code that I wrote to create this program, you can click [this link](https://github.com/Emaad-Mir/GamesArcade/blob/gh-pages/_includes/hangman.html).

# Video Response
Link to [my video submission (YouTube)](https://youtu.be/3i7DEMg-Pv4)

# Written Response

## 3a.

### 3.a.i.
The purpose of the program is to relieve the user's boredom and entertain them by challenging them to guess a random word.


### 3.a.ii.

In the video, the user plays two rounds of hangman: one in which they guess the word and win and one in which they fail to guess the word in the seven lives they were given. In the first round, the user was able to guess the correct word (HOUSE) with 5 lives remaining. The user inputted letters into the text box, and the more letters they guessed correctly, the more blanks that were filled. The user eventually guesses all of the letters correctly and is presented with the "You Win!" message. In the second round, the user was unable to guess the correct word (CONVERSATION) and lost all of their lives. The more letters the user guessed incorrectly, the more letters that were added to the list of incorrect guesses. Once the user loses all of their lives, the game ends and they are prompted with the "You Lose" message.


### 3.a.iii.

The input from the video is the user inputting letters in order to guess the randomly chosen word. The output is demonstrated by the program's response to the user's guessed letters, which is either adding the letter that the user guessed to the blanks or adding an incorrect letter guessed by the user to the list of incorrect letters. 

## 3b.


### 3.b.i.

![]({{site.baseurl}}/images/codeblock1.png)


### 3.b.ii.

![]({{site.baseurl}}/images/codeblock2.png)


### 3.b.iii.

The name of the list being used is called possibleSolutions.


### 3.b.iv.

The data contained in the list possibleSolutions represents the possible words that could be randomly chosen for the user to guess. 



### 3.b.v.

The list possibleSolutions allows many words (all added by the user) to be represented by one variable. An alternative method would be to create variables for every single word in the list, which may be a large number of variables (as previously stated, all of the words in the list are added by the user). Making a variable for every word that the user adds will make the process of creating the program unnecessarily complicated and time-consuming, which is why a list is used here. 

## 3.c.

### 3.c.i.

![]({{site.baseurl}}/images/procedure.png)


### 3.c.ii.

![]({{site.baseurl}}/images/procedurecalled.png)


### 3.c.iii.

The procedure of this program is GameOver, which passes through two parameters, solution (string) and won (boolean, true or false). The procedure is called in the function guessLetter, which updates the letters displayed on what are initially the blanks. In the procedure itself, if the boolean variable won evaluates to true (i.e. the user has guessed all of the letters), they will be presented with a "You Win!" message. Otherwise, if the boolean variable won evaluates to false (i.e. the user has run out of lives before guessing the correct word), they will be presented with a "You Lost" message. In both cases, the correct answer, or word that was randomly chosen, is revealed. In the function guessLetter, if the boolean variable goodGuess is true (i.e. the letters inputted by the user form the word that was randomly chosen, variable solution), the procedure gameOver is called, with the solution being revealed along with the boolean variable won evaluated to true. All of these functions and parameters allow for the user to see the output that corresponds to what they input (whether the letter inputted is correct, whether they are able to guess the word before running out of lives, etc.).

### 3.c.iv.

![]({{site.baseurl}}/images/algorithm.png)

The identified algorithm first checks whether the game is finished (as shown by finished in the conditional). If the variable finished is true, the program returns without doing anything else (does not return a value). If the game is not finished, it reads the letter inputted by the player (not case sensitive) and initializes a variable goodGuess to false. The algorithm then iterates through an array of solution letters, checking whether each letter matches the player's guess. If the letter does match the player's guess, the goodGuess variable is set to true, and the progress array is updated with the correct letter. After processing the guess, the updateDisplay() function is called to update the game display (i.e. fills in the blanks). If the guess was correct and the player has now won the game, the algorithm calls the gameOver() function, with the variable won being evaluated to true. If the guess was incorrect, the guess is added to an array of wrong guesses, and the player's remaining lives are reduced by one. The updateDisplay() function is called again to update the game display, and if the player has run out of lives, the gameOver() function is called to indicate that the game is over, and the player has lost. 


## 3.d

### 3.d.i.

#### Call One

The first call results from the word "Aesthetics" being guessed correctly in seven lives or less. 


#### Call Two

The second call results from the word "Intelligent" not being guessed in the seven lives given. 


### 3.d.ii.

#### Condition(s) tested by Call One

![]({{site.baseurl}}/images/firstcall.png)

The user guessing the word correctly causes the above code segment to be executed, which sets the boolean variable "won" to true and the solution variable equal to the user's progress. 


#### Condition(s) tested by Call Two

![]({{site.baseurl}}/images/secondcall.png)

The user failing to guess the word causes the above code segment to be executed, which sets the boolean variable "won" equal to false and presents the user with the "You Lost" message.


### 3.d.iii.

#### Results of Call One

A E S T H E T I C S

Lives: 5

[R, O]

YOU WIN! The correct answer was AESTHETICS.


#### Results of Call Two

_ N T E _ _ _ _ E N T

Lives: 0

[A, O, S, C, P, R, K]

GAME OVER The correct answer was INTELLIGENT.

