import numpy as np

left= 2
mode= 5
right= 11
vals = np.random.triangular(left, mode, right, size=1000)
print(vals)