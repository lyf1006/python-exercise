import matplotlib.pyplot as plt 
from random_walk import RandomWalk

#多次随机漫步
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(100000)
    rw.fill_walk()

    #设置绘图窗口尺寸,dpi指定分辨率
    plt.figure(dpi=128, figsize=(6, 4))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, 
        cmap=plt.cm.Spectral, edgecolor='none', s=0.5)

    #突出起点和终点,参数s设置点的大小
    # plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    # plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', 
    #     s=100)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    
    keep_moving = input("Make another walk? (y/n): ")
    if keep_moving == 'n':
        break
