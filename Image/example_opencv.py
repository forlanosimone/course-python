##
# Utilizziamo OperCV per caricare l'immagine e matplotlib per plottarla

from cv2 import imread
import numpy as np # OpenCV lavora sempre con NumPy
import cv2
import matplotlib.pyplot as plt # Importiamo la funzionalità per fare il plot

# Immagine a colori
img = cv2.imread ("./Image/s1.png")
print
print(img.shape)

# Immagine in scala di grigi
img_g = cv2.imread("./Image/s1_g.png")
print(img_g.shape) # OpenCV converte anche l'immagine a scala di grigi in un immagine a 3 canali
# Se vogliamo evitare questo dobbiamo utilizzare IMREAD_GRAYSCALE
img_g = cv2.imread("./Image/s1_g.png", cv2.IMREAD_GRAYSCALE)
print(img_g.shape)

# OpenCV carica l'immagine in formato BGR mentre MathPlotLib in RGB
plt.imshow(img)
plt.show()

# Per vedere l'immagine normalmente dobbiamo fare lo swap dei canali B e R
img_reordered = img[:,:,[2,1,0]] # Swap canali

plt.imshow(img_reordered)
plt.show()

# Un'immagine con gradazioni di grigi ha sempre 3 canali RGB ma con valori uguali [77,77,77]
# L'immagine in scala di grigi si ottiene da una a colori così gray = 0.2989*R + 0.5870*G + 0.1140*B perché l'occhio umano ha sensibilità diversa ai colori
# Plotto l'immagine in scala di grigi
plt.imshow(img_g) # La vediamo a colori perché applica una color map
plt.show()

plt.imshow(img_g, cmap="gray") # Color map scala di grigi
plt.show()
