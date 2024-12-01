import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Step 1: Simulate data
np.random.seed(42)  # For reproducibility
n_samples = 100
x = np.random.rand(n_samples) * 10  # Independent variable (0 to 10)
true_slope = 2.5
true_intercept = 5.0
noise = np.random.randn(n_samples) * 2  # Add some noise
y = true_slope * x + true_intercept + noise  # Dependent variable

# Step 2: Fit the linear regression model using statsmodels
X = sm.add_constant(x)  # Add intercept (constant term) to the model
model = sm.OLS(y, X)  # Ordinary Least Squares
results = model.fit()

# Step 3: Display results
print(results.summary())

# Step 4: Plot the data and regression line
plt.scatter(x, y, label='Data', alpha=0.7)
plt.plot(x, results.predict(X), color='red', label='Fitted line', linewidth=2)
plt.xlabel('Independent Variable (x)')
plt.ylabel('Dependent Variable (y)')
plt.title('Linear Regression with Simulated Data')
plt.legend()
plt.show()
