import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn

def get_noise_title(noise):
    if noise == 'ambience':
        noise_title = 'TV'
    elif noise == 'domestic':
        noise_title = 'Door'
    elif noise == 'pet':
        noise_title = 'Dog'
    elif noise == 'urban':
        noise_title = 'Car engine'
    elif noise == 'weather':
        noise_title = 'Rain'
    else:
        noise_title = noise
    return noise_title

def plot_confusion_matrix(file_path, model, noise, SNR, save_path=None):
    data = np.loadtxt(file_path)

    class_names = ['18', '20', '21', '22', '23', '24',
                   '25', '26', '27', '28', '29', '30',
                   '31', '32', '34', '35', '36', '37', '39']

    df_cm = pd.DataFrame(
        data,
        index=[classs for classs in class_names],
        columns=[classs for classs in class_names]
    )

    plt.figure(figsize=(10, 7))
    sn.set(font_scale=1)
    sn.heatmap(df_cm, annot=True, annot_kws={"size": 15}, cmap=plt.cm.Blues)

    plt.xlabel('Predicted label')
    plt.ylabel('True label')

    noise_title = get_noise_title(noise)
    plt.title('Confusion Matrix {}, {} Noise, SNR {} dB'.format(model, noise_title.capitalize(), SNR))

    if save_path is not None:
        plt.savefig(save_path, bbox_inches='tight')

    plt.show()


if __name__ == '__main__':
    model = 'HTS_AT'
    noise = 'white'
    SNR = -25

    file_path = 'noise_{}_SNR_{}_fold_1.txt'.format(noise, SNR)
    save_path = '{}_{}_{}dB.png'.format(model, noise, SNR)

    plot_confusion_matrix(file_path, model, noise, SNR, save_path=save_path)
