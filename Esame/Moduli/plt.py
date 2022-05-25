'''
Questo modulo permette di plottare un'immagine con una sola funzione
'''
import matplotlib.pyplot as plt

def plt_img(img, title, block):
    '''
    Questa funzione plotta un immagine con un titolo.
    @param img: array da plottare
    @param title: stringa da inserire come titolo
    @param block: se block=False è bloccante
    '''

    plt.imshow(img, cmap="gray") # Con mappa di colori
    plt.title(title)
    plt.show(block=block) # Plot non bloccante False
