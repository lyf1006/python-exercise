import matplotlib.pyplot as plt 
from random_walk import RandomWalk

#多次随机漫步
while True:
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    #设置绘图窗口尺寸,dpi指定分辨率
    plt.figure(dpi=128, figsize=(6, 4))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, c='green', linewidth=2)

    plt.show()
    
    keep_moving = input("Make another walk? (y/n): ")
    if keep_moving == 'n':
        break
