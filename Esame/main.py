##
# Questo codice premette di...
# URL DBSCAN: https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py
# URL Adaptive Thresholding: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html

# Importo le librerie
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

from moduli import read, crop_imge
from moduli.plt_img import plt_img

# Definisco il path del file di testo e leggo i nomi delle immagini
PATH_file = ".\\Esame\\image.txt"
riga_splitted = read.read_txt(PATH_file)

# Definisco il path delle immagini
PATH_img = ".\\Esame\\immagini\\"
img = read.read_img(PATH_img, riga_splitted)

# Plot immagine
plt_img(img, "Immagine Originale")

# Estrazione ROI (Region Of Interest)
roi_img = crop_imge.roi(img)

# CLASSE
#roi = point(input("scrivi start_x"),input("scrivi start_y"),input("scrivi stop_x"),input("scrivi stop_y"))
#roi_img = img_1[roi.get_start_y() : roi.get_stop_x() , roi.get_start_x() : roi.get_stop_x()]
#roi_img = img_1[roi.get_roi()]

# Plot ROI
plt_img(roi_img, "Region of Interest")

# Adaptive Thresholding
th = cv.adaptiveThreshold(roi_img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,21,6)
th_inv = cv.adaptiveThreshold(roi_img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY_INV,21,6)

# Erosione e dilatazione
'''
kernel = np.ones((3,3))
kernel[1,1] = 1
kernel_2 = kernel
kernel_2[1,1] = 2
th_filter= cv.dilate(th, kernel)
th_filter= cv.erode(th, kernel_2)
noiseless_image_bw = cv.fastNlMeansDenoising(roi_img, None, h = 10, templateWindowSize = 7,\
                                            searchWindowSize = 21)
'''
# Plot ROI con 2 valori
titles = ["Valore grilli v=0", "Valore grilli v=255"]
images = [th, th_inv]

for i in range(2):
    plt.subplot(1,2,i+1),
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

# Utente sceglie valore dei grilli
v = int(input("Inserisi valori grilli, 0 o 255:"))

if v == 255:
    v = 1

# Plot immagine con valore scelto
th = cv.adaptiveThreshold(roi_img,255,cv.ADAPTIVE_THRESH_MEAN_C, v,21,6)
plt_img(th,"Immagine con valori scelti")

# Matrice P con pixel che hanno valori pari a v
coordinate = []  # Lista delle coordinate
last_x, last_y = 0, 0  # Inizilizziamo a zero

rows, cols = th.shape  # Calcoliamo righe e colonne

if v == 1:
    v = 255

# Itero su righe e colonne con due for
for x in range(399):
    for y in range(499):
        px = th[x, y]
        if px == v:
                coordinate.append((y, x))
        last_x, last_y = x, y

coordinate.append((last_y, last_x))
P = np.array(coordinate)
print(P)
plt_img(th,"Immagine con valori scelti")

# Algoritmo DBSCAN
eps = 2 #int(input("inserisci eps (Es.2):"))
min_samples = 5 #int(input("inserisci min_samples (Es.5):"))

#X = StandardScaler().fit_transform(P)
db = DBSCAN(eps = 2, min_samples = 5).fit(P)

# Plot
F = np.full((rows, cols), -1)
print(F)
