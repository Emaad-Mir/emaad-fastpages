---
layout: post
description: A blog post demonstrating what happened when I tried to change the theme of my web page from minima to another supported theme.
categories: [markdown, week2]
title: My Attempt at Changing the Remote Theme
image: /images/dark-mode.jpg
---

By default, your web page has the theme minima as shown in the image below in config.yml:

![]({{site.baseurl}}/images/config-file.png "https://github.com/Emaad-Mir/emaad-fastpages")

The minima theme is okay, but I wanted to try something different to spice up my web page a little bit. I did this by looking for supported themes I could switch to and changing the jekyll theme from minima to hacker:

![]({{site.baseurl}}/images/theme-change.png "https://github.com/Emaad-Mir/emaad-fastpages")

However, when I went onto GitHub to see if my commit went through, I saw this error:

![]({{site.baseurl}}/images/fail.png "https://github.com/Emaad-Mir/emaad-fastpages")

I looked into the error, and it turned out that it involved something called Jekyll build. This was what the comment "Everything below here should be left alone. Modifications may break fastpages" was trying to warn me about. 

![]({{site.baseurl}}/images/comment.jpg "https://github.com/Emaad-Mir/emaad-fastpages")


I now realize that any changes that I try to implement into this area of the config.yml file, whether it is a theme change or something else, will result in the errors like the ones I experienced. 







