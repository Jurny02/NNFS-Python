import numpy as np
import nnfs
import matplotlib.pyplot as plt
from nnfs.datasets import vertical_data

nnfs.init()

X, y = vertical_data(samples=100, classes=3)
plt.scatter(X[:, 0], X[:,1], c=y, s=40, cmap='brg')
plt.show()