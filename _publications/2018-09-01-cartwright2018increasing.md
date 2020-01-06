---
layout: default-publication
title: "Increasing Drum Transcription Vocabulary Using Data Synthesis"
collection: publications
permalink: /publications/2018-09-01-cartwright2018increasing
abstract: "Current datasets for automatic drum transcription (ADT) are small and limited due to the tedious task of annotating onset events. While some of these datasets contain large vocabularies of percussive instrument classes (e.g. ~20 classes), many of these classes occur very infrequently in the data. This paucity of data makes it difficult to train models that support such large vocabularies. Therefore, data-driven drum transcription models often focus on a small number of percussive instrument classes (e.g. 3 classes). In this paper, we propose to support large-vocabulary drum transcription by generating a large synthetic dataset (210,000 eight second examples) of audio examples for which we have groundtruth transcriptions. Using this synthetic dataset along with existing drum transcription datasets, we train convolutional-recurrent neural networks (CRNNs) in a multi-task framework to support large-vocabulary ADT. We find that training on both the synthetic and real music drum transcription datasets together improves performance on not only large-vocabulary ADT, but also beat / downbeat detection small-vocabulary ADT."
date: 2018-09-01
venue: 'International Conference on Digital Audio Effects (DAFx)'
paperurl: '/files/cartwright2018increasing.pdf'
image: '/assets/images/cartwright2018increasing.png'
imagewidth: 100.0
presentation: '/files/cartwright2018increasing_presentation.pdf'
code: 'https://github.com/mcartwright/dafx2018_adt'
codename: 'Trained keras models'
categories: 
  - Sound Event Detection
  - Music Information Retrieval
citation: 'Cartwright, M., Bello, J.P. Increasing Drum Transcription Vocabulary Using Data Synthesis. In <i>Proceedings of the International Conference on Digital Audio Effects (DAFx)</i>, 2018.'
author_profile: true
---