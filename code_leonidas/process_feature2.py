import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import math

nb_class = 5

sample_gap = 250
coeff_sample = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
x = np.arange(0, 25088, sample_gap)
print(x.shape)

value_sum = np.array([0, 0, 0, 0, 0])

feature_value = np.load("feature_value/Vgg16/5/TrainFeatureValue20056" + str(1) + ".npy")
feature_value = np.int(feature_value[0])
plt.matshow(feature_value, cmap=plt.get_cmap('Dark2'))

plt.show()

while(1):
    pass
for k in range(1, nb_class + 1):
    feature_value = np.load("feature_value/Vgg16/5/TrainFeatureValue20056" + str(k) + ".npy")
    print(feature_value.shape)
    plt.xlabel('Feature Dimension')
    plt.ylabel('Feature Value')
    plt.title("Class " + str(k) + "/" + str(nb_class) + " Features Distribution")
    temp_sum = sum(feature_value[0][::sample_gap])
    for q in range(5):
        #y = feature_value[q][temp][::sample_gap]
        y = feature_value[q][::sample_gap]
        #y = y[::sample_gap]
        coeff_sample[q] = sum(y) / temp_sum
        print(coeff_sample)
        y = y / coeff_sample[q]

        #x = np.arange(0, int(len(temp) / sample_gap))
        x = np.arange(0, len(y))
        plt.plot(x, y, linewidth=1.5, label="C" + str(k) + "P" + str(q) + "FV")

    plt.legend()
    plt.savefig("results/pictures/UMass/Vgg16/5/class" + str(k) + "ffeature.jpg", dpi=1800, bbox_inches='tight')
    plt.show()
