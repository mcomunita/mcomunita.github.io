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
My [research](/research) lies at the intersection of human-computer interaction, machine learning, and audio signal processing. Specifically, I research human-centered machine listening and audio processing tools for creative expression with sound and understanding the acoustic world. 

I am currently a Research Assistant Professor in NYU’s [Department of Computer Science and Engineering](https://engineering.nyu.edu/academics/departments/computer-science-and-engineering) with affiliations to NYU’s [Music and Audio Research Lab](https://steinhardt.nyu.edu/marl/) and the [Center for Urban Science and Progress](http://cusp.nyu.edu/). I completed my PhD in computer science at Northwestern University as a member of the [Interactive Audio Lab](http://music.eecs.northwestern.edu/), and I hold a Master of Arts from Stanford University ([CCRMA](https://ccrma.stanford.edu/)) and a Bachelor of Music from Northwestern University.  Before my current position, I spent two years as a postdoctoral researcher in the Music and Audio Research Lab (MARL) at New York University (NYU). 

Starting in January 2021, I will be an Assistant Professor at NJIT's [Ying Wu College of Computing](https://computing.njit.edu/) in the Department of Informatics. I will be recruiting PhD students for Fall 2021.

News
-------
{% for post in site.posts limit:5  %}
  <a href="{{ post.url | relative_url }}" rel="permalink">{{ post.date | date: "%B %Y"}}</a> - {{ post.blurb }}
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