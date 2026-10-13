---
layout: archive
title: "Personal"
permalink: /personal/
author_profile: true
---

In addition to economics, I've gotten to do a lot of other fun things. I grew up in Lubbock, TX, where my parents owned and operated [Joyland Amusement Park](https://en.wikipedia.org/wiki/Joyland_Amusement_Park). I played golf competitively during my high school and undergrad years, and still play recreationally (current handicap: 2.1). Additionally, while in undergrad, I spent a semester in Washington DC interning for the Cato Institute thanks to the LCU Honors College. In my free time, I like to play golf and basketball, watch sports (go Mavs! go Cowboys!), and just be a [fun guy](https://www.youtube.com/watch?v=zIwh0njInPk&ab_channel=Ball).


<link rel="stylesheet" href="{{ '/assets/css/personal-gallery.css' | relative_url }}">

<div class="personal-gallery">
{% for photo in site.data.personal_photos %}
  <figure class="personal-gallery__item">
    <a href="{{ '/images/personal/' | append: photo.file | relative_url }}" aria-label="{{ photo.alt | escape }} — view full-size photo">
      <img src="{{ '/images/personal/' | append: photo.file | relative_url }}" alt="{{ photo.alt | escape }}" loading="lazy" decoding="async">
    </a>
    {% if photo.caption and photo.caption != '' %}<figcaption>{{ photo.caption | escape }}</figcaption>{% endif %}
  </figure>
{% endfor %}
</div>
