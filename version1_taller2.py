import numpy as np
import matplotlib.pyplot as plt

left= 1
mode= 7
right= 11
n=2000
vals = np.random.triangular(left, mode, right, size=n)
print(vals)
plt.hist(vals, bins=50, density=True, alpha=0.6, color='b', edgecolor='black')

plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.title("Distribución Triangular")
plt.show()