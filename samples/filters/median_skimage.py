import numpy as np
from scipy import ndimage, misc
import sys
import skimage
from skimage.morphology import disk
from skimage import data
try:
    from skimage import filters
except ImportError:
    from skimage import filter as filters


# http://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
def to_gray(img):
    if len(img.shape) == 2 or img.shape[2] == 1:
        #Already gray
        return img
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]

    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


def median(img, kernal=3):
    img = to_gray(img)
    img = img.astype(np.uint8)
    img = filters.rank.median(img, disk(kernal))

    return img

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    img = ndimage.imread(input_path)
    img = median(img, 21)
    misc.imsave(output_path, img)
