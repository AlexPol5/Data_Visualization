import csv

from datetime import datetime

from matplotlib import pyplot as plt

# Чтение дат, максимальных и минимальных температур из файла.
filename = 'samara_god.csv'
filename_1 = 'sochi_god.csv'

with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%d.%m.%y")
            high = int(row[1])
            low = int(row[2])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

with open (filename_1) as f1:
    reader_1 = csv.reader(f1)
    header_row_1 = next(reader_1)

    dates_1, highs_1, lows_1 = [], [], []
    for row in reader_1:
        try:
            current_date_1 = datetime.strptime(row[0], "%d.%m.%y")
            high_1 = int(row[1])
            low_1 = int(row[2])
        except ValueError:
            print(current_date_1, 'missing data')
        else:
            dates_1.append(current_date_1)
            highs_1.append(high_1)
            lows_1.append(low_1)

# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='black', alpha=0.5)
plt.plot(dates_1, highs_1, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.plot(dates_1, lows_1, c='green', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.7)
plt.fill_between(dates_1, highs_1, lows_1, facecolor='green', alpha=0.7)

# Форматирование диаграммы.
plt.title("Ежедневная максимальная и минимальная температура за 2019 год\nСамара и Сочи",
          fontsize=10)
plt.xlabel('', fontsize=7)

fig.autofmt_xdate()
plt.ylabel("Температура (С)", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=7)

plt.show()