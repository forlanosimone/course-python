

import numpy as np

x = np.arange(0,10,0.1) 
print(x)

y = np.sin(x) # Ci sono operazioni matematiche che si possono fare direttamente sugli array (Es. sin)

np.save("Librerie/test.npy",y) # Consente di salvare un file di nome test.npy con all'interno l'array y

import os
print(os.getcwd()) # Ci peremtte di conoscere il percorso su cui stiamo lavorando (current work directory)

y = np.load('Librerie/test.npy')
print(y)