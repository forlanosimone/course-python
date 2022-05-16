##
# Per ogni ROI calcolare Min,Max,Media e Deviazione Standard e salvarle in un file di testo
# Descrizione del dato: https://micasense.com/sample-data-altum/ 

import tifffile as tiff
import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg

# Leggo le immagine
img_1 = tiff.imread(".\\Elaborazione immagini\\altum-capture\\IMG_0220_1.tif")
img_cv = cv2.imread(".\\Elaborazione immagini\\altum-capture\\IMG_0220_1.tif")
img_mtp = mpimg.imread(".\\Elaborazione immagini\\altum-capture\\IMG_0220_1.tif")

img_2 = tiff.imread(".\\Elaborazione immagini\\altum-capture\\IMG_0220_2.tif")
img_3 = tiff.imread(".\\Elaborazione immagini\\altum-capture\\IMG_0220_3.tif")
img_4 = tiff.imread(".\\Elaborazione immagini\\altum-capture\\IMG_0220_4.tif")
img_5 = tiff.imread(".\\Elaborazione immagini\\altum-capture\\IMG_0220_5.tif")

# Array totale NxMxK delle 5 immagini dove N ed M sono le dimensioni delle singole immagini e K = 5
(N,M) = img_1.shape
K = 5

array = np.zeros((N,M,K))
print("Dimensione array:", array.shape) # Ci mostra la dimensione, l'ultima cirfa corrisponde al numero di canali
print("Assi array:", array.ndim)

# np.append?
array[:,:,0] = img_1
array[:,:,1] = img_2
array[:,:,2] = img_3
array[:,:,3] = img_4
array[:,:,4] = img_5

# Apro il file di testo contenente la ROI
file = open(".\\Elaborazione immagini\\altum-capture\\ROI_1.txt")

# Operazione di lettura
riga = file.readline()
#print(riga)

riga_splitted = riga.split(";") # splitto la linea con il separatore (;)

x1 = int(riga_splitted[0])
y1 = int(riga_splitted[1])
x2 = int(riga_splitted[2])
y2 = int(riga_splitted[3])

# operazione di chiusura
file.close()

# ROI immagine
roi_img = array[x1:x2,y1:y2,0]
print(roi_img.shape)

# Plottiamo l'immagine
plt.imshow(roi_img)
plt.show()


# Calcolare Min,Max,Media e Deviazione Standard per ogni canale
min = np.min(roi_img)
print("Il minimo è:", min)
max = np.max(roi_img)
print("Il massimo è:", max)
mean = np.mean(roi_img)
print("La media è:", mean)
std_dev = np.std(roi_img)
print("La deviazione standard è:", std_dev)

# Salvataggio
name = str(input("Salva come:"))

statistic_ROI = [K, min, max, mean, std_dev]

np.savetxt(".\\Elaborazione immagini\\altum-capture\\s" + name, statistic_ROI) # Consente di salvare un file
