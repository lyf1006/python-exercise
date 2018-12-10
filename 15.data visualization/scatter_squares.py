import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

#edgecolor 设置为none 将删除数据点的黑色轮廓
#c设置数据点的颜色,可以使用RGB值，0-1之间取值
#cmap确定映射的颜色,可以参见colormap reference（matplotlib.org 下的examples)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.RdYlGn, edgecolor='none', s=40)
#设置图表标题并给坐标轴加上标签
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

#自动保存图表，第一参数为图表名称，第二参数作用为裁去空白区域
plt.savefig('squares_plot.png', bbox_inches='tight' )

plt.show()
