from scipy import ndimage, misc
from skimage import data
try:
    from skimage import filters
except ImportError:
    from skimage import filter as filters

import sys

def to_gray(img):
    if len(img.shape) == 2 or img.shape[2] == 1:
        #Already gray
        return img
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def otsu_threshold(img):
    img = to_gray(img)
    threshold_value = filters.threshold_otsu(img)
    img[img < threshold_value] = 0
    img[img >= threshold_value] = 255
    return img

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    img = ndimage.imread(input_path)
    img = otsu_threshold(img)
    misc.imsave(output_path, img)
