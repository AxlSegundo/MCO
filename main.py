import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.linspace(0, 10, n)
y = 5 + 8 * x + np.random.normal(0, 0.5 * x, n)

plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter plot of y vs x")
plt.show()

mean_x = np.mean(x)
mean_y = np.mean(y)
sum_x = np.sum(x)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

b2 = (mean_y * sum_x - sum_xy) / (mean_x * sum_x - sum_x2)
b1 = mean_y - b2 * mean_x

prediction = b1 + b2 * x
print(f"y = {b1} + {b2}x")

# plot the regression line
plt.scatter(x, y)
plt.plot(x, prediction, color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter plot of y vs x")
plt.show()

# Get residuals
residuals = y - prediction
plt.scatter(x, residuals)
plt.axhline(y=0, color="r", linestyle="-")
plt.xlabel("x")
plt.ylabel("Residuals")
plt.title("Scatter plot of residuals vs x")
plt.show()

# Get the average error
average_error = np.mean(residuals)
print(average_error)
