##
# Bitwise Operations (per ogni bit facciamo operazioni di AND, OR, NOT, XOR)
# https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html#bitwise-operations

import numpy as np
import matplotlib.pyplot as plt
import cv2

img_g = cv2.imread(".\\13 - Elaborazione immagini\\Image\\s1_g.png", cv2.IMREAD_GRAYSCALE)
plt.imshow(img_g, cmap="gray")
plt.show()

# Bitwise Operations
'''
Ecco come sono rappresentati i numeri

0000 0000 0
0000 0001 1
0000 0010 2
0000 0011 3
0000 0100 4
0000 0101 5
0000 0110 6
0000 0111 7
0000 1000 8

Ecco la funzione AND

A B | (A AND B)
0 0 |     0
0 1 |     0
1 0 |     0
1 1 |     1

'''
print("7 AND 1:",np.bitwise_and(7,1)) # Faccio 7 AND 1
'''
7 AND 1
0000 0111
0000 0001
---------
0000 0001

'''
print("7 AND 2:",np.bitwise_and(7,2))
'''
7 AND 2
0000 0111
0000 0010
---------
0000 0010

'''
print("6 AND 1:",np.bitwise_and(6,1))
'''
7 AND 1
0000 0110
0000 0001
---------
0000 0000

'''

# Facciamo img_g AND 1
img_g1 = np.bitwise_and(img_g, 1)
plt.imshow(img_g1) # Steganografia
plt.show()

'''
Nell'immagine di Van Gogh sono stati messi pari a 0 l'ultimo bit di ogni pixel 
poi l'immagine di Marylin dov'era 0 è rimasta 0 
e dove era 1 è stata aggiunta al valore dell'immagine di Van Gogh
'''
# Matrice di rotazione
rows = img_g.shape[0]
print("Rows:",rows)
cols = img_g.shape[1]
print("Cols:",cols)

M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1.2) # 45° rotazione e 1.2 fattore di scala
out = cv2.warpAffine(img_g, M, (cols,rows))
plt.imshow(out)
plt.show()

# Smoothing filter
kernel = np.ones((11,11), np.float32)/(11*11)
dst = cv2.filter2D(img_g, -1, kernel)
plt.imshow(dst, cmap="gray")
plt.show()
