import matplotlib.pyplot as plt
import numpy as np
import math

# Draw a graph for sinh(x)
sinh = np.sinh
cosh = np.cosh
tanh = np.tanh

plt.plot(sinh, color='red', label='sinh')
plt.legend()
plt.show()