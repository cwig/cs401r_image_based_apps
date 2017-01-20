import numpy as np
from scipy import ndimage, misc
import sys
import matplotlib.pyplot as plt

# http://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
def to_gray(img):
    if len(img.shape) == 2 or img.shape[2] == 1:
        #Already gray
        return img
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    img = ndimage.imread(input_path)
    img = to_gray(img)
    misc.imsave(output_path, img)
