---
layout: single
classes: 
  - wide
title: "Publications"
permalink: /publications/
author_profile: true
---

{% assign postsByYear = site.publications | group_by_exp: 'post', 'post.date | date: "%Y"' %}
{% for year in postsByYear reversed %}
  <section id="{{ year.name }}" class="taxonomy__section">
    <h2 class="archive__subtitle">{{ year.name }}</h2>
    <div class="small entries-{{ page.entries_layout | default: 'list' }}">
      {% for post in year.items reversed %}
        <p class="archive__item-excerpt" itemprop="description">
          <a href="{{ post.paperurl }}"><i class="fas fa-fw fa-file-pdf" aria-hidden="true"></i></a>
          <a href="{{ post.permalink }}" style="text-decoration:none;">
          {{ post.citation }} </a>
        </p>
      {% endfor %}
    </div>
  </section>
{% endfor %}