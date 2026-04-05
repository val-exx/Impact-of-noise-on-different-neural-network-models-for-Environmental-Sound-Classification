# Source Code Overview

This folder contains the core source code of the project.

The code is organized into modules that reflect the main steps of the experimental pipeline used in the thesis.

---

## Folder structure

### `data/`

This module contains the dataset preparation script.

Main purpose:

* preparing a reduced version of ESC-50
* remapping labels
* resampling audio files
* organizing the data into folds

Main file:

* `prepare_esc20_dataset.py`

---

### `noise/`

This module contains the scripts used to generate, prepare, and analyze noises.

Main purpose:

* generating synthetic colored noises
* preparing real-world environmental noises
* computing signal and noise power
* supporting controlled noisy-audio generation

Main files:

* `signal_power.py`
* `generate_colored_noise.py`
* `prepare_environmental_noises.py`

---

### `visualization/`

This module contains the scripts used to visualize both signals and results.

Main purpose:

* comparing clean and noisy spectrograms
* plotting confusion matrices
* plotting accuracy as a function of SNR

Main files:

* `plot_noisy_spectrogram.py`
* `plot_confusion_matrix.py`
* `plot_accuracy_vs_snr.py`

---

### `evaluation/`

This module contains the scripts used to evaluate models under noisy conditions.

Main purpose:

* applying controlled noise
* running inference
* computing confusion matrices
* supporting robustness evaluation

Main files:

* `evaluate_noisy.py`
* `compute_confusion_matrix.py`

---

### `demo_pipeline.py`

This script provides a simple end-to-end example of the project workflow.

Main steps:

1. load an audio file
2. generate synthetic noise
3. mix signal and noise
4. visualize clean and noisy spectrograms
5. run a placeholder model prediction
6. compute a simple confusion matrix

This file is intended as a compact demonstration of how the different modules connect to each other.

---

## Purpose of the `src/` folder

The `src/` folder contains the technical core of the repository.

It implements the main components of the project:

* dataset preparation
* noise generation and processing
* visualization of signals and results
* evaluation under noisy conditions

Together, these modules define the pipeline used to study the robustness of different audio classification models under background noise.

---

## Suggested reading order

For a quick understanding of the codebase, the recommended order is:

1. `data/prepare_esc20_dataset.py`
2. `noise/generate_colored_noise.py`
3. `noise/prepare_environmental_noises.py`
4. `evaluation/evaluate_noisy.py`
5. `visualization/plot_noisy_spectrogram.py`
6. `visualization/plot_accuracy_vs_snr.py`
7. `demo_pipeline.py`

---

