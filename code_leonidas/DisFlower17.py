import cv2
import numpy as np
import os
from PIL import Image

img_path = 'Datasets/Flower17'
save_path = 'Datasets/Flower17'

with open("flower17.txt", 'r') as f:
    #print(len(f.readlines()))
    k = 0
    for line in f:
        if not k % 80:
            if not os.path.isdir(os.path.join(save_path, str(int(k/80) + 1))):
                os.makedirs(os.path.join(save_path, str(int(k / 80) + 1)))
        img_dir = os.path.join(save_path, line.split("\n")[0])
        print(img_dir)
        img = Image.open(img_dir)
        img.save(os.path.join(os.path.join(save_path, str(int(k/80) + 1)), line.split("\n")[0]))
        k += 1