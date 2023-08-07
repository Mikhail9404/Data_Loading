import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename_1 = '../data/sitka_weather_2018_simple.csv'
filename_2 = '../data/death_valley_2018_simple.csv'

current_date = range(1, 365)
highs, lows = [], []

with open(filename_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        if row[0] == "USW00025333":
            # Получение средней температуры из файла (Sitka).
            highs, lows = [], []
            title = "Daily high and low temperature - 2018\n Sitka"
            for row in reader:
                try:
                    high = int(row[5])
                    low = int(row[6])
                except ValueError:
                    print(f"Missing data for {current_date} (Sitka)")
                else:
                    highs.append(high)
                    lows.append(low)

        elif row[0] == "USC00042319":
            # Получение средней температуры из файла (Death_Valley).
            highs, lows = [], []
            title = "Daily high and low temperature - 2018\n Death Valley"
            for row in reader:
                try:
                    high = int(row[4])
                    low = int(row[5])
                except ValueError:
                    print(f"Missing data for {current_date} (Death Valley)")
                else:
                    highs.append(high)
                    lows.append(low)
        else:
            print("Я ничего не записал!")


# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red', alpha=0.5)
ax.plot(lows, c='blue', alpha=0.5)


# Форматирование даиграммы.
plt.title(title, fontsize=20)
plt.xlabel('Days', fontsize=20)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()