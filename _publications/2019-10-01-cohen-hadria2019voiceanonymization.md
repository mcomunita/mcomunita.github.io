---
layout: default-publication
title: "Voice Anonymization in Urban Sound Recordings"
collection: publications
permalink: /publications/2019-10-01-cohen-hadria2019voiceanonymization
abstract: "Monitoring health and noise pollution in urban environments often entails deploying acoustic sensor networks to passively collect data in public spaces. Although spaces are technically public, people in the environment may not fully realize the degree to which they may be recorded by the sensor network, which may be perceived as a violation of expected privacy. Therefore, we propose a method to anonymize and blur the voices of people recorded in public spaces &#8212; a novel, yet increasingly important task as acoustic sensing becomes ubiquitous in sensor-equipped smart cities. This method is analogous to Google&apos;s face blurring in its Street View photographs, which arose from similar concerns in the visual domain. The proposed blurring method aims to anonymize voices by removing both the linguistic content and personal identity from voices, while preserving the rest of the acoustic scene.\n\n The method consists of a three-step process. First, voices are separated from non-voice content by a deep U-Net source separation model. Second, we evaluate two approaches to obscure the identity and intelligibility of the extracted voices: a low pass filter to remove most of the formants in the voices, and an inversion of Mel-Frequency Cepstral Coefficients (MFCC). Finally, the blurred vocal content is mixed with the separated non-vocal signal to reconstruct the acoustic scene. Using background recordings from a real urban acoustic sensor network in New York City, we present a complete evaluation of our method, with automatic speech recognition, speaker identification, sound event detection, and human perceptual evaluation."
date: 2019-10-01
venue: 'IEEE International Workshop on Machine Learning for Signal Processing (MLSP)'
paperurl: '/files/cohen-hadria2019voiceanonymization.pdf'
image: '/assets/images/cohen-hadria2019voiceanonymization.png'
imagealign: left
imagewidth: 50.0
categories: 
  - Sound Event Detection
citation: 'Cohen-Hadria, A., Cartwright, M., McFee, B., Bello, J.P. Voice Anonymization in Urban Sound Recordings. In <i>Proceedings of the IEEE International Workshop on Machine Learning for Signal Processing (MLSP)</i>, 2019.'
author_profile: true
---