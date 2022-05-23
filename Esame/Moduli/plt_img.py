'''
Questo modulo permette di plottare un'immagine con una sola funzione.
'''

import matplotlib.pyplot as plt
import cv2 as cv

def plt_img(img, title): #, label_x, label_y):
    plt.imshow(img, cmap="gray")
    plt.title(title)
    #plt.xticks([label_x]),plt.yticks([label_y])
    plt.show()
    