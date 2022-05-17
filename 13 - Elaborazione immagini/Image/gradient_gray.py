##
# Voglio mostrare un'immagine con ogni colonna un intensità di grigi diversa

import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((240,640),dtype=np.uint8)

# Operazione di unpacking che consente di prendere una tupla e spacchettarla
(r,c) = img.shape # Shape fa tornare una tupla

# Si usa i nella righe e j nelle colonne
for j in range(c):
    img[:,j] = j

# Plot
plt.imshow(img, cmap="gray")
plt.show()
