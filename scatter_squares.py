import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolor='none', s=40)

# Назначение заголовка диаграммы и меток осей.
plt.title("Квадраты чисел", fontsize=18)
plt.xlabel("Значение", fontsize=12)
plt.ylabel("Квадрат значения", fontsize=12)

# Назначение диапазона для каждой оси.
plt.axis([0, 1000, 0, 1100000])

# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', which='major', labelsize=8)

plt.savefig('squares_plot.png', bbox_iches='tight')