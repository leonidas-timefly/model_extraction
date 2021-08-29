import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import math
from keras.preprocessing import image
from keras_vggface import utils

nb_class = 5

sample_gap = 250
coeff_sample = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
x = np.arange(0, 25088, sample_gap)
print(x.shape)
value_sum = np.array([0, 0, 0, 0, 0])

feature_value1 = np.load("Train_data_set/UMass/train_set_class" + str(1) + ".npy")
feature_value2 = np.load("Train_data_set/UMass/train_set_class" + str(2) + ".npy")
feature_value3 = np.load("Train_data_set/UMass/train_set_class" + str(3) + ".npy")
feature_value4 = np.load("Train_data_set/UMass/train_set_class" + str(4) + ".npy")
feature_value5 = np.load("Train_data_set/UMass/train_set_class" + str(5) + ".npy")

for k in range(0, 20):
    list1 = feature_value5[k].tolist()
    img = utils.postprocess_input(list1, version=1)
    img = image.array_to_img(img)
    image.save_img("results/pictures/UMass/Vgg16/5/class5/class" + str(k) + "photo.jpg", img)





feature_value1 = feature_value1.astype(int)
feature_value2 = feature_value2.astype(int)
feature_value3 = feature_value3.astype(int)
feature_value4 = feature_value4.astype(int)
feature_value5 = feature_value5.astype(int)
eff = 2


'''
for k in range(0, 20):
    feature_value = [feature_value5[k][100 * (eff - 1):100 * eff + 1]]
    print(feature_value)
    plt.matshow(feature_value, cmap=plt.cm.binary)  # 这里设置颜色为红色，也可以设置其他颜色
    #plt.title("matrix A")
    plt.yticks([])
    plt.savefig("results/pictures/UMass/Vgg16/5/class5/class" + str(k) + "hotpot.jpg", dpi=1800, bbox_inches='tight')
    plt.show()
'''

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

feature_value = np.load("feature_value/Vgg16/5/TrainFeatureValue20056" + str(1) + ".npy")
feature_value = feature_value[0].astype(int)
print(max(feature_value))
print(feature_value)
print(feature_value.shape)
temp = []
feature_value = [feature_value]

A = np.arange(0, 100).reshape(1, 100)
print(A)
print(A.shape)
plt.matshow(feature_value, cmap=plt.cm.Reds)#这里设置颜色为红色，也可以设置其他颜色
plt.title("matrix A")

plt.show()

while(1):
    pass
#ax.imshow(feature_value,cmap='coolwarm')

plt.matshow(feature_value, cmap=plt.get_cmap('Dark2'))


plt.show()

while(1):
    pass