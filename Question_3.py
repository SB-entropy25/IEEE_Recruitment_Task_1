import numpy as np

#Here we create 5x5 matrix with random integers between 1 and 100
matrix = np.random.randint(1, 101, size=(5,5))

# as asked we are printing matrix in grid format
print("Matrix:\n", matrix)

# Statistics
print("Maximum:", matrix.max())
print("Minimum:", matrix.min())
print("Mean:", matrix.mean())

# Normalize elements to range 0-1
norm_matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min())
print("Normalized Matrix:\n", norm_matrix)

# Flatten and sort
flat_sorted = np.sort(matrix.flatten())  #print original matrix
print("Flattened & Sorted(original matrix):", flat_sorted)

flat_sorted2 = np.sort(norm_matrix.flatten()) #flatten normalised matrix
print("Flattened & Sorted(Normalised matrix):", flat_sorted2)
