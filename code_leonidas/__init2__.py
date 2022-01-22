import matplotlib.pyplot as plt
import numpy as np
import matplotlib

plt.style.use('bmh')

for k in range(1):


    y0 = np.array([0.9333333333333333, 0.6, 0.8, 0.9333333333333333, 1.0, 0.8, 0.9333333333333333, 0.8666666666666667, 0.8, 0.8666666666666667, 0.9333333333333333, 0.8, 0.8, 1.0, 0.6666666666666666, 0.7333333333333333, 0.9333333333333333, 0.8, 0.9333333333333333, 0.9333333333333333, 0.8, 0.9333333333333333, 0.6666666666666666, 0.7333333333333333, 0.8666666666666667, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.9333333333333333, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0, 0.9333333333333333, 0.8666666666666667, 1.0, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 1.0, 0.8666666666666667, 1.0, 1.0, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.7333333333333333, 0.9333333333333333, 1.0, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.8, 0.7333333333333333, 0.6666666666666666, 0.8, 0.8666666666666667, 1.0, 0.7333333333333333, 0.5333333333333333, 0.8, 0.7333333333333333, 0.6, 0.8666666666666667, 0.7333333333333333, 0.4666666666666667, 0.6, 0.3333333333333333, 0.4])
    y1 = np.array([0.7333333333333333, 0.8, 0.4666666666666667, 0.6666666666666666, 0.8, 0.9333333333333333, 1.0, 0.8666666666666667, 0.8666666666666667, 0.6666666666666666, 0.8, 0.7333333333333333, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.8, 1.0, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.6, 1.0, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 0.6666666666666666, 1.0, 1.0, 0.8666666666666667, 0.9333333333333333, 1.0, 0.8, 0.8666666666666667, 0.7333333333333333, 1.0, 0.8666666666666667, 1.0, 0.8666666666666667, 0.6, 0.9333333333333333, 0.8, 0.8, 0.8, 0.9333333333333333, 0.8666666666666667, 0.9333333333333333, 1.0, 0.9333333333333333, 1.0, 0.8, 0.8666666666666667, 1.0, 1.0, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.8, 0.8666666666666667, 1.0, 0.8, 0.9333333333333333, 1.0, 0.8666666666666667, 0.9333333333333333, 0.9333333333333333, 1.0, 0.8666666666666667, 0.8, 0.7333333333333333, 0.5333333333333333, 0.7333333333333333, 0.7333333333333333, 0.6666666666666666, 0.5333333333333333, 0.7333333333333333, 0.6, 0.4, 0.6])
    y2 = np.array([0.8, 0.4666666666666667, 0.8666666666666667, 0.6666666666666666, 0.9333333333333333, 0.8666666666666667, 0.4666666666666667, 0.7333333333333333, 1.0, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 0.5333333333333333, 1.0, 1.0, 1.0, 0.8666666666666667, 0.8, 1.0, 0.9333333333333333, 0.6666666666666666, 0.9333333333333333, 0.7333333333333333, 0.8666666666666667, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.7333333333333333, 0.8, 1.0, 0.8666666666666667, 0.8, 1.0, 1.0, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 1.0, 1.0, 0.5333333333333333, 0.6666666666666666, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.9333333333333333, 1.0, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 1.0, 1.0, 0.8666666666666667, 0.8666666666666667, 1.0, 0.9333333333333333, 1.0, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 1.0, 1.0, 1.0, 1.0, 0.8666666666666667, 0.7333333333333333, 1.0, 0.8666666666666667, 0.8666666666666667, 0.7333333333333333, 0.8, 0.6666666666666666, 0.6, 0.8666666666666667, 0.6, 0.6, 0.7333333333333333, 0.5333333333333333, 0.4666666666666667, 0.4])
    y3 = np.array([0.9333333333333333, 0.8, 0.8, 0.7333333333333333, 0.8, 0.8, 0.8, 1.0, 0.8, 0.9333333333333333, 0.8, 0.8666666666666667, 0.6666666666666666, 0.8, 0.8, 1.0, 1.0, 0.9333333333333333, 0.8666666666666667, 0.3333333333333333, 0.8666666666666667, 0.8, 0.6666666666666666, 0.8, 0.7333333333333333, 0.7333333333333333, 0.7333333333333333, 0.9333333333333333, 1.0, 0.8, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.8666666666666667, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.8666666666666667, 1.0, 0.8, 1.0, 1.0, 0.8666666666666667, 0.9333333333333333, 0.9333333333333333, 1.0, 0.9333333333333333, 0.8666666666666667, 0.7333333333333333, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.9333333333333333, 0.8666666666666667, 0.8, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.6, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.3333333333333333, 0.7333333333333333, 0.8, 0.4666666666666667, 0.6666666666666666, 0.4666666666666667, 0.6])
    y4 = np.array([0.9333333333333333, 1.0, 0.8, 0.9333333333333333, 0.8, 0.9333333333333333, 0.9333333333333333, 0.7333333333333333, 1.0, 0.8666666666666667, 0.8, 0.8666666666666667, 0.8, 1.0, 0.8666666666666667, 0.9333333333333333, 0.8, 1.0, 1.0, 0.9333333333333333, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 0.7333333333333333, 0.8, 0.9333333333333333, 0.9333333333333333, 0.8666666666666667, 0.7333333333333333, 0.8, 0.8666666666666667, 0.8, 0.9333333333333333, 0.9333333333333333, 0.8666666666666667, 0.8, 0.8, 1.0, 0.8, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8, 0.6666666666666666, 0.9333333333333333, 1.0, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 1.0, 0.8, 0.9333333333333333, 1.0, 1.0, 0.8666666666666667, 0.8, 1.0, 0.8, 0.8666666666666667, 0.9333333333333333, 0.7333333333333333, 1.0, 0.8666666666666667, 0.8, 0.8, 0.9333333333333333, 0.9333333333333333, 1.0, 0.9333333333333333, 0.8666666666666667, 0.6, 0.6666666666666666, 0.6, 0.6666666666666666, 0.7333333333333333, 0.4, 0.6, 0.4])
    y5 = np.array([0.6, 0.9333333333333333, 0.6, 0.9333333333333333, 0.9333333333333333, 0.7333333333333333, 0.9333333333333333, 0.7333333333333333, 0.8, 0.8666666666666667, 0.8, 0.8, 0.8666666666666667, 0.6666666666666666, 0.8666666666666667, 0.8, 0.9333333333333333, 1.0, 0.7333333333333333, 0.8666666666666667, 0.8666666666666667, 0.6666666666666666, 1.0, 0.8, 0.8666666666666667, 0.8, 0.7333333333333333, 0.8666666666666667, 0.9333333333333333, 0.6, 1.0, 0.8666666666666667, 1.0, 0.9333333333333333, 0.8666666666666667, 1.0, 0.8666666666666667, 1.0, 0.8666666666666667, 1.0, 0.9333333333333333, 0.7333333333333333, 1.0, 0.8666666666666667, 1.0, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 1.0, 1.0, 0.9333333333333333, 0.9333333333333333, 0.8666666666666667, 0.9333333333333333, 1.0, 0.8666666666666667, 1.0, 0.8666666666666667, 0.9333333333333333, 1.0, 0.7333333333333333, 0.9333333333333333, 1.0, 0.9333333333333333, 0.9333333333333333, 0.8666666666666667, 0.8, 0.7333333333333333, 0.8, 0.8666666666666667, 0.4666666666666667, 0.6666666666666666, 0.6666666666666666, 0.4666666666666667, 0.2, 0.6666666666666666, 0.5333333333333333, 0.7333333333333333, 0.5333333333333333])
    y6 = np.array([1.0, 0.8, 0.9333333333333333, 0.8, 0.8666666666666667, 0.9333333333333333, 1.0, 0.7333333333333333, 0.8, 0.3333333333333333, 0.8, 0.7333333333333333, 1.0, 0.8666666666666667, 0.9333333333333333, 0.8, 0.9333333333333333, 0.8, 0.9333333333333333, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.8, 1.0, 0.8666666666666667, 0.9333333333333333, 0.5333333333333333, 1.0, 0.6666666666666666, 0.9333333333333333, 0.6666666666666666, 0.8, 0.8666666666666667, 1.0, 0.8666666666666667, 0.8, 0.7333333333333333, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 1.0, 1.0, 0.9333333333333333, 0.8, 1.0, 0.7333333333333333, 0.9333333333333333, 0.7333333333333333, 1.0, 0.9333333333333333, 1.0, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 1.0, 0.8, 0.9333333333333333, 0.9333333333333333, 1.0, 0.8, 0.8666666666666667, 0.8, 0.9333333333333333, 0.9333333333333333, 0.7333333333333333, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.6666666666666666, 0.6, 0.7333333333333333, 0.7333333333333333, 0.7333333333333333, 0.7333333333333333, 0.4666666666666667, 0.4, 0.6666666666666666, 0.4666666666666667, 0.4])
    y7 = np.array([0.7333333333333333, 0.8, 0.6, 0.9333333333333333, 0.9333333333333333, 0.8, 1.0, 1.0, 0.8666666666666667, 0.9333333333333333, 0.7333333333333333, 0.8, 0.8666666666666667, 0.6666666666666666, 0.8666666666666667, 0.9333333333333333, 0.9333333333333333, 1.0, 0.8, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 1.0, 0.6666666666666666, 0.8, 1.0, 0.8666666666666667, 1.0, 0.6, 0.8, 1.0, 0.9333333333333333, 0.8666666666666667, 0.7333333333333333, 0.5333333333333333, 0.9333333333333333, 0.9333333333333333, 0.7333333333333333, 0.9333333333333333, 0.9333333333333333, 0.6666666666666666, 0.6, 0.8666666666666667, 1.0, 0.7333333333333333, 0.8, 1.0, 1.0, 0.8, 0.7333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 1.0, 0.9333333333333333, 0.9333333333333333, 1.0, 1.0, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.7333333333333333, 0.8, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 0.7333333333333333, 0.8666666666666667, 0.7333333333333333, 0.8666666666666667, 0.8666666666666667, 0.7333333333333333, 0.8, 0.6666666666666666, 0.6, 0.4666666666666667, 0.4666666666666667, 0.6])
    y8 = np.array([0.9333333333333333, 0.5333333333333333, 0.6, 0.9333333333333333, 0.8, 0.9333333333333333, 0.7333333333333333, 1.0, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 0.7333333333333333, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8, 1.0, 0.8, 0.9333333333333333, 0.5333333333333333, 1.0, 0.9333333333333333, 0.8666666666666667, 0.8, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 0.8, 0.8, 0.8666666666666667, 0.8, 0.8666666666666667, 0.8, 0.8666666666666667, 1.0, 0.9333333333333333, 1.0, 1.0, 1.0, 0.9333333333333333, 0.8, 1.0, 0.9333333333333333, 0.9333333333333333, 1.0, 1.0, 1.0, 1.0, 0.8, 0.8666666666666667, 1.0, 0.9333333333333333, 0.8666666666666667, 0.9333333333333333, 1.0, 0.8666666666666667, 1.0, 1.0, 1.0, 0.9333333333333333, 1.0, 1.0, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.8, 0.9333333333333333, 0.5333333333333333, 0.5333333333333333, 0.9333333333333333, 0.8, 0.7333333333333333, 0.8, 0.4666666666666667, 0.6, 0.3333333333333333, 0.3333333333333333, 0.4666666666666667, 0.4666666666666667])
    y9 = np.array([0.4, 0.4666666666666667, 0.8666666666666667, 1.0, 0.9333333333333333, 0.4, 0.8, 0.8666666666666667, 0.7333333333333333, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 0.8, 0.8, 0.8, 0.7333333333333333, 0.8666666666666667, 0.9333333333333333, 0.9333333333333333, 0.8, 0.8666666666666667, 0.9333333333333333, 0.8, 0.9333333333333333, 0.8, 0.8666666666666667, 0.9333333333333333, 1.0, 0.8666666666666667, 0.8, 0.8, 1.0, 0.9333333333333333, 0.8666666666666667, 1.0, 0.9333333333333333, 0.8666666666666667, 0.7333333333333333, 0.6666666666666666, 0.9333333333333333, 0.9333333333333333, 0.8, 1.0, 0.8666666666666667, 0.9333333333333333, 0.9333333333333333, 1.0, 0.8, 1.0, 0.9333333333333333, 0.8666666666666667, 0.6666666666666666, 1.0, 1.0, 0.8666666666666667, 0.7333333333333333, 1.0, 0.9333333333333333, 0.8, 0.8666666666666667, 0.8666666666666667, 1.0, 0.9333333333333333, 1.0, 0.8, 0.6666666666666666, 0.6, 0.8, 0.6666666666666666, 0.7333333333333333, 0.4666666666666667, 0.6666666666666666, 0.8, 0.3333333333333333, 0.6666666666666666, 0.3333333333333333, 0.6, 0.6666666666666666])
    y10 = np.array([0.8, 0.6666666666666666, 0.8, 0.8666666666666667, 0.9333333333333333, 0.5333333333333333, 1.0, 0.9333333333333333, 0.7333333333333333, 0.5333333333333333, 0.8666666666666667, 0.6, 0.9333333333333333, 1.0, 1.0, 0.9333333333333333, 0.8, 0.6666666666666666, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.9333333333333333, 0.6666666666666666, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 1.0, 0.8666666666666667, 0.8666666666666667, 0.5333333333333333, 0.8666666666666667, 0.8666666666666667, 0.6666666666666666, 0.9333333333333333, 0.9333333333333333, 1.0, 0.8666666666666667, 0.7333333333333333, 0.9333333333333333, 0.9333333333333333, 1.0, 0.9333333333333333, 0.9333333333333333, 1.0, 1.0, 0.7333333333333333, 0.8666666666666667, 1.0, 1.0, 0.7333333333333333, 1.0, 0.8, 0.8666666666666667, 1.0, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 1.0, 0.9333333333333333, 0.8666666666666667, 1.0, 1.0, 0.8666666666666667, 0.8, 0.9333333333333333, 1.0, 0.9333333333333333, 0.8, 0.8, 0.8, 0.6666666666666666, 0.7333333333333333, 0.8, 0.5333333333333333, 0.8, 0.7333333333333333, 0.5333333333333333, 0.4666666666666667])
    y11 = np.array([0.8, 0.9333333333333333, 0.6, 0.8, 1.0, 0.6, 0.8, 0.9333333333333333, 1.0, 1.0, 0.8666666666666667, 0.8, 0.3333333333333333, 0.7333333333333333, 0.8666666666666667, 0.6, 0.9333333333333333, 0.8, 0.7333333333333333, 0.8666666666666667, 0.6, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 1.0, 0.8666666666666667, 0.8666666666666667, 0.7333333333333333, 0.8, 1.0, 0.26666666666666666, 0.9333333333333333, 1.0, 0.6666666666666666, 1.0, 0.9333333333333333, 1.0, 0.6666666666666666, 0.9333333333333333, 1.0, 0.9333333333333333, 1.0, 0.8, 0.9333333333333333, 1.0, 0.8666666666666667, 0.9333333333333333, 0.7333333333333333, 0.8, 0.8, 0.9333333333333333, 1.0, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 1.0, 0.9333333333333333, 0.8666666666666667, 1.0, 0.6, 1.0, 1.0, 0.9333333333333333, 0.8, 0.8, 1.0, 0.8, 0.8, 0.8, 0.9333333333333333, 0.6, 0.6, 0.7333333333333333, 0.6666666666666666, 0.6, 0.4666666666666667, 0.7333333333333333, 0.4])


    max_y = []
    min_y = []
    for k in range(80):
        max_num = max(y0[k], y1[k], y2[k], y3[k], y4[k], y5[k], y6[k], y7[k], y8[k], y9[k], y10[k], y11[k])
        min_num = min(y0[k], y1[k], y2[k], y3[k], y4[k], y5[k], y6[k], y7[k], y8[k], y9[k], y10[k], y11[k])
        max_y.append(max_num)
        min_y.append(min_num)
    r1 = (y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 - np.array(min_y)) / 11

    y0 = np.array([0.9, 0.8, 0.7666666666666667, 0.36666666666666664, 0.7666666666666667, 0.9, 0.9666666666666667, 0.6333333333333333, 1.0, 0.8666666666666667, 0.8666666666666667, 0.9666666666666667, 0.9, 0.8666666666666667, 0.8, 0.9666666666666667, 0.9333333333333333, 0.6666666666666666, 0.8333333333333334, 0.8666666666666667, 0.9666666666666667, 0.9, 0.8666666666666667, 1.0, 0.9666666666666667, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9666666666666667, 0.9333333333333333, 1.0, 0.8333333333333334, 0.9333333333333333, 1.0, 0.9666666666666667, 1.0, 0.9666666666666667, 0.9333333333333333, 0.8666666666666667, 0.9333333333333333, 0.9, 0.9333333333333333, 0.8666666666666667, 0.9, 0.9333333333333333, 0.8333333333333334, 0.9, 0.9333333333333333, 0.9666666666666667, 0.9666666666666667, 0.9666666666666667, 0.9666666666666667, 0.9666666666666667, 0.9333333333333333, 0.9333333333333333, 1.0, 1.0, 1.0, 0.9666666666666667, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.9, 0.9333333333333333, 0.9, 0.8666666666666667, 0.8666666666666667, 1.0, 0.7666666666666667, 0.8666666666666667, 0.8333333333333334, 0.7666666666666667, 0.7, 0.7, 0.6666666666666666, 0.5333333333333333, 0.6333333333333333, 0.7666666666666667])
    y1 = np.array([0.9333333333333333, 1.0, 0.8666666666666667, 0.9, 1.0, 0.9, 0.9333333333333333, 0.9, 0.7666666666666667, 0.6666666666666666, 0.9666666666666667, 0.6, 0.9333333333333333, 0.9333333333333333, 0.8666666666666667, 0.9666666666666667, 0.9333333333333333, 1.0, 0.8333333333333334, 0.9666666666666667, 0.9666666666666667, 0.9, 0.8666666666666667, 0.9333333333333333, 0.8, 0.9333333333333333, 0.9, 0.9333333333333333, 0.9666666666666667, 1.0, 0.9, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 0.8333333333333334, 0.9, 0.9666666666666667, 0.8666666666666667, 0.9333333333333333, 1.0, 0.9666666666666667, 0.9333333333333333, 0.8333333333333334, 0.9333333333333333, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 1.0, 0.9, 0.8333333333333334, 0.9333333333333333, 1.0, 0.9, 0.9666666666666667, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 1.0, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.8333333333333334, 0.8, 0.9666666666666667, 0.8666666666666667, 0.8, 0.8333333333333334, 0.8333333333333334, 0.6333333333333333, 0.6, 0.6, 0.6333333333333333, 0.5333333333333333, 0.7333333333333333, 0.43333333333333335])
    y2 = np.array([0.7666666666666667, 0.9, 0.8333333333333334, 0.8666666666666667, 0.8333333333333334, 0.8666666666666667, 0.9, 0.8333333333333334, 0.8666666666666667, 0.9, 0.7333333333333333, 0.6666666666666666, 0.9333333333333333, 0.9, 0.6666666666666666, 0.9333333333333333, 1.0, 0.9666666666666667, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.9, 0.8333333333333334, 1.0, 0.7666666666666667, 0.9, 0.9, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9, 1.0, 0.9666666666666667, 0.9, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 1.0, 0.9, 1.0, 0.9666666666666667, 0.9333333333333333, 0.9333333333333333, 0.9666666666666667, 0.9666666666666667, 1.0, 0.9, 0.9666666666666667, 0.9, 0.9666666666666667, 0.9666666666666667, 0.9333333333333333, 0.8666666666666667, 0.9, 0.9666666666666667, 0.9666666666666667, 0.8666666666666667, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.8333333333333334, 0.9333333333333333, 0.9333333333333333, 0.9, 0.8, 0.7666666666666667, 0.9, 0.7, 0.7, 0.7666666666666667, 0.6666666666666666, 0.4, 0.43333333333333335])
    y3 = np.array([0.8666666666666667, 0.9, 0.9666666666666667, 0.7, 0.7, 0.9, 0.7, 0.9666666666666667, 0.8, 1.0, 0.9666666666666667, 0.9, 0.9, 0.8, 0.9666666666666667, 0.9333333333333333, 1.0, 0.9333333333333333, 1.0, 0.9666666666666667, 0.7, 1.0, 0.8333333333333334, 0.9333333333333333, 0.9666666666666667, 0.7333333333333333, 0.9666666666666667, 1.0, 0.7333333333333333, 0.9, 0.9666666666666667, 0.9, 0.9, 0.8, 0.7666666666666667, 0.9333333333333333, 0.9, 0.9333333333333333, 0.8666666666666667, 0.9666666666666667, 0.9, 0.8666666666666667, 1.0, 1.0, 0.9, 0.9333333333333333, 0.8666666666666667, 1.0, 0.9666666666666667, 0.9333333333333333, 1.0, 0.8, 0.9333333333333333, 0.9, 0.9333333333333333, 0.9666666666666667, 0.9, 0.8, 0.9666666666666667, 0.8666666666666667, 0.9666666666666667, 0.9, 0.9, 0.9333333333333333, 0.9, 0.9333333333333333, 0.9, 0.8666666666666667, 0.9, 0.8, 0.9, 0.7666666666666667, 0.6666666666666666, 0.8, 0.7333333333333333, 0.8333333333333334, 0.6333333333333333, 0.7, 0.7333333333333333, 0.5333333333333333])
    y4 = np.array([0.9333333333333333, 0.9, 0.9666666666666667, 0.8, 0.9333333333333333, 0.7333333333333333, 0.7333333333333333, 0.9666666666666667, 0.7333333333333333, 0.8666666666666667, 0.9, 0.9666666666666667, 0.9, 1.0, 0.9, 0.8666666666666667, 0.7, 0.8666666666666667, 0.9333333333333333, 1.0, 0.8333333333333334, 0.9, 0.9333333333333333, 0.9666666666666667, 0.7666666666666667, 0.8666666666666667, 0.8, 0.9666666666666667, 0.8666666666666667, 1.0, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.8333333333333334, 0.9666666666666667, 0.9, 0.8333333333333334, 0.9333333333333333, 0.9666666666666667, 0.9, 1.0, 1.0, 0.9333333333333333, 0.9333333333333333, 0.8666666666666667, 0.9666666666666667, 0.8666666666666667, 0.9333333333333333, 0.9666666666666667, 0.8666666666666667, 0.9666666666666667, 0.9666666666666667, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 1.0, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 0.9, 0.9666666666666667, 0.9, 0.9, 0.9333333333333333, 0.8333333333333334, 0.8333333333333334, 0.8666666666666667, 0.8, 0.8666666666666667, 0.6, 0.8, 0.7333333333333333, 0.6, 0.4, 0.6666666666666666, 0.6333333333333333])
    y5 = np.array([0.9, 0.8666666666666667, 0.8, 0.9, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.6666666666666666, 0.7666666666666667, 0.9333333333333333, 0.9, 0.9333333333333333, 0.9, 0.8666666666666667, 0.7, 0.8333333333333334, 1.0, 0.9666666666666667, 0.8, 0.9, 0.8666666666666667, 0.9666666666666667, 0.8666666666666667, 0.9333333333333333, 0.8666666666666667, 1.0, 0.9, 0.8666666666666667, 0.9, 0.7666666666666667, 0.9, 0.9666666666666667, 0.9333333333333333, 0.9333333333333333, 0.8333333333333334, 1.0, 0.9666666666666667, 0.8333333333333334, 0.9666666666666667, 0.9, 0.9333333333333333, 0.9, 0.8666666666666667, 0.9333333333333333, 0.8, 1.0, 0.9, 0.8333333333333334, 1.0, 0.8666666666666667, 0.9666666666666667, 0.9333333333333333, 1.0, 0.8666666666666667, 1.0, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9, 0.8333333333333334, 0.9333333333333333, 0.9333333333333333, 0.9, 0.8666666666666667, 0.9, 0.9, 0.6666666666666666, 0.8666666666666667, 0.6, 0.6333333333333333, 0.7333333333333333, 0.6333333333333333, 0.5, 0.7, 0.5333333333333333])
    y6 = np.array([0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.8, 0.7333333333333333, 0.7333333333333333, 0.9666666666666667, 0.8, 0.8333333333333334, 1.0, 0.7666666666666667, 0.7666666666666667, 1.0, 0.6333333333333333, 0.9, 0.6666666666666666, 0.8666666666666667, 0.7666666666666667, 0.9666666666666667, 0.6666666666666666, 0.7666666666666667, 0.9, 1.0, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9666666666666667, 0.9333333333333333, 0.8666666666666667, 0.9666666666666667, 1.0, 0.9666666666666667, 0.9333333333333333, 0.8333333333333334, 0.8666666666666667, 1.0, 0.9, 0.8333333333333334, 0.9666666666666667, 0.9333333333333333, 0.9, 0.9, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 1.0, 0.9666666666666667, 0.9, 0.9333333333333333, 0.9, 0.9333333333333333, 0.9333333333333333, 0.8666666666666667, 0.9666666666666667, 1.0, 0.8666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9666666666666667, 0.9666666666666667, 0.8666666666666667, 0.9666666666666667, 0.8333333333333334, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.8, 0.8, 0.9333333333333333, 0.8666666666666667, 0.6333333333333333, 0.8333333333333334, 0.8666666666666667, 0.6, 0.7666666666666667, 0.5666666666666667, 0.6, 0.5666666666666667])
    y7 = np.array([1.0, 0.9666666666666667, 0.9666666666666667, 0.9666666666666667, 0.9666666666666667, 0.8666666666666667, 0.8333333333333334, 0.8, 0.8666666666666667, 0.8666666666666667, 0.7333333333333333, 0.9, 0.7333333333333333, 0.7666666666666667, 0.8333333333333334, 0.9, 0.9666666666666667, 0.8, 0.9333333333333333, 0.8, 0.8333333333333334, 1.0, 0.7333333333333333, 0.9333333333333333, 0.7666666666666667, 0.9666666666666667, 0.8333333333333334, 0.9666666666666667, 0.9, 0.8, 0.9333333333333333, 0.8666666666666667, 0.9, 0.9333333333333333, 0.9, 0.9, 0.9666666666666667, 0.8333333333333334, 0.8, 1.0, 1.0, 0.9333333333333333, 0.9, 0.9666666666666667, 0.9333333333333333, 0.8666666666666667, 0.9, 0.9, 0.9333333333333333, 1.0, 0.9, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.8666666666666667, 0.8666666666666667, 0.9333333333333333, 0.8333333333333334, 0.9666666666666667, 0.9333333333333333, 0.9, 0.9333333333333333, 0.8333333333333334, 0.9666666666666667, 0.8666666666666667, 0.8333333333333334, 0.8666666666666667, 0.8333333333333334, 0.8, 0.8333333333333334, 0.8333333333333334, 0.8, 0.6, 0.7666666666666667, 0.9, 0.6, 0.7333333333333333])
    y8 = np.array([0.8666666666666667, 0.8333333333333334, 0.8666666666666667, 0.8, 0.9333333333333333, 0.9, 0.8333333333333334, 0.8, 0.9333333333333333, 0.9, 0.9333333333333333, 0.8333333333333334, 1.0, 0.9333333333333333, 0.9, 1.0, 0.7333333333333333, 0.9, 0.8333333333333334, 0.8333333333333334, 0.9333333333333333, 0.9, 0.8666666666666667, 0.8, 1.0, 0.9, 0.8, 0.8333333333333334, 0.8666666666666667, 0.8, 0.8333333333333334, 0.9333333333333333, 0.9, 0.9666666666666667, 0.9333333333333333, 0.9333333333333333, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9666666666666667, 0.9666666666666667, 0.9666666666666667, 0.9666666666666667, 0.9333333333333333, 0.8333333333333334, 0.9666666666666667, 0.9, 0.9, 0.9666666666666667, 0.8666666666666667, 0.9666666666666667, 0.9666666666666667, 1.0, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 1.0, 0.9, 0.9, 1.0, 0.9, 0.8333333333333334, 0.8333333333333334, 0.9333333333333333, 0.9, 0.8333333333333334, 0.8666666666666667, 0.7, 0.8, 0.8, 0.8, 0.7666666666666667, 0.7666666666666667, 0.6333333333333333, 0.6])
    y9 = np.array([0.9666666666666667, 0.8, 0.9333333333333333, 0.6333333333333333, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 1.0, 1.0, 0.7, 0.9, 0.8666666666666667, 0.9666666666666667, 0.9666666666666667, 0.8666666666666667, 0.9, 0.9, 0.9, 0.6333333333333333, 0.9333333333333333, 0.7666666666666667, 0.9666666666666667, 0.9666666666666667, 0.8, 0.9333333333333333, 0.8666666666666667, 1.0, 0.9333333333333333, 0.9, 0.8, 0.9666666666666667, 0.8666666666666667, 0.7666666666666667, 0.9, 0.9, 0.8, 0.9666666666666667, 0.9333333333333333, 0.8, 0.8, 0.9333333333333333, 0.8333333333333334, 0.9333333333333333, 0.9333333333333333, 1.0, 0.9666666666666667, 0.9, 0.9666666666666667, 1.0, 0.9, 0.9666666666666667, 0.9666666666666667, 0.9666666666666667, 1.0, 1.0, 0.9333333333333333, 1.0, 0.9666666666666667, 0.9333333333333333, 1.0, 1.0, 0.9333333333333333, 0.8333333333333334, 0.9, 0.7666666666666667, 0.8333333333333334, 0.9333333333333333, 0.8666666666666667, 0.9333333333333333, 0.8333333333333334, 0.8333333333333334, 0.8, 0.9333333333333333, 0.6666666666666666, 0.7, 0.6666666666666666, 0.5333333333333333, 0.5666666666666667, 0.5666666666666667, 0.5666666666666667])
    y10 = np.array([0.8666666666666667, 0.7666666666666667, 0.7666666666666667, 0.8666666666666667, 0.9, 0.7666666666666667, 0.8, 0.9333333333333333, 0.9666666666666667, 0.9, 0.7333333333333333, 0.8333333333333334, 0.9333333333333333, 0.9666666666666667, 0.9666666666666667, 1.0, 0.8, 0.9666666666666667, 0.9, 1.0, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 0.9333333333333333, 0.9, 0.9333333333333333, 0.9, 1.0, 0.9333333333333333, 0.8666666666666667, 0.8, 0.9333333333333333, 0.7333333333333333, 1.0, 0.9333333333333333, 0.9666666666666667, 0.9666666666666667, 0.8333333333333334, 0.8333333333333334, 0.8666666666666667, 0.8333333333333334, 0.9333333333333333, 0.9333333333333333, 1.0, 0.8666666666666667, 0.8666666666666667, 0.9666666666666667, 0.9666666666666667, 0.9666666666666667, 0.8333333333333334, 0.9, 0.9666666666666667, 1.0, 1.0, 0.9666666666666667, 1.0, 0.9, 0.9666666666666667, 0.9666666666666667, 0.9, 0.9666666666666667, 0.9, 0.9333333333333333, 0.8666666666666667, 0.9333333333333333, 0.9, 0.9, 0.9, 0.7, 0.8666666666666667, 0.8, 0.7333333333333333, 0.8666666666666667, 0.6666666666666666, 0.7333333333333333, 0.6333333333333333, 0.7333333333333333, 0.5666666666666667, 0.6333333333333333, 0.7333333333333333])
    y11 = np.array([0.7333333333333333, 0.8, 0.9333333333333333, 0.7333333333333333, 0.5333333333333333, 0.7, 0.8333333333333334, 0.8333333333333334, 0.5666666666666667, 0.7, 0.9333333333333333, 1.0, 0.9333333333333333, 0.9, 0.8666666666666667, 1.0, 0.8333333333333334, 0.9, 0.8666666666666667, 0.8, 0.9, 1.0, 0.9, 1.0, 0.8333333333333334, 0.9666666666666667, 0.8666666666666667, 0.7666666666666667, 0.9333333333333333, 0.9333333333333333, 0.7666666666666667, 0.8333333333333334, 0.9333333333333333, 0.9666666666666667, 0.9333333333333333, 0.8, 1.0, 1.0, 0.8666666666666667, 0.7333333333333333, 0.9666666666666667, 0.8333333333333334, 0.9333333333333333, 1.0, 1.0, 0.9, 0.9, 1.0, 0.9666666666666667, 0.9666666666666667, 0.9333333333333333, 1.0, 0.9666666666666667, 0.9333333333333333, 0.9666666666666667, 0.9, 0.9, 0.9333333333333333, 1.0, 0.8666666666666667, 0.9, 0.9666666666666667, 0.8, 0.9333333333333333, 0.9666666666666667, 0.9666666666666667, 0.9333333333333333, 0.9, 0.9, 0.8666666666666667, 0.8333333333333334, 0.8666666666666667, 0.8666666666666667, 0.8333333333333334, 0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 0.6333333333333333, 0.6666666666666666, 0.7])

    max_y = []
    min_y = []
    for k in range(80):
        max_num = max(y0[k], y1[k], y2[k], y3[k], y4[k], y5[k], y6[k], y7[k], y8[k], y9[k], y10[k], y11[k])
        min_num = min(y0[k], y1[k], y2[k], y3[k], y4[k], y5[k], y6[k], y7[k], y8[k], y9[k], y10[k], y11[k])
        max_y.append(max_num)
        min_y.append(min_num)
    r2 = (y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 - np.array(min_y)) / 11



x = np.arange(10, 90, 1)

plt.xlabel("Crop Rate(%)")
# 显示纵轴标签
plt.ylabel("Fidelity")
# 显示图标题
#plt.title("Fedility Viriation")
#plt.xlim(0.1,0.9)
plt.ylim(0.59,1.0)
plt.xlim(9,90)


f1 = np.polyfit(x, r1, 4)
f2 = np.polyfit(x, r2, 4)
p1 = np.poly1d(f1)
p2 = np.poly1d(f2)
yvals1 = p1(x)
yvals2 = p2(x)

plt.plot(x, yvals1, color = "#fcb001")
plt.plot(x, yvals2)

#plt.hist(r3,bins=80)
plt.bar(x, r2, alpha=0.6, width=1, edgecolor = "black", label = "NABOC=6")
plt.bar(x, r1, alpha=0.6, width=1, color = "#fcb001", edgecolor = "black", label = "NABOC=3")


plt.legend(loc=1)

plt.savefig("2-layer.jpg", dpi=1800, bbox_inches='tight')

plt.show()
