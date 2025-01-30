import numpy as np

left= 1
mode= 7
right= 11
n=2000
vals = np.random.triangular(left, mode, right, size=n)
print(vals)