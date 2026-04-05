
import os
import numpy as np
import librosa
from pydub import AudioSegment

def associate(label_old):
    label_new = ''

    if label_old == '18':
        label_new = 0
    elif label_old == '20':
        label_new = 1
    elif label_old == '21':
        label_new = 2
    elif label_old == '22':
        label_new = 3
    elif label_old == '23':
        label_new = 4
    elif label_old == '24':
        label_new = 5
    elif label_old == '25':
        label_new = 6
    elif label_old == '26':
        label_new = 7
    elif label_old == '27':
        label_new = 8
    elif label_old == '28':
        label_new = 9
    elif label_old == '29':
        label_new = 10
    elif label_old == '30':
        label_new = 11
    elif label_old == '31':
        label_new = 12
    elif label_old == '32':
        label_new = 13
    elif label_old == '34':
        label_new = 14
    elif label_old == '35':
        label_new = 15
    elif label_old == '36':
        label_new = 16
    elif label_old == '37':
        label_new = 17
    elif label_old == '39':
        label_new = 18

    return label_new

def prepare_esc20_dataset(dataset_path, resample_path, output_path):
    meta_path = os.path.join(dataset_path, "meta", "esc50.csv")
    audio_path = os.path.join(dataset_path, "audio")

    meta = np.loadtxt(meta_path, delimiter=',', dtype='str', skiprows=1)
    audio_list = os.listdir(audio_path)

    if not os.path.exists(resample_path):
        os.makedirs(resample_path)

    for f in audio_list:
        full_f = os.path.join(audio_path, f)
        resample_f = os.path.join(resample_path, f)
        sound = AudioSegment.from_file(full_f)
        sound = sound.set_frame_rate(32000)
        sound.export(resample_f, format="wav")

    output_dict = [[] for _ in range(5)]

    for label in meta:
        name = label[0]
        fold = label[1]
        target = associate(label[2])

        y, sr = librosa.load(os.path.join(resample_path, name), sr=None)

        output_dict[int(fold) - 1].append(
            {
                "name": name,
                "target": int(target),
                "waveform": y
            }
        )

    np.save(output_path, output_dict)
