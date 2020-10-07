import csv

from datetime import datetime

from matplotlib import pyplot as plt

# Чтение дат, максимальных и минимальных температур из файла.
filename = 'samara_god.csv'
filename_1 = 'sochi_god.csv'

with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, osadki = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%d.%m.%y")
            osad = int(row[6])

        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            osadki.append(osad)

with open (filename_1) as f1:
    reader_1 = csv.reader(f1)
    header_row_1 = next(reader_1)

    dates_1, osadki_1 = [], []
    for row in reader_1:
        try:
            current_date_1 = datetime.strptime(row[0], "%d.%m.%y")
            osad_1 = int(row[6])

        except ValueError:
            print(current_date_1, 'missing data')
        else:
            dates_1.append(current_date_1)
            osadki_1.append(osad_1)

# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, osadki, c='red', alpha=0.5)
plt.plot(dates_1, osadki_1, c='blue', alpha=0.5)

#plt.fill_between(dates, osadki, osadki_1, facecolor='blue', alpha=0.7)

# Форматирование диаграммы.
plt.title("Ежедневное количество осадков за 2019 год\nСамара и Сочи",
          fontsize=10)
plt.xlabel('', fontsize=7)

fig.autofmt_xdate()
plt.ylabel("Осадки, мм", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=7)

plt.show()