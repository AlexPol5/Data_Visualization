import pygal
from cube import Cube

# Создание кубиков D6 и D10.
cube_1 = Cube()
cube_2 = Cube(10)

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(50000):
    result = cube_1.roll() + cube_2.roll()
    results.append(result)

# Анализ результатов.
frequencies = []
max_result = cube_1.num_sides + cube_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Визуализация результатов.
hist = pygal.Bar()

hist.title = "Результаты подбрасывания 2-х кубиков D6 и D10 50000 раз."
hist.x_labels = [x for x in range(2, max_result+1)]
hist.x_title = "Результат"
hist.y_title = "Частота результата"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')