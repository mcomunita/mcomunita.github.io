---
layout        : default-publication
title         : "Modelling black-box audio effects with time-varying feature modulation"
collection    : publications
permalink     : /publications/2023-05-05-comunita2022gcntfilm

abstract      : "Deep learning approaches for black-box modelling of audio effects have shown promise, however, the majority of existing work focuses on nonlinear effects with behaviour on relatively short time-scales, such as guitar amplifiers and distortion. While recurrent and convolutional architectures can theoretically be extended to capture behaviour at longer time scales, we show that simply scaling the width, depth, or dilation factor of existing architectures does not result in satisfactory performance when modelling audio effects such as fuzz and dynamic range compression. To address this, we propose the integration of time-varying feature-wise linear modulation into existing temporal convolutional backbones, an approach that enables learnable adaptation of the intermediate activations. We demonstrate that our approach more accurately captures long-range dependencies for a range of fuzz and compressor implementations across both time and frequency domain metrics. We provide sound examples, source code, and pretrained models to faciliate reproducibility"

date            : 2023-05-05
venue           : 
paperurl        : '/files/comunita2023gcntfilm-paper.pdf'
image           : '/files/comunita2022gcntfilm-image.png'
imagewidth      : 80.0
poster          : 
presentation    : 
code            : 'https://github.com/mcomunita/gcn-tfilm'
codename        : 'https://github.com/mcomunita/gcn-tfilm'
data            : 'https://zenodo.org/record/7271558#.Y2vIxezP0-R'
dataname        : 'dataset'
webpage         : 'https://mcomunita.github.io/gcn-tfilm_page/'
webpagename     : 'https://mcomunita.github.io/gcn-tfilm_page/'
categories      : 
citation        : 'Comunità, M., Steinmetz, C. J, Phan, H., Reiss, J. D. <b>"Modelling Black-box Audio Effects with Time-varying Feature Modulation"</b> - <i>ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing</i>'
author_profile  : true
---