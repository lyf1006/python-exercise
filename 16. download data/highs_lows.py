import csv
import matplotlib.pyplot as plt
from datetime import datetime

#相对路径加上上一级就不会报错
filename = r'16. download data/death_valley_2014.csv'
with open(filename)as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,highs, lows = [], [], []
    for row in reader:
        #错误检查，温度不能为字符串
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
      
    fig = plt.figure(dpi=128, figsize=(10, 6))
    #alpha指定颜色的透明度，0为完全透明
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    #填充区间
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    #设置图形格式
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    #绘制斜的日起标签
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
    #打印索引及其值
    # for index, column_header, in enumerate(header_row):
    #     print(index, column_header)