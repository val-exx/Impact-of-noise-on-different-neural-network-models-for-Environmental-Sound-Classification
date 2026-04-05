import numpy as np

def compute_confusion_matrix(y_true, y_pred, num_classes=19):
    cm = np.zeros((num_classes, num_classes))

    for t, p in zip(y_true, y_pred):
        cm[int(t), int(p)] += 1

    return cm


def save_confusion_matrix(cm, output_path):
    np.savetxt(output_path, cm, fmt='%d')
