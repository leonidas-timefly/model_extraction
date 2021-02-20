'''
from PIL import Image
I = Image.open('p1-6.jpg')
I.show()
L = I.convert('L')
L.show()
L.save('p1-6-1.jpg')
'''
from skimage import io,data
from PIL import Image
img=io.imread('p1-5.jpg')
bdata=img[:,:,2]
io.imshow(bdata)
io.imsave('channel-b.jpg', bdata)
io.show()
