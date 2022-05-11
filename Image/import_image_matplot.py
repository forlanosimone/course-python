##
# Andiamo a caricare l'immagine con matplotlib

import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

print(os.getcwd()) # In questo modo printiamo la Current Work Dircetory
img = mpimg.imread("./Image/s1.png")
print("Dimensione:", img.shape) # Ci mostra la dimensione, l'ultima cirfa corrisponde al numero di canali
print("Canali:", img.ndim) # Numero di canali (RGB)

# Vogliamo prendere tutti i valori del 1° pixel
print(img[0,0,:])

# Importando NumPy possiamo utilizzare anche la funzione max
import numpy as np
print(np.max(img[:,0,0])) # Prende il valore massimo di rosso nella riga

# In questo modo plottiamo l'immagine
plt.imshow(img)
plt.show()

# Color Map, ci consente di renderizzare in modo diverso i colori
img_ch0 = img[:,:,0]
plt.imshow(img_ch0)
plt.show()

# Scala di grigi
plt.imshow(img_ch0, cmap="gray")
plt.show()

# Binary Thresholding
binary_img = img_ch0 > 0.6 # Ho selezionato i pin che hanno un valore maggiore di 0.6
plt.imshow(binary_img, cmap="gray")
plt.show()
