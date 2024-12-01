import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Parameters
df = 10  # Degrees of freedom
x = np.linspace(-4, 4, 500)  # Values for the x-axis

# T-distribution PDF
t_pdf = t.pdf(x, df)

# Plot the t-distribution
plt.plot(x, t_pdf, label=f't-distribution (df={df})', color='blue', linewidth=2)

# Compare with Standard Normal Distribution
from scipy.stats import norm
normal_pdf = norm.pdf(x)
plt.plot(x, normal_pdf, label='Standard Normal', color='red', linestyle='--')

# Add labels, legend, and title
plt.title('t-Distribution vs Standard Normal')
plt.xlabel('x')
plt.ylabel('Density')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid(alpha=0.3)

# Show the plot
plt.show()
