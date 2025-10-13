#Define two custom numpy arrays, say A and B. Generate two new numpy arrays by stacking A and B vertically and horizontally.

import numpy as np

A = np.array([[1, 2, 3],
             [4, 5, 6]])

B = np.array([[7, 8, 9],
              [10, 11, 12]])

print("A: \n", A)
print("B: \n", B)
print("\n")



# Stack vertically
vertical_stack = np.vstack((A, B))

# Stack horizontally
horizontal_stack = np.hstack((A, B))

print("Vertical Stack:\n", vertical_stack)
print("\nHorizontal Stack:\n", horizontal_stack)