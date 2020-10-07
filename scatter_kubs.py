import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens,
            edgecolor='none', s=40)

# Назначение заголовка диаграммы и меток осей.
plt.title("Кубы чисел", fontsize=18)
plt.xlabel("Значение", fontsize=12)
plt.ylabel("Куб значения", fontsize=12)

# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', which='major', labelsize=8)

# Назначение диапазона для каждой оси.
plt.axis([0, 5001, 0, 125000000000])

plt.show()
