import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename_1 = 'C:/Users/kuznecov.mihail/PycharmProjects/Data_Loading/data/sitka_weather_2018_simple.csv'
filename_2 = 'C:/Users/kuznecov.mihail/PycharmProjects/Data_Loading/data/death_valley_2018_simple.csv'

current_date = range(1, 364)

with open(filename_1) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Получение средней температуры из файла (Sitka).
    average_sitka = []
    for row in reader:
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date} (Sitka)")
        else:
            average_sitka.append((high + low) / 2)

with open(filename_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Получение средней температуры из файла (Death_valley).
    average_dv = []
    for row in reader:
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date} (Death Valley)")
        else:
            average_dv.append((high + low) / 2)

# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(average_sitka, c='red', alpha=0.5)
ax.plot(average_dv, c='blue', alpha=0.5)

# Форматирование даиграммы.
title = "Daily average temperatures - 2018\nSitka and Death Valley"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()