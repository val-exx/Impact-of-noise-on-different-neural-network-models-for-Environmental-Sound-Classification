# Noise Module

This folder contains the scripts used to generate, prepare, and analyze the noises used in the experiments.

The goal of this module is to provide a consistent and controlled way to create noisy audio signals for robustness evaluation.

---

## Files overview

### `signal_power.py`

This file contains utility functions to compute signal power.

Main functions:

* `compute_power(...)`: computes the average power of a signal in the time domain
* `bandpower(...)`: computes the power of a signal inside a selected frequency band using the periodogram
* `model_frequency_band(...)`: returns the frequency range associated with each model (`mn40as`, `htsat`, `tfnet`)

These functions are used to analyze both clean signals and noises and to ensure consistent comparisons in the relevant frequency ranges.

---

### `generate_colored_noise.py`

This script generates synthetic colored noises with different spectral properties.

Implemented noise types:

* white noise
* pink noise
* brownian noise
* blue noise
* violet noise

The generation is based on shaping the spectrum of white noise to obtain different frequency distributions.

These noises are used to simulate controlled perturbations during evaluation.

---

### `prepare_environmental_noises.py`

This script prepares real-world environmental noise recordings before they are used in the experiments.

Main operations:

* loading audio files
* trimming clips to a fixed duration
* applying offsets for specific cases (e.g. wind recordings)
* scaling amplitude using manually defined factors
* saving processed audio files

This ensures that all noise samples are consistent in duration and amplitude.

---

## Example usage

### Generate colored noise

```python
from src.noise.generate_colored_noise import generate_audio_noise

noise = generate_audio_noise(
    noise_type='pink',
    duration=5,
    sr=44100,
    noise_level=0.5
)
```

---

### Compute band power

```python
from src.noise.signal_power import bandpower, model_frequency_band

fmin, fmax = model_frequency_band('htsat')
power = bandpower(audio, fs=44100, fmin=fmin, fmax=fmax)
```

---

### Prepare environmental noises

```python
from src.noise.prepare_environmental_noises import prepare_noises

prepare_noises(
    input_path='raw_noises/',
    output_path='processed_noises/',
    sr=44100,
    duration=5.0
)
```

---

## Purpose of this module

The scripts in this folder support the noise pipeline of the project:

1. generate synthetic colored noises
2. prepare real-world environmental noise clips
3. compute and analyze signal/noise power
4. enable controlled noisy-audio creation for robustness evaluation

This module is a key part of the experimental setup, allowing a fair comparison of model performance under different noise conditions.

---


For a general overview of the project, refer to the main `README.md` in the root of the repository.
