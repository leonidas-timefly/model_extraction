import matplotlib.pyplot as plt
import numpy as np
import matplotlib

plt.style.use('bmh')

for k in range(1):

    y0 = np.array()
    y1 = np.array()
    y2 = np.array()
    y3 = np.array()
    y4 = np.array()
    y5 = np.array()
    y6 = np.array()
    y7 = np.array()
    y8 = np.array()
    y9 = np.array()
    y10 = np.array()
    y11 = np.array()






    max_y = []
    min_y = []
    for k in range(80):
        max_num = max(y0[k], y1[k], y2[k], y3[k], y4[k], y5[k], y6[k], y7[k], y8[k], y9[k], y10[k])
        min_num = min(y0[k], y1[k], y2[k], y3[k], y4[k], y5[k], y6[k], y7[k], y8[k], y9[k], y10[k])
        max_y.append(max_num)
        min_y.append(min_num)
    r1 = (y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 - np.array(min_y)) / 10

    y0 = np.array()
    y1 = np.array()
    y2 = np.array()
    y3 = np.array()
    y4 = np.array()
    y5 = np.array()
    y6 = np.array()
    y7 = np.array()
    y8 = np.array()
    y9 = np.array()
    y10 = np.array()


    max_y = []
    min_y = []
    for k in range(80):
        max_num = max(y0[k], y1[k], y2[k], y3[k], y4[k], y5[k], y6[k], y7[k], y8[k], y9[k], y10[k])
        min_num = min(y0[k], y1[k], y2[k], y3[k], y4[k], y5[k], y6[k], y7[k], y8[k], y9[k], y10[k])
        max_y.append(max_num)
        min_y.append(min_num)
    r2 = (y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 - np.array(min_y)) / 10


x = np.arange(10, 90, 1)

plt.xlabel("Crop Rate(%)")
# 显示纵轴标签
plt.ylabel("Fidelity")
# 显示图标题
#plt.title("Fedility Viriation")
#plt.xlim(0.1,0.9)
plt.ylim(0.39,1.0)
plt.xlim(9,90)


f1 = np.polyfit(x, r2, 4)
f2 = np.polyfit(x, r1, 4)
p1 = np.poly1d(f1)
p2 = np.poly1d(f2)
yvals1 = p1(x)
yvals2 = p2(x)

plt.plot(x, yvals1)
plt.plot(x, yvals2, color = "#fcb001")

#plt.hist(r3,bins=80)
plt.bar(x, r2, alpha=0.6, width=1, edgecolor = "black", label = "NABOC=6")
plt.bar(x, r1, alpha=0.6, width=1, color = "#fcb001", edgecolor = "black", label = "NABOC=3")

plt.legend(loc=1)

plt.savefig("5-layer.jpg", dpi=1800, bbox_inches='tight')

plt.show()
