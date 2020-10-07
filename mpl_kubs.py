import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

plt.plot(x_values, y_values, linewidth=5)

# Назначение заголовка диаграммы и меток осей.
plt.title('Кубы чисел', fontsize=24)
plt.xlabel('Значения', fontsize=14)
plt.ylabel('Кубы значений', fontsize=14)

# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', labelsize=14)

plt.show()

