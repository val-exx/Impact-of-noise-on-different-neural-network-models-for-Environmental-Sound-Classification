import os
import matplotlib.pyplot as plt

def read_acc_file(file_path):
    accs = []

    with open(file_path, 'r') as f:
        rows = f.readlines()

    for row in rows:
        row = row.strip()
        if row != '':
            accs.append(float(row))

    return accs

def get_noise_title(noise):
    if noise == 'brown':
        return 'Brownian Noise'
    elif noise == 'ambience':
        return 'TV Noise'
    elif noise == 'domestic':
        return 'Door Noise'
    elif noise == 'pet':
        return 'Dog Noise'
    elif noise == 'urban':
        return 'Car Engine Noise'
    elif noise == 'weather':
        return 'Rain Noise'
    else:
        return '{} Noise'.format(noise.capitalize())

def plot_accuracy_vs_snr(noise, input_path='.', save_path=None):
    SNRs = [-10, -5, 0, 5, 15, 20, 25, 30, 35, 40, 45, 50, 55, 65]

    cnn10_file = os.path.join(input_path, 'CNN10_{}'.format(noise))
    tfnet_file = os.path.join(input_path, 'TFNet_{}'.format(noise))
    mn40as_file = os.path.join(input_path, 'mn40_as_{}'.format(noise))
    htsat_file = os.path.join(input_path, 'HTS_AT_{}'.format(noise))

    if not os.path.exists(cnn10_file) and os.path.exists(cnn10_file + '.txt'):
        cnn10_file = cnn10_file + '.txt'
    if not os.path.exists(tfnet_file) and os.path.exists(tfnet_file + '.txt'):
        tfnet_file = tfnet_file + '.txt'
    if not os.path.exists(mn40as_file) and os.path.exists(mn40as_file + '.txt'):
        mn40as_file = mn40as_file + '.txt'
    if not os.path.exists(htsat_file) and os.path.exists(htsat_file + '.txt'):
        htsat_file = htsat_file + '.txt'

    cnn10_acc = read_acc_file(cnn10_file)
    tfnet_acc = read_acc_file(tfnet_file)
    mn40as_acc = read_acc_file(mn40as_file)
    htsat_acc = read_acc_file(htsat_file)

    plt.plot(SNRs[:len(cnn10_acc)], [acc * 100 for acc in cnn10_acc])
    plt.plot(SNRs[:len(tfnet_acc)], [acc * 100 for acc in tfnet_acc])
    plt.plot(SNRs[:len(mn40as_acc)], [acc * 100 for acc in mn40as_acc])
    plt.plot(SNRs[:len(htsat_acc)], [acc * 100 for acc in htsat_acc])

    plt.legend(['CNN10', 'TFNet', 'mn40_as', 'HTS_AT'])
    plt.title('Models Accuracy @ {}'.format(get_noise_title(noise)))
    plt.ylabel('Model Accuracy (%)')
    plt.xlabel('SNR (dB)')
    plt.grid(True, which="both", ls="-")
    plt.minorticks_on()

    if save_path is not None:
        plt.savefig(save_path, bbox_inches='tight')

    plt.show()

if __name__ == '__main__':
    noise = 'white'
    input_path = '.'
    save_path = 'accuracy_{}.png'.format(noise)

    plot_accuracy_vs_snr(
        noise=noise,
        input_path=input_path,
        save_path=save_path
    )
