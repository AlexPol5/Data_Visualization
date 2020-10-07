import pygal
from cube import Cube

# Создание кубика D6.
cube = Cube()

# Моделирование серии бросков с сохранением результатов в списке.
# results = []
results = [cube.roll() for roll_num in range(1000)]
# for roll_num in range(1000):
    # result = cube.roll()
    # results.append(result)

# Анализ результатов.
# frequencies = []
frequencies = [results.count(value) for value in range(1, cube.num_sides+1)]
# for value in range(1, cube.num_sides+1):
    #frequency = results.count(value)
    #frequencies.append(frequency)

print(frequencies)

# Визуализация результатов.
hist = pygal.Bar()

hist.title = "Результаты подбрасывания шестигранного кубика 1000 раз."
hist.x_labels = [x for x in range(1, cube.num_sides+1)]
hist.x_title = "Результат"
hist.y_title = "Частота результата"

hist.add('D6', frequencies)
hist.render_to_file('cube_visual.svg')