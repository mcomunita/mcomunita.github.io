---
layout: default-publication
title: "Scaper: A Library for Soundscape Synthesis and Augmentation"
collection: publications
permalink: /publications/2017-10-01-salamon2017scaper
abstract: "Sound event detection (SED) in environmental recordings is a key topic of research in machine listening, with applications in noise monitoring for smart cities, self-driving cars, surveillance, bioacoustic monitoring, and indexing of large multimedia collections. Developing new solutions for SED often relies on the availability of strongly labeled audio recordings, where the annotation includes the onset, offset and source of every event. Generating such precise annotations manually is very time consuming, and as a result existing datasets for SED with strong labels are scarce and limited in size. To address this issue, we present Scaper, an open-source library for soundscape synthesis and augmentation. Given a collection of isolated sound events, Scaper acts as a high-level sequencer that can generate multiple soundscapes from a single, probabilistically defined, &#8220;specification&#8221;. To increase the variability of the output, Scaper supports the application of audio transformations such as pitch shifting and time stretching individually to every event. To illustrate the potential of the library, we generate a dataset of 10,000 soundscapes and use it to compare the performance of two state-of-the-art algorithms, including a breakdown by soundscape characteristics. We also describe how Scaper was used to generate audio stimuli for an audio labeling crowdsourcing experiment, and conclude with a discussion of Scaper&#8217;s limitations and potential applications."
date: 2017-10-01
venue: 'IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (WASPAA)'
paperurl: '/files/salamon2017scaper.pdf'
image: '/assets/images/scaper.png'
imagewidth: 50.0
code: 'https://github.com/justinsalamon/scaper'
codename: 'Scaper'
data: 'http://urbansed.weebly.com/'
dataname: 'URBAN-SED dataset'
categories: 
  - Sound Event Detection
citation: 'Salamon, J., MacConnell, D., Cartwright, M., Li, P., Bello, J.P. Scaper: A Library for Soundscape Synthesis and Augmentation. In <i>Proceedings of the IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (WASPAA)</i>, 2017.'
author_profile: true
---