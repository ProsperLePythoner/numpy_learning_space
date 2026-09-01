import numpy as np

arr = np.array([x for x in range(11)])
new_arr = np.array_split(arr, 5)

for i in new_arr:
    print(f"Array {i}: ", end='')
    for j in i:
        print(f"{j}", end=' ')
    print()