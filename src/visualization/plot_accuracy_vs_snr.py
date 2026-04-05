import os
import numpy as np
import matplotlib.pyplot as plt

def get_acc_from_matrix(confusion_matrix):
    array = np.zeros((19, 19))

    for row_list, row in zip(confusion_matrix, range(19)):
        values = row_list.split(' ')
        values = [value for value in values if value != '']
        for value, column in zip(values, range(19)):
            array[row, column] = int(float(value))

    accuracy = np.sum(np.diag(array)) / np.sum(array)
    return accuracy

def get_mean_accuracy_for_model_noise(model, noise, SNRs, folds, input_path):
    mean_accs = []

    for SNR in SNRs:
        fold_accs = []

        for fold in folds:
            if model == 'TFNet' or model == 'CNN10':
                snr_str = str(float(SNR))
            else:
                snr_str = str(SNR)

            if noise == 'pet':
                file_name = 'noise_{}_SNR_{}_fold_{}.txt'.format(noise, snr_str, fold)
            else:
                file_name = 'noise_{}_SNR_{}_fold_{}.txt'.format(noise, snr_str, fold)

            file_path = os.path.join(input_path, model, 'confusion_matrix', file_name)

            if not os.path.exists(file_path):
                continue

            with open(file_path, 'r') as f:
                lines = f.read().split('\n')

            lines = [line for line in lines if line.strip() != '']
            acc = get_acc_from_matrix(lines)
            fold_accs.append(acc)

        if len(fold_accs) > 0:
            mean_accs.append(np.mean(fold_accs))
        else:
            mean_accs.append(np.nan)

    return mean_accs

def plot_accuracy_vs_snr(noise, input_path, save_path=None):
    models = ['CNN10', 'TFNet', 'mn40_as', 'HTS_AT']
    folds = [1, 2, 3, 4, 5]

    SNRs = [55, 45, 35, 25, 15, 5, -15, -25]

    cnn10_acc = get_mean_accuracy_for_model_noise('CNN10', noise, SNRs, folds, input_path)
    tfnet_acc = get_mean_accuracy_for_model_noise('TFNet', noise, SNRs, folds, input_path)
    mn40as_acc = get_mean_accuracy_for_model_noise('mn40_as', noise, SNRs, folds, input_path)
    htsat_acc = get_mean_accuracy_for_model_noise('HTS_AT', noise, SNRs, folds, input_path)

    plt.plot(SNRs, mn40as_acc)
    plt.plot(SNRs, htsat_acc)
    plt.plot(SNRs, tfnet_acc)
    plt.plot(SNRs, cnn10_acc)

    plt.legend(['mn40_as', 'HTS_AT', 'TFNet', 'CNN10'])

    if noise != 'brown':
        title = '{} Noise'.format(noise.capitalize())
    else:
        title = 'Brownian Noise'

    plt.suptitle(title)
    plt.ylabel('Model Accuracy')
    plt.xlabel('SNR [dB]')
    plt.grid(True, which='both', ls='-')
    plt.minorticks_on()

    if save_path is not None:
        plt.savefig(save_path, bbox_inches='tight')

    plt.show()


if __name__ == '__main__':
    noise = 'white'
    input_path = '.'
    save_path = 'accuracy_vs_snr_{}.png'.format(noise)

    plot_accuracy_vs_snr(noise, input_path, save_path=save_path)
