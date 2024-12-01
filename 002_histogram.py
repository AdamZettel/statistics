import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
np.random.seed(42)  # For reproducibility
data = np.random.normal(loc=0, scale=1, size=1000)  # Normally distributed data

# Plot the histogram
plt.hist(data, bins=30, color='blue', alpha=0.7, edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Randomly Generated Data')

# Show the plot
plt.show()
