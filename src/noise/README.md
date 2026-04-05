# Noise Module

This folder contains the scripts used to prepare, generate and analyze the noises employed in the thesis experiments on environmental sound classification under noisy conditions.

## Files overview

### `signal_power.py`

This file contains utility functions to compute signal power.

Main functions:

* `compute_power(...)`: computes the average power of a signal in the time domain
* `bandpower(...)`: computes the power of a signal inside a selected frequency band using the periodogram
* `model_frequency_band(...)`: returns the frequency range associated with each model (`mn40as`, `htsat`, `tfnet`)

This code is useful to measure both clean signals and noises and to make comparisons in the frequency bands that are relevant for each model.

---

### `generate_colored_noise.py`

This file is used to generate synthetic colored noises.

Implemented noise types:

* white noise
* pink noise
* brownian noise
* blue noise
* violet noise

The generation is based on shaping the spectrum of white noise so that different spectral distributions are obtained.
This script is useful to create the artificial noises used in the robustness analysis.

---

### `prepare_environmental_noises.py`

This file is used to prepare real-world environmental noises before using them in the experiments.

Main operations:

* loading audio files
* cutting clips to a fixed duration
* applying an offset for specific files when needed
* scaling the noise amplitude with manually selected factors
* saving the processed audio files

This script was used to obtain consistent noise clips from external recordings before mixing them with target sounds.

---

## Purpose of this folder

Overall, the scripts in this folder support the noise preparation pipeline of the project:

1. generate synthetic colored noises
2. prepare real-world noise clips
3. compute and compare signal/noise power
4. support controlled noisy-audio creation for robustness evaluation
