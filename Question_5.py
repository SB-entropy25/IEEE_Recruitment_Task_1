import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random numbers from a standard normal distribution (mean=0, std=1)
data = np.random.normal(loc=0, scale=1, size=1000)

# Generate indices for the x-axis (can be a simple range)
indices = np.arange(1000)

# Create a scatter plot
plt.scatter(indices, data, alpha=0.5)
plt.title("Scatter Plot of 1000 Random Numbers from Normal Distribution")
plt.xlabel("Sample Index")
plt.ylabel("Random Value (Normal Distribution)")
plt.show()
