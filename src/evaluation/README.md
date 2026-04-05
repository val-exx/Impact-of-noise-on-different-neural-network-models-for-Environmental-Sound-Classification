# Evaluation Module

This folder contains the scripts used to evaluate model performance under noisy conditions.

The goal of this module is to apply controlled noise to audio samples, run model inference, and compute performance metrics.

---

## Files overview

### `evaluate_noisy.py`

This script evaluates a model on noisy audio data.

Main operations:

* iterating over the dataset
* adding noise at different SNR levels
* running model inference
* collecting predictions and ground truth labels
* generating confusion matrices

This script represents the core evaluation pipeline of the project.

---

### `compute_confusion_matrix.py`

This file contains utility functions to compute and store confusion matrices.

Main functions:

* `compute_confusion_matrix(...)`: builds a confusion matrix from predictions and targets
* `save_confusion_matrix(...)`: saves the matrix to a text file

These matrices are later used for computing accuracy and visualization.

---

## Example usage

```python id="w7sx9o"
from src.evaluation.evaluate_noisy import evaluate_model_on_noisy_data

evaluate_model_on_noisy_data(
    model=my_model,
    dataset=my_dataset,
    noise_audio=my_noise,
    snr_list=[55, 45, 35, 25, 15, 5, -15, -25],
    output_dir="results/confusion_matrix/",
    model_name="htsat"
)
```

---

## Purpose of this module

The scripts in this folder define how model performance is evaluated under noise.

They enable:

1. controlled noise injection
2. consistent evaluation across models
3. generation of confusion matrices for further analysis

This module connects the dataset, noise generation, and visualization components of the project.

---


