# Visualization Module

This folder contains the scripts used to visualize the results of the experiments.

The goal of this module is to provide clear and interpretable representations of:

* how noise affects audio signals
* how model performance changes under different noise conditions

---

## Files overview

### `plot_noisy_spectrogram.py`

This script compares clean and noisy audio signals in the time-frequency domain.

Main operations:

* computing the STFT of clean and noisy signals
* converting amplitude to decibel scale
* plotting spectrograms using librosa

This visualization helps to understand how noise affects the structure of the signal across frequencies.

---

### `plot_confusion_matrix.py`

This script plots a confusion matrix starting from a saved text file.

Main operations:

* loading the confusion matrix from a `.txt` file
* converting it into a matrix format
* visualizing it as a heatmap using seaborn
* optionally saving the plot as an image

This visualization is useful to analyze class-level performance and identify misclassifications under specific noise conditions.

---

### `plot_accuracy_vs_snr.py`

This script plots model accuracy as a function of SNR (Signal-to-Noise Ratio) for a given noise type.

Main operations:

* reading confusion matrices from text files
* computing accuracy from each confusion matrix
* averaging results across folds
* plotting accuracy trends for multiple models

The script allows comparison between different architectures (e.g. CNN10, TFNet, mn40_as, HTS-AT) under varying noise levels.

---

## Example usage

### Plot clean vs noisy spectrogram

```python id="j33sdi"
from src.visualization.plot_noisy_spectrogram import plot_spectrogram_comparison

plot_spectrogram_comparison(
    audio=clean_audio,
    noisy_audio=noisy_audio,
    sr=44100,
    n_fft=1024,
    hop_length=320
)
```

---

### Plot confusion matrix

```python id="jnh5sj"
from src.visualization.plot_confusion_matrix import plot_confusion_matrix

plot_confusion_matrix(
    file_path="noise_white_SNR_-25_fold_1.txt",
    model="HTS_AT",
    noise="white",
    SNR=-25,
    save_path="cm_white_-25.png"
)
```

---

### Plot accuracy vs SNR

```python id="d7csj6"
from src.visualization.plot_accuracy_vs_snr import plot_accuracy_vs_snr

plot_accuracy_vs_snr(
    noise="white",
    input_path="path/to/results",
    save_path="accuracy_vs_snr_white.png"
)
```

---

## Purpose of this module

The scripts in this folder are used to visually analyze the impact of noise on both signals and model performance.

They support:

1. qualitative analysis of noisy audio signals
2. inspection of class-level errors through confusion matrices
3. comparison of model robustness across different SNR levels

These visualizations are essential to interpret the experimental results and validate the robustness analysis.

---


