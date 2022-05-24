'''
Questo modulo permette di plottare un'immagine con una sola funzione.
'''
import matplotlib.pyplot as plt

# @param img array da plottare
# @param title stringa da inserire come titolo

def plt_img(img, title):
    "Questa funzione plotta un immagine con un titolo."
    plt.imshow(img, cmap="gray")
    plt.title(title)
    plt.show(block = False)
