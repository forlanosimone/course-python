##
# Plot grafico

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots() # Create a figure containing a single axes
ax.plot([1, 2, 3, 4], [1, 4, 3, 3]) # Plot some data on the axes

plt.show()

# Plot array
x = np.arange(0,10,0.1)
y = np.sin(x)

plt.plot(x,y)
plt.show() # Abbiamo plottato l'array xy