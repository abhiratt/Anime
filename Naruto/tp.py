import glob
from PIL import Image


w = glob.glob('Images/*.png')
for index, i in enumerate(w):
    im = Image.open(i)
    im.save('Naruto/'+str(index+1)+'.png')
    width, height = im.size
    newsize = (450, 800)
    im1 = im.resize(newsize)
    im1.save('Naruto/resized/'+str(index)+'.png')
