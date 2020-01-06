---
layout: single
classes: 
  - wide
title: "Sound Event Detection"
permalink: /publications/sound-event-detection
author_profile: true
taxonomy: Sound Event Detection
---

<section class="taxonomy__section">
{% for post in site.publications %}
  {% if post.categories contains page.taxonomy %}
      <div class="small entries-{{ page.entries_layout | default: 'list' }}">
          <p class="archive__item-excerpt" itemprop="description">
            <a href="{{ post.paperurl }}"><i class="fas fa-fw fa-file-pdf" aria-hidden="true"></i></a>
            <a href="{{ post.permalink }}" style="text-decoration:none;">
            {{ post.citation }} </a>
          </p>
      </div>
  {% endif %}
{% endfor %}
</section>