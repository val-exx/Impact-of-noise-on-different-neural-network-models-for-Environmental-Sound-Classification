
# Data Module

This folder contains the script used to prepare the dataset for the experiments.

The goal of this module is to create a consistent and reproducible dataset starting from ESC-50.

---

## Files overview

### `prepare_esc20_dataset.py`

This script creates a reduced version of the ESC-50 dataset by selecting a subset of classes and preparing the data for model training and evaluation.

Main operations:

* reading ESC-50 metadata (`esc50.csv`)
* selecting a subset of classes (mapped to 19 categories)
* remapping original labels to a new label space
* resampling all audio files to a fixed sampling rate (32 kHz)
* organizing samples into folds (based on the original ESC-50 split)
* storing the processed dataset in a `.npy` file

Each sample is stored as a dictionary containing:

* `name`: file name
* `target`: remapped class label
* `waveform`: audio signal

---

## Example usage

```python id="1u2g7v"
from src.data.prepare_esc20_dataset import prepare_esc20_dataset

prepare_esc20_dataset(
    dataset_path="path/to/ESC-50",
    resample_path="path/to/resampled_audio",
    output_path="path/to/output/esc20.npy"
)
```

---

## Purpose of this module

This script defines the dataset used in all experiments.

It ensures:

1. consistent class selection
2. fixed sampling rate
3. correct cross-validation splits

This preprocessing step is essential to make the experiments reproducible and comparable across different models.

---

## Project structure

This module is part of a larger pipeline:

* `src/data/` → dataset preparation
* `src/noise/` → noise generation and processing
* `src/evaluation/` → model evaluation under noise

For a general overview of the project, refer to the main `README.md` in the root of the repository.
