'''
Questo modulo permette di plottare un'immagine con una sola funzione.
'''
import matplotlib.pyplot as plt
import cv2 as cv

def plt_img(img, title):
    "Questa funzione plotta un immagine con un titolo."
    plt.imshow(img, cmap="gray")
    plt.title(title)
    plt.show(block = False)

if(__name__ == "__main__"):
    print("Voglio fare il test...")
