import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.array([[1, 2, 3], [3, -5, 1], [9, 8, 9], [10, 1, 0.12]])
cent = np.array([n for n in range(101)])

plt.title("Random data".upper())
print(f"The mean for cent is {np.mean(cent)}")
plt.plot(data, marker="o")
plt.show()