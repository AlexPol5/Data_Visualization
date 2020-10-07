from cube import Cube
import pygal

# Создание двух кубиков D8.
cube_1 = Cube(8)
cube_2 = Cube(8)

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(5000000):
    result = cube_1.roll() + cube_2.roll()
    results.append(result)

# Анализ резульататов.
frequencies = []
max_result = cube_1.num_sides + cube_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Визуализация результатов.
hist = pygal.Bar()

hist.title = "Результаты подбрасывания двух 8-гранных кубиков 5 млн раз."
hist.x_labels = [x for x in range(2, max_result+1)]
hist.x_title = "Результат"
hist.y_title = "Частота результата"

hist.add('D8 + D8', frequencies)
hist.render_to_file('cube_visual_D8.svg')