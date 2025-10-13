# 2. Find common elements between A and B. [Hint : Intersection of two sets]

import numpy as np

A = np.array([[1, 2, 3],
             [4, 5, 6]])

B = np.array([[7, 8, 9],
              [10, 11, 12]])

common_elements = np.intersect1d(A, B)

print("Common elements between A and B:", common_elements)