import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import math

nb_class = 5

sample_gap = 15
coeff_sample = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
x = np.arange(0, 4096, sample_gap)
print(x.shape)

value_sum = np.array([0, 0, 0, 0, 0])

for k in range(1, nb_class + 1):
    feature_value = np.load("feature_value/Vgg16/5/TrainFeatureValue" + str(k) + ".npy")
    print(feature_value.shape)
    while(1):
        pass
    plt.xlabel('Feature Dimension')
    plt.ylabel('Feature Value')
    plt.title("Class " + str(k) + "/" + str(nb_class) + " Features Distribution")
    temp = []
    with open("class1max&min.txt", "r") as f:
        for line in f:
            temp.append(int(line.split(".")[0]))
    a = sorted(temp)
    temp = np.array(a)
    temp_sum = sum(feature_value[0][temp][::sample_gap])
    for q in range(5):
        y = feature_value[q][temp][::sample_gap]
        #y = y[::sample_gap]
        coeff_sample[q] = sum(y) / temp_sum
        print(coeff_sample)
        y = y / coeff_sample[q]
        x = np.arange(0, int(len(temp) / sample_gap) + 1)
        plt.plot(x, y, linewidth=1.5, label="C" + str(k) + "P" + str(q) + "FV")

    plt.legend()
    plt.savefig("results/pictures/UMass/Vgg16/5/class" + str(k) + "feature.jpg", dpi=1800, bbox_inches='tight')
    plt.show()
    '''
    feature_value = np.load("feature_value/Vgg16/5/TrainFeatureValue" + str(k) + ".npy")
    plt.xlabel('Feature Dimension')
    plt.ylabel('Feature Value')
    plt.title("Class " + str(k) + "/" + str(nb_class) + " Features Distribution")
    for n in range(5):
        coeff_sample[n] = sum(feature_value[n])
    for a in range(1, 5):
        coeff_sample[a] = coeff_sample[a] / coeff_sample[0]
    coeff_sample[0] = 1.0
    for m in range(5):
        y = norm_feature = feature_value[m] / coeff_sample[m]
        #y = norm_feature[::sample_gap]
        #for n in range(len(y)):
            #if y[n] <= 1:
                #continue
            #else:
                #y[n] = math.log(y[n])
        print(norm_feature)
        for t in range(len(y)):
            if 4096 - t > sample_gap and t < sample_gap:
                y[t] = sum(norm_feature[0: t + sample_gap])
                #y[k] /= (t + sample_gap)
            elif 4096 - t > sample_gap and t >= sample_gap:
                y[k] = sum(norm_feature[t - sample_gap: t + sample_gap])
                #y[k] /= (2 * sample_gap)
            else:
                y[k] = sum(norm_feature[t - sample_gap: 4096])
                #y[k] /= (4096 - k*sample_gap)
        print(y.shape)
        y = y[::sample_gap]
        print(y.shape)
        print(y)
        plt.plot(x, y, linewidth=1.5, label="C" + str(k) + "P" + str(m) + "FV")
    #print(value_sum)
    plt.legend()

    plt.savefig("results/pictures/UMass/Vgg16/5/class" + str(k) + "feature.jpg", dpi=1800, bbox_inches='tight')
    plt.show()
    '''