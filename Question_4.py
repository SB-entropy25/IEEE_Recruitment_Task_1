import numpy as np

np.random.seed(0)  # For reproducibility

# Here we create a 5x5 matrix of random integers between 1 and 100
matrix_5x5 = np.random.randint(1, 101, (5, 5))
print("Original 5x5 matrix:")
print(matrix_5x5)

# here we extract the middle 3x3 matrix using slicing
middle_3x3 = matrix_5x5[1:4, 1:4]
print("\nMiddle 3x3 matrix:")
print(middle_3x3)

# extract the first row and last column
first_row = middle_3x3[0, :]
last_col = middle_3x3[:, -1]
print("\nFirst row of 3x3 matrix:", first_row)
print("Last column of 3x3 matrix:", last_col)

# printing the dot product
dot_product = np.dot(first_row, last_col)
print("\nDot product of first row and last column:", dot_product)

