import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Назначение заголовка диаграммы и меток осей.
plt.title("Квадраты чисел", fontsize=24)
plt.xlabel("Значение", fontsize=14)
plt.ylabel("Квадрат значения", fontsize=14)

# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', labelsize=14)

plt.show()