##
# OpenCV usa sempre NumPy
# https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_tutorials.html

import cv2
import numpy as np

img = cv2.imread("./Image/s1.png")
print("Tipo:", img.dtype,"Canali:", img.ndim,"Dimensione:", img.shape)

# La matrice è leggibile e scrivibile
print(img[0,0,0]) # Lettura
img[0,0,0] = 255 # Scrittura
print(img[0,0,0]) # Lettura

# ROI Region Of Interest
print(img.shape)
roi_img = img[300:400,300:400,:]
print(roi_img.shape)
