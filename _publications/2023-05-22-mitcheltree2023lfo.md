---
layout        : default-publication
title         : "Modulation Extraction for LFO-driven Audio Effects"
collection    : publications
permalink     : /publications/2023-05-22-mitcheltree2023lfo

abstract      : "Low frequency oscillator (LFO) driven audio effects such as phaser, flanger, and chorus, modify an input signal using time-varying filters and delays, resulting in characteristic sweeping or widening effects. It has been shown that these effects can be modeled using neural networks when conditioned with the ground truth LFO signal. However, in most cases, the LFO signal is not accessible and measurement from the audio signal is nontrivial, hindering the modeling process. To address this, we propose a framework capable of extracting arbitrary LFO signals from processed audio across multiple digital audio effects, parameter settings, and instrument configurations. Since our system imposes no restrictions on the LFO signal shape, we demonstrate its ability to extract quasiperiodic, combined, and distorted modulation signals that are relevant to effect modeling. Furthermore, we show how coupling the extraction model with a simple processing network enables training of end-to-end black-box models of unseen analog or digital LFO-driven audio effects using only dry and wet audio pairs, overcoming the need to access the audio effect or internal LFO signal. We make our code available and provide the trained audio effect models in a real-time VST plugin."

date            : 2023-05-05
venue           : 'DAFX 2023 - International Conference on Digital Audio Effects (DAFx23)'
paperurl        : '/files/mitcheltree2023lfo-paper.pdf'
image           : '/files/mitcheltree2023lfo-image.png'
imagewidth      : 80.0
poster          : 
presentation    : 
code            : 'https://github.com/christhetree/mod_extraction'
codename        : 'https://github.com/christhetree/mod_extraction'
data            : 
dataname        : 
webpage         : 'https://christhetr.ee/mod_extraction/'
webpagename     : 'https://christhetr.ee/mod_extraction/'
categories      : 
citation        : 'Mitcheltree, C., Steinmetz, C. J., Comunità, M., Reiss, J. D. <b>"Modulation Extraction for LFO-driven Audio Effects"</b> - <i>arXiv preprint arXiv:2305.13262</i>'
author_profile  : true
---