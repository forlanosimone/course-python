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

from point import point
from Moduli.read_file import read_file

# Definisco il path del file di testo e leggo i nomi delle immagini
PATH_file = ".\\Esame\\image.txt"

riga_splitted = read_file(PATH_file)

PATH_img = ".\\Esame\\Immagini\\"
i=0
for item in riga_splitted:
    nome = riga_splitted[i]
    img = cv.imread(f'{PATH_img}{nome}', cv.IMREAD_GRAYSCALE)
    plt.imshow(img, cmap = "gray")
    plt.show()
    i+=1

# Estrazione ROI (Region Of Interest)
# Posso fare una classe point dove fornisco x e y o inserisco le coordinate in una lista e poi splitto?
start_x = (2800) #int(input("inserisci start_x:")) #2800
start_y = (800) #int(input("inserisci start_y:")) #800
stop_x = (3000) #int(input("inserisci stop_x:")) #3000
stop_y = (1000) #int(input("inserisci stop_y:")) #1000

roi_img = img[start_y:stop_y ,start_x:stop_x] # Prima la y (righe) poi x (colonne)

# CLASSE
#roi = point(input("scrivi start_x"),input("scrivi start_y"),input("scrivi stop_x"),input("scrivi stop_y"))
#roi_img = img_1[roi.get_start_y() : roi.get_stop_x() , roi.get_start_x() : roi.get_stop_x()]
#roi_img = img_1[roi.get_roi()]

# PLOT ROI
#plt.imshow(roi_img, cmap="gray")
#plt.show()

# Adaptive Thresholding
th = cv.adaptiveThreshold(roi_img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,5)
th_inv = cv.adaptiveThreshold(roi_img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY_INV,11,2)
titles = ['Valore grilli v=0', 'Valore grilli v=255']
images = [th, th_inv]

for i in range(2):
    plt.subplot(1,2,i+1),
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

v = int(input("Inserisi 0 o 255:"))

if v == 255:
    v = 1

th = cv.adaptiveThreshold(roi_img,255,cv.ADAPTIVE_THRESH_MEAN_C, v,11,2)

# Matrice P con pixel che hanno valori pari a v
coordinate = []  # Lista delle coordinate
last_x, last_y = 0, 0  # Inizilizziamo a zero

rows, cols = th.shape  # Calcoliamo righe e colonne

# Itero su righe e colonne con due for
for x in range(rows):
    for y in range(cols):
        px = th[x, y]
        if px == 255:
                coordinate.append((y, x))
        last_x, last_y = x, y

coordinate.append((last_y, last_x))
print(coordinate)
P = np.array(coordinate)
print(P)

#Matrice P n*2
#[y1, x1,
#y2, x2,
#…
#yN, xN]

# Algoritmo DBSCAN
#eps = int(input("inserisci eps:")) #2
#min_samples = int(input("inserisci min_samples:")) #5

#X = StandardScaler().fit_transform(P)
db = DBSCAN(eps = 2, min_samples = 5).fit(P)

# Plot
F = np.ones((rows, cols))

plt.imshow(F)
plt.show()
