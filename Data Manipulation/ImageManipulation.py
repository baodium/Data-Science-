from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm

example_file = ("http://upload.wikimedia.org/wikipedia/commons/7/7d/Dog_face.png")
image = imread(example_file, as_grey = True)
plt.imshow(image, cmap=cm.gray)
plt.show()
print("data type: %s , shape: %s" %(type(image), image.shape))

image2 = image[5:70, 0:70]
plt.imshow(image2, cmap = cm.gray)
plt.show()

image3 = resize(image2, (30, 30), mode='edge')
plt.imshow(image3, cmap=cm.gray)
print("data type: %s, shape: %s " %(type(image3), image3.shape))
image_row = image3.flatten()
print("data type: %s, shape: %s " %(type(image_row), image_row.shape))
