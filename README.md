# Impact of Noise on Neural Network Architectures for Environmental Sound Classification

## 📌 Overview

This repository contains the code and experimental pipeline developed for my Master's thesis at Politecnico di Torino.

The project investigates how different deep learning architectures behave under noisy conditions in environmental sound classification tasks. The goal is to evaluate **model robustness to noise** and identify which architectural choices improve performance in real-world scenarios.

## ❓ Research Question

How does background noise affect the robustness of different neural network architectures for environmental sound classification?

## 🚀 Key Contributions

* Comparative analysis of **CNN-based and Transformer-based models**
* Evaluation under multiple noise conditions:

  * Colored noise (white, pink, red, blue, violet)
  * Real-world environmental noise (e.g., TV, rain, dog, door, engine)
* Performance analysis across different **SNR levels**
* Robustness evaluation using:

  * Accuracy vs SNR curves
  * Confusion matrices
  * Spectral analysis (PSD)

## 🧠 Models Compared

* **CNN10** (PANNs-based)
* **TFNet** (Time-Frequency Attention)
* **mn40_as** (MobileNetV3 + Knowledge Distillation from PaSST)
* **HTS-AT** (Hierarchical Transformer with attention mechanisms)

## 📊 Dataset

* Based on **ESC-50**
* Reduced to **19 selected classes** (focused on domestic and human-related sounds)
* Additional **unseen test set** collected for robustness evaluation

> ⚠️ Dataset is not included. Please download ESC-50 from the official source and place it in `data/raw/`.

## ⚙️ Project Structure

```
├── src/                # Core code (models, training, evaluation)
├── configs/            # Experiment configurations
├── data/               # Dataset structure (not included)
├── notebooks/          # Analysis and visualization
├── results/            # Outputs (figures, tables)
├── docs/               # Thesis and additional documentation
└── scripts/            # Reproducibility scripts
```

## 🔬 Methodology

The experimental pipeline consists of:

1. **Feature Extraction**

   * Log-Mel Spectrograms (via STFT)

2. **Training**

   * Models trained/fine-tuned on ESC-50
   * Cross-validation using predefined folds

3. **Noise Injection**

   * Controlled addition of noise at different SNR levels
   * Both synthetic (colored) and real-world noise

4. **Evaluation**

   * Clean vs noisy inference comparison
   * Robustness analysis across noise types and intensities

## 📈 Results (Highlights)

* Transformer-based models (e.g., HTS-AT) show **higher robustness to noise**
* Pretraining and attention mechanisms significantly improve performance
* CNN-based models degrade faster at low SNR levels

## ▶️ Reproducibility

### Install dependencies

```bash
pip install -r requirements.txt
```

### Train a model

```bash
python -m src.training.train --config configs/cnn10.yaml
```

### Evaluate with noise

```bash
python -m src.evaluation.evaluate_noisy --config configs/experiment_main.yaml
```

## 📷 Example Outputs

* Accuracy vs SNR plots
* Spectrogram comparisons (clean vs noisy)
* Confusion matrices under extreme noise conditions

## 📄 Thesis

Full thesis available here:
👉 `docs/thesis.pdf`

## 🛠️ Technologies

* Python
* PyTorch
* torchaudio
* NumPy / SciPy
* Matplotlib

## 📬 Contact

If you have questions or want to discuss the project, feel free to reach out.

---

⭐ If you find this project useful, consider giving it a star!
