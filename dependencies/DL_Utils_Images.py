import numpy as np
import matplotlib.pyplot as plt


def imshow_RGB(path_to_image):
    img1 = plt.imread(path_to_image)
    figure, plots = plt.subplots(ncols=3, nrows=1)
    for i, subplot in zip(range(3), plots):
        temp = np.zeros(img1.shape, dtype='uint8')
        temp[:,:,i] = img1[:,:,i]
        subplot.imshow(temp)
        subplot.set_axis_off()
    plt.show()

    return None

def image_info(path_to_image):

    image = plt.imread(path_to_image)
    print(f"Profundidad de pixel {image.dtype}")
    print(f"Valores (min, max): ({np.min(image)},{np.max(image)})")
    print(f"Dimensiones de la imagen: {image.shape}")
    print(f"Total Pixeles: {image.ravel().shape()}")

    return None

def imshow(path_to_image, cmap = "gray", title = "Imagen"):
    img = plt.imread(path_to_image)
    plt.imshow(img, cmap=cmap)
    plt.title(title)
    plt.show()

    return None
