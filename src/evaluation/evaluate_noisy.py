import os
import numpy as np

from src.noise.signal_power import bandpower, model_frequency_band
# from src.noise.snr_mixer import mix_noise_at_snr   (se lo aggiungiamo dopo)
from src.evaluation.compute_confusion_matrix import compute_confusion_matrix, save_confusion_matrix


def evaluate_model_on_noisy_data(
    model,
    dataset,
    noise_audio,
    snr_list,
    output_dir,
    model_name='model'
):
    """
    model: object with predict(audio) method
    dataset: list of dicts -> {"waveform": ..., "target": ...}
    noise_audio: array
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    fmin, fmax = model_frequency_band(model_name)

    for snr in snr_list:
        y_true = []
        y_pred = []

        for sample in dataset:
            audio = sample["waveform"]
            target = sample["target"]

            # TODO: sostituire con funzione tua (colored / snr mixer)
            noisy_audio = audio  # placeholder

            pred = model.predict(noisy_audio)

            y_true.append(target)
            y_pred.append(pred)

        cm = compute_confusion_matrix(y_true, y_pred)

        file_name = "noise_SNR_{}.txt".format(snr)
        save_path = os.path.join(output_dir, file_name)

        save_confusion_matrix(cm, save_path)
