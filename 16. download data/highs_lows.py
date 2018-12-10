import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = r'C:/Users/huayu/Desktop/something/Python_programming/16. download data/sitka_weather_07-2014.csv'
with open(filename)as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)
    
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')
    #设置图形格式
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    #绘制斜的日起标签
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
    #打印索引及其值
    # for index, column_header, in enumerate(header_row):
    #     print(index, column_header)