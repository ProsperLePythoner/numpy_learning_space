import matplotlib.pyplot as plt
import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[39, 67, 2], [12, 23, 63]])
arr = np.concatenate((arr1, arr2), axis=1)

print(f"Concatenated array:\n{arr}")

stack = np.stack((arr1, arr2), axis=1)
print(f"\nStack array:\n{stack}")

h_stack = np.hstack((arr1, arr2))
v_stack = np.vstack((arr1, arr2))
print(f"\nHStack array:\n{h_stack}")
print(f"\nVStack array:\n{v_stack}")