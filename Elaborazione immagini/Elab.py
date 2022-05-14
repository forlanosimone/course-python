##
# 
# https://micasense.com/sample-data-altum/ 

import tifffile as tiff
import numpy as np
import sys

# Leggo l'immagine
my_img = tiff.imread(".\\Elaborazione immagini\\altum-capture\\IMG_0220_1.tif")

# Apro il file di testo contenente la ROI
file = open(".\\Elaborazione immagini\\ROI_1.txt")

# Operazione di lettura
riga = str(file.readline())
print(riga)