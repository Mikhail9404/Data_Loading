import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename_1 = 'C:/Users/kuznecov.mihail/PycharmProjects/Data_Loading/data/sitka_weather_2018_simple.csv'
filename_2 = 'C:/Users/kuznecov.mihail/PycharmProjects/Data_Loading/data/death_valley_2018_simple.csv'

with open(filename_1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Получение дат, температурных минимумов и максимумов из файла (Sitka).
    highs_sitka, lows_sitka = [], []
    for row in reader:
        current_date = range(1, 364)
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date} (Sitka)")
        else:
#            dates_sitka.append(current_date)
            highs_sitka.append(high)
            lows_sitka.append(low)

with open(filename_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Получение температурных минимумов и максимумов из файла (Death_valley).
    dates_dv = range(1, 364)
    highs_dv, lows_dv = [], []
#    current_date =
    for row in reader:
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date} (Death Valley)")
        else:
            highs_dv.append(high)
            lows_dv.append(low)
           # dates_dv.append(current_date)

# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates_dv, highs_sitka, highs_dv, c='red', alpha=0.5)
ax.plot(dates_dv, lows_sitka, lows_dv, c='blue', alpha=0.5)

# Форматирование даиграммы.
title = "Daily high and low temperatures - 2018\nSitka and Death Valley"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()