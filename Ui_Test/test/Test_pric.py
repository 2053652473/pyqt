# 0、导入包import matplotlib.pyplot as plt# 1、准备数据
from matplotlib import pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
fig = plt.figure(figsize=(8, 3), dpi=100, facecolor=(0,1,0,1), edgecolor=(1,0,0,1), frameon=True, linewidth=1)
ax1 = fig.add_subplot(121)
ax1.plot(x, y)
ax2 = fig.add_subplot(122)
ax2.plot(x, y)
ax1.set_title('lim')
ax2.set_title('ticks')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax1.set_xlim([1, 4])
ax1.set_ylim([10, 40])
ax2.set_xticks(range(1, 5))
ax2.set_yticks([(i*10) for i in range(1, 5)])
# 5、保存图形(按需要使用)# plt.savefig(‘xxx.png’)# 6、显示图形\
plt.show()