---
toc: true
layout: post
description: For the week of 1-9, we had to complete a few object oriented programming (OOP) hacks that involved using attributes and objects (e.g. Class). This blog notes some of the important parts of the finished code I made and could be useful in making our written responses for the Create Performance Task.
categories: [extra]
title: OOP Hacks Explained
image: /images/python_image.jpg
comments: true
---


# What is OOP?

Object Oriented Programming (OOP) is a really useful way of allowing us to give one variable multiple properties. One way to think of this is programming a video game. If you wanted to create the villain or main character, you would want to assign them as an object, or "class". Within this class, you could give the objects multiple characteristics/attributes about themselves, such as their powers, intelligence, stamina, strengths, etc. Overall, OOP allows us to write code that is  cohesive and easier to follow. 


# Important Note #1: Defining the Class

This is the code segment that can be found at the very top of my finished hacks, shown below:

![image.png](attachment:image.png)

Although there is not a whole lot to look at from just this segment, there a few things worth noticing. For instance, if you look at all of the "self." lines, you will see how the periods are followed by an underscore. The underscore is there in order to make the variables used (arguments inside def_init_) protected to that one class. By doing this, if a user wishes to make more classes, they can continue to reuse the same variable with different elements as long as that variable is protected to each of those classes. If the underscore was not there, this would cause the definition of the variable to change, making the code very messy and unnecessarily complex.


# Setters and Getters

During the lecture, you may have heard the teacher discuss something about setters and getters being used in the code they showed. Here are some simple definitions for setters and getters:

Setter - Setters not only set the value of a attribute, but they also allow you to change or update the value of the attribute, if desired.
Getter - The definition is pretty much said in the name, but getters are what get the value of the attribute which was previously set by the setter.

Some of the code specifically involves the use of setters and getters, as shown below as an example:

![image.png](attachment:image.png)


# Output

If you took a close look at what was in the output, you may have noticed that an asterisk would appear next to a user's name, as shown below:

![image.png](attachment:image.png)

The asterisk is there to tell you that the computer has printed out the value of certain attributes for Chinmay. If I decided to pass u1 and u1's password as the parameters after users, then an asterisk would appear next to Emaad. 

# Conclusion

I really hope that this was helpful to people who are/were confused about these hacks even after completing them. I hope that this may be a helpful tool in making the written responses for the Create Performance Task, as knowing what your code does and being able to explain its functionality is a crucial skill for this class and beyond. 