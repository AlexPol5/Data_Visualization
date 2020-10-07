import csv

from datetime import datetime

from matplotlib import pyplot as plt

# Чтение дат и максимальных и минимальных температур из файла.
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    #for index, column_header in enumerate(header_row):
     #   print(index, column_header)

# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.3)

# Форматирование диаграммы.
title = "Дневные максимумы и минимумы температур в 2014 г\nДолина Смерти"
plt.title(title, fontsize=14)
plt.xlabel('', fontsize=7)

fig.autofmt_xdate()
plt.ylabel("Температура, F", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=7)

plt.show()