import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'C:/Users/kuznecov.mihail/PycharmProjects/Data_Loading/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Получение дат и велечину ежедневных осадков.
    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            prcp = float(row[3])
        except ValueError:
            print(f"Missing data {current_date}")
        else:
            dates.append(current_date)
            prcps.append(prcp)

# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, prcps, c='red', alpha=0.5)

# Форматирование даиграммы.
plt.title("Daily precipitation - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation value", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()