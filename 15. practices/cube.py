import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]
bigx_values = list(range(1, 5001))
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.magma)
plt.title("**3", fontsize=24)
plt.xlabel("value", fontsize=12)
plt.ylabel("value**3", fontsize=12)
plt.tick_params(axis='both', labelsize=14)

plt.show()
