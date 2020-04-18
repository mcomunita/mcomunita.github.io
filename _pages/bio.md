---
layout: single
permalink: /
author_profile: true
redirect_from: 
  - /bio/
  - /bio.html
  - /about/
  - /about.html
  - /home/
  - /home.html
---
I am Brooklyn-based computer scientist and musician. My [research](/research) lies at the intersection of human-computer interaction, machine learning, and audio signal processing. Specifically, I research human-centered machine listening and audio processing systems that enable new interactions for creative expression through sound and understanding the acoustic world at scale. 

I am currently a Research Assistant Professor in NYU’s [Department of Computer Science and Engineering](https://engineering.nyu.edu/academics/departments/computer-science-and-engineering) with affiliations to NYU’s [Music and Audio Research Lab](https://steinhardt.nyu.edu/marl/) and the [Center for Urban Science and Progress](http://cusp.nyu.edu/). I completed my PhD in computer science at Northwestern University as a member of the [Interactive Audio Lab](http://music.eecs.northwestern.edu/), and I hold a Master of Arts from Stanford University ([CCRMA](https://ccrma.stanford.edu/)) and a Bachelor of Music from Northwestern University.  Before my current position, I spent two years as a postdoctoral researcher in the Music and Audio Research Lab (MARL) at New York University (NYU). 

As a [musician](/music), I exercise my passion for low frequencies, enveloping noise, and textural sound using computers, synthesizers, and bass. With experimental-rock trio [volcano!](https://volcanoisaband.com/), I released albums on The Leaf Label and toured the United States and Europe.

News
-------
{% for post in site.posts limit:5  %}
  <b>{{ post.date | date: "%B %Y"}}</b> - {{ post.blurb }}
{% endfor %}


Current Affiliations
-------
* [Department of Computer Science and Engineering (CSE)](https://engineering.nyu.edu/academics/departments/computer-science-and-engineering)
* [Music and Audio Research Lab (MARL)](http://steinhardt.nyu.edu/marl/)
* [Center for Urban Science and Progress (CUSP)](http://cusp.nyu.edu/)
* [Sounds of New York City Project (SONYC)](http://wp.nyu.edu/sonyc)

Contact
-------
<address>
    Center for Urban Science and Progress<br />
    New York University<br />
    13th Floor<br />
    370 Jay Street<br />
    Brooklyn, NY 11201
</address>