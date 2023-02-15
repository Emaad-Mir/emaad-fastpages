---
toc: true
layout: post
description: This blog goes over what we have done so far for the CPT as well as the plans for the future (for N@TM tomorrow!)
categories: [extra]
title: CPT Progress Check 2
image: /images/college-board-logo.png
comments: true
---

# Overview of This Blog

Around last week, I made the first blog that documented our team's progress. With N@TM getting closer, below is how much farther we have come in terms of tangibles, what we have accomplished, problems we still have, and much more. 

## Words API

For my part of the project, I decided to implement a words api that I found online so that each round, a list of 10 random words is generated with one word being randomly picked from that list. The word that is picked is the word that the user will have to guess in 7 lives. Below is the code for the API, as well as what it looks like in the backend view of our project:

![]({{site.baseurl}}/images/codeforapi.png "https://github.com/Emaad-Mir/emaad-fastpages")

![]({{site.baseurl}}/images/wordgen.png "https://github.com/Emaad-Mir/emaad-fastpages")

As you can see, at the end of the url is "?number=10", which indicates that we are requesting the link to choose a list of 10 random words. One of these words will then be randomly chosen from the list created, and that will be what the user has to guess.

## Subdomain Creation + Nginx Message

Originally, I believed that we were supposed to use freenom in order to create our DNS; however, a fellow CSP student sent a link to an alternative method called www.duckdns.org, which was a relief considering the fact that Freenom tends to not be consistent in when it does and does not work. I named our subdomain gamesarcade, as shown below, and upon copying and pasting the link into the web browser, the nginx welcome message shows up. Both images described are shown below:

![]({{site.baseurl}}/images/nginx.png "https://github.com/Emaad-Mir/emaad-fastpages")

![]({{site.baseurl}}/images/duckdns.png "https://github.com/Emaad-Mir/emaad-fastpages")


## GET/POST Methods

As you may recall, a few weeks ago, we had to use postman to test our APIs, and the images below show me doing just that. When I add another item (game) with the four attributes (name, desc, date, link), it adds another row to the Flask table that I created, which is what connects the frontend and backend. This is connecting the two because by adding a link attribute, the user can click on the github.io link from the backend site on to the frontend site with all of the games. 

![]({{site.baseurl}}/images/postmanaddget.png "https://github.com/Emaad-Mir/emaad-fastpages")

![]({{site.baseurl}}/images/addingentrie.png "https://github.com/Emaad-Mir/emaad-fastpages")


## Issues with AWS

While our group has made a lot more progress on our project compared to last week, we still have a couple of problems that are ongoing, including the fact that the curl command does not work for our API. Below are some of the various error messages that I received whenever I tried to curl the link with our assigned port number 8034:

![]({{site.baseurl}}/images/curlerror.png "https://github.com/Emaad-Mir/emaad-fastpages")

Furthermore, while I don't have images of this specific error, I also would have an error which would tell me that there was an internal server error whenever I tried to use curl. I would also sometimes get that the connection was reset by a peer, and I tried looking up solutions to both of these when each error was presented to me. I tried many different combinations of ports and checked to make sure that I was doing everything right. Not only that, but I even checked into other teams' files to see if we were doing it right, and it looked to me that we were doing everything exactly the same, yet somehow curl only worked for them and not us. I hope that today, we will be able to find a solution to this issue and that Mr. Yeung will know what to do when we tell him that the problem is persisting. 


## Frontend problem 

I am also having an issue with my frontend portion of the project, and it involves something within my initHangman function, shown below:

![]({{site.baseurl}}/images/frontenderror.png "https://github.com/Emaad-Mir/emaad-fastpages")

I have tried various solutions online, but none have helped me so far. I hope to figure out why this is happening soon and that our group will be fully prepared for N@TM. 