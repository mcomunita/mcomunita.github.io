---
layout: default-publication
title: "Per-Channel Energy Normalization: Why and How"
collection: publications
permalink: /publications/2019-01-01-lostanlen2019perchannel
abstract: "In the context of automatic speech recognition and acoustic event detection, an adaptive procedure named perchannel energy normalization (PCEN) has recently shown to outperform the pointwise logarithm of mel-frequency spectrogram (logmelspec) as an acoustic frontend. This article investigates the adequacy of PCEN for spectrogram-based pattern recognition in far-field noisy recordings, both from theoretical and practical standpoints. First, we apply PCEN on various datasets of natural acoustic environments and find empirically that it Gaussianizes distributions of magnitudes while decorrelating frequency bands. Secondly, we describe the asymptotic regimes of each component in PCEN: temporal integration, gain control, and dynamic range compression. Thirdly, we give practical advice for adapting PCEN parameters to the temporal properties of the noise to be mitigated, the signal to be enhanced, and the choice of time-frequency representation. As it converts a large class of real-world soundscapes into additive white Gaussian noise (AWGN), PCEN is a computationally efficient frontend for robust detection and classification of acoustic events in heterogeneous environments."
date: 2019-01-01
venue: 'IEEE Signal Processing Letters'
paperurl: '/files/lostanlen2019perchannel.pdf'
categories: 
  - Sound Event Detection
citation: 'Lostanlen, V., Salamon, J., Cartwright, M., McFee, B., Farnsworth, A., Kelling, S., Bello, J.P. Per-Channel Energy Normalization: Why and How. In <i>IEEE Signal Processing Letters</i>, vol. 26(1), 2019, pp. 39-43.'
author_profile: true
---