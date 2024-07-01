---
layout        : default-publication
title         : "SpecMaskGIT: Masked Generative Modeling of Audio Spectrograms for Efficient Audio Synthesis and Beyond"
collection    : publications
permalink     : /publications/2024-06-26-comunita2023specmaskgit

abstract      : "Recent advances in generative models that iteratively synthesize audio clips sparked great success to text-to-audio synthesis (TTA), but with the cost of slow synthesis speed and heavy computation. Although there have been attempts to accelerate the iterative procedure, high-quality TTA systems remain inefficient due to hundreds of iterations required in the inference phase and large amount of model parameters. To address the challenges, we propose SpecMaskGIT, a light-weighted, efficient yet effective TTA model based on the masked generative modeling of spectrograms. First, SpecMaskGIT synthesizes a realistic 10s audio clip by less than 16 iterations, an order-of-magnitude less than previous iterative TTA methods. As a discrete model, SpecMaskGIT outperforms larger VQ-Diffusion and auto-regressive models in the TTA benchmark, while being real-time with only 4 CPU cores or even 30x faster with a GPU. Next, built upon a latent space of Mel-spectrogram, SpecMaskGIT has a wider range of applications (e.g., the zero-shot bandwidth extension) than similar methods built on the latent wave domain. Moreover, we interpret SpecMaskGIT as a generative extension to previous discriminative audio masked Transformers, and shed light on its audio representation learning potential. We hope our work inspires the exploration of masked audio modeling toward further diverse scenarios."

date            : 2024-06-26
venue           : 'ISMIR 2024'
paperurl        : '/files/comunita2024specmaskgit-paper.pdf'
image           : '/files/comunita2024specmaskgit-image.png'
imagewidth      : 100.0
poster          : 
presentation    : 
code            : 
codename        : 
data            : 
dataname        : 
webpage         : 'https://zzaudio.github.io/SpecMaskGIT/index.html'
webpagename     : 'https://zzaudio.github.io/SpecMaskGIT/index.html'
categories      : 
citation        : 'Comunità, M., Zhong, Z., Takahashi, A., Yang, S., Zhao, M., Saito, K., Ikemiya, Y., Shibuya, T., Takahashi, S., Mitsufuji, Y.<b>"SpecMaskGIT: Masked Generative Modeling of Audio Spectrograms for Efficient Audio Synthesis and Beyond"</b> - <i>International Society for Music Information Retrieval Conference. ISMIR 2024.</i>'
author_profile  : true
---