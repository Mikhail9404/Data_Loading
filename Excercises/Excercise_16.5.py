import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = '../data/moscow_snow.csv'



with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        # Получение кол-ва снега.
        snow = []
        for row in reader:
            try:
                snow_day = int(row[3])
            except ValueError:
                    print(f"Missing data for {current_date}")
            else:
                snow.append(snow_day)



# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(snow, c='red', alpha=0.5)

# Форматирование даиграммы.
title = "Daily snow time recently in Moscow"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=20)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()