import os
from PIL import Image

img_path = 'zhong.jpg'

img = Image.open(img_path)
img2 = img.resize((540, 720))
img2.save("zhong2.jpg", dpi = (72, 72))

#973 728

