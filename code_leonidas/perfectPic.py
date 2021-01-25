from keras_vggface.vggface import VGGFace
from keras_vggface import utils
from keras.preprocessing import image
from keras.engine import Model
from keras.layers import Flatten, Dropout, Dense, Input, Activation
from keras.models import load_model, Sequential
import numpy as np
from keras import backend as K
import sys
import os
import gc
import os
import shutil

os.environ['CUDA_VISIBLE_DEVICES'] = '1'

np.set_printoptions(threshold=np.nan)

RetrainAllLayers = False
newLayers = 1

UMass_Vgg_Path = "Features/UMass/Vgg16"

retrainLayerIndex = -4

retrained_model_path = 'vggface-retrained.h5'

maxAttempt = 4095
nb_class = 5
alpha = 0.1
epoch = 50
initImage = 2   #0:random; 1:a face image; other values:blank

VGGFace_original_model = VGGFace(model='vgg16', pooling='max')
vgg_retrained = load_model(retrained_model_path)

XX = VGGFace_original_model.input
YY = VGGFace_original_model.layers[retrainLayerIndex].output
feature_extractor = Model(XX, YY)

def del_file(filepath):
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

def generate_image(input, model, intermediate_target):
    loss = K.sum(K.square(model.output[0] - intermediate_target[0]))
    gradients = K.gradients(loss, model.input)[0]
    fn = K.function([model.input], [gradients])

    for i in range(1, epoch):
        grads = fn([input])
        input = input - alpha * grads[0]
    return input

def predictor():
    model = Sequential()
    model.add(Flatten(name='test', input_shape=(1,4096)))
    model.add(Activation('relu', name='fc7/relu'))
    if newLayers==1:
        model.add(Dense(nb_class, name='fc8-2'))
        model.add(Activation('softmax', name='fc8-2/softmax'))
    elif newLayers==2:
        model.add(Dense(4096, name='fc8-2'))
        model.add(Activation('relu', name='fc8-2/relu'))
        model.add(Dense(nb_class, name='fc8-2-1'))
        model.add(Activation('softmax', name='fc8-2/softmax'))
    elif newLayers==3:
        model.add(Dense(4096, name='fc8-2'))
        model.add(Activation('relu', name='fc8-2/relu'))
        model.add(Dense(4096, name='fc8-2-1'))
        model.add(Activation('relu', name='fc8-2-1/relu'))
        model.add(Dense(nb_class, name='fc8-2-2'))
        model.add(Activation('softmax', name='fc8-2/softmax'))
    return model

predictor_model = predictor()
predictor_model.load_weights(retrained_model_path, by_name=True)

x = np.zeros(shape=(4096,1,4096))
for i in range(0,4096):
    x[i,0,i] = 10000
preds = predictor_model.predict(x)

del x
gc.collect()
max_index = np.argmax(preds, axis=1)

del_file(filepath = UMass_Vgg_Path+ "/" + str(nb_class))

gc.collect()

for feature_order in range(0, 4096):
    index_ = max_index[feature_order]
    feature_path = os.path.join(UMass_Vgg_Path, str(nb_class))
    if not os.path.isdir(feature_path):
        os.makedirs(feature_path)
    feature_class_path = os.path.join(feature_path, "class" +  str(max_index[feature_order] + 1))
    if not os.path.isdir(feature_class_path):
        os.makedirs(feature_class_path)
    file_name = os.path.join(feature_class_path, str(feature_order) + ".txt")
    print(file_name)

    with open(file_name, 'w') as f:
        #f.write("I love you")
        for feature_value in range(500, 0, -10):

            x = np.zeros(shape=(4096,1,4096))
            x[feature_order, 0, feature_order] = feature_value
            print(feature_order, feature_value)

            preds_all_class = predictor_model.predict(x)
            del x
            gc.collect()
            temp = preds_all_class[feature_order]
            del preds_all_class
            gc.collect()

            print(index_)
            #print(preds_all_class)
            preds_single = temp[index_]
            del temp
            gc.collect()

            print(preds_single)
            #f.write("I love you")
            f.write(str(preds_single) + "\n")