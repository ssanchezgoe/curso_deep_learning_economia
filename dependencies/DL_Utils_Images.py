import numpy as np
import matplotlib.pyplot as plt


def imshow_RGB(path_to_image)
    img1 = plt.imread(path_to_image)
    figure, plots = plt.subplots(ncols=3, nrows=1)
    for i, subplot in zip(range(3), plots):
        temp = np.zeros(img1.shape, dtype='uint8')
        temp[:,:,i] = img1[:,:,i]
        subplot.imshow(temp)
        subplot.set_axis_off()
    plt.show()

    return None
