import numpy as np
from scipy import ndimage, misc
import sys

def global_threshold(img, threshold_value):
    img[img < threshold_value] = 0
    img[img >= threshold_value] = 255
    return img

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    threshold_value = int(sys.argv[3])

    img = ndimage.imread(input_path)
    img = global_threshold(img, threshold_value)
    misc.imsave(output_path, img)
