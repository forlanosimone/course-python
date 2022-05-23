'''
Questo modulo permette di leggere il file image.txt e ritornare una lista 
con il nome delle immagini all'interno del file.
'''

from unittest import result
import sys

#PATH_file = ".\\Esame\\image.txt"

def read_txt(PATH_file):
    # Operazione di apertura    
    try:   
        file = open(PATH_file, "r") # Apro il file in modalità di lettura
    except IOError:
        print("il file non esiste, controllare PATH_file")
        sys.exit(1)

    # Operazione di lettura
    riga = file.read()
    riga_splitted = riga.split("\n")

    # Operazione di chiusura
    file.close()

    return riga_splitted

#riga_splitted = read_txt(PATH_file)

import cv2 as cv
import matplotlib.pyplot as plt

#PATH_img = ".\\Esame\\immagini\\"

def read_img(PATH_img, riga_splitted):
    # Operazione di lettura
    nome = riga_splitted[0]

    img = cv.imread(f'{PATH_img}{nome}', cv.IMREAD_GRAYSCALE)

    if img.all == None:
        print("L'immagine non esiste, controllare PATH_img e l'immagine")
        sys.exit(1)
    return img

#read_img(PATH_img, riga_splitted)

#     i=0
# for item in riga_splitted:
#     nome = riga_splitted[i]
#     img = cv.imread(f'{PATH_img}{nome}', cv.IMREAD_GRAYSCALE)
#     plt.imshow(img, cmap = "gray")
#     plt.show()
#     i+=1