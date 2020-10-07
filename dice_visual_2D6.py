import pygal
from cube import Cube

# Создание двух кубиков D6.
cube_1 = Cube()
cube_2 = Cube()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(1000):
    result = cube_1.roll() * cube_2.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
max_result = cube_1.num_sides * cube_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Визуализация результатов.
hist = pygal.Bar()

hist.title = "Результаты подбрасывания 2-х шестигранных кубиков 1000 раз."
hist.x_labels = [x for x in range(1, max_result+1)]
hist.x_title = "Результат"
hist.y_title = "Частота результата"

hist.add('D6 * D6', frequencies)
hist.render_to_file('dice_visual_2D6.svg')