import pygal

from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остаётся
# активной.
while True:
    # Построение случайного блуждания и нанесение точек на диаграмму.
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))


    # Визуализация результатов.
    hist = pygal.Bar()

    hist.title = "Случайное блуждание для 50000 точек."

    hist.render_to_file('bluzdan_visual_50000.svg')

    keep_running = input("Создать новое блуждание? (д/н): ")
    if keep_running == 'н':
        break