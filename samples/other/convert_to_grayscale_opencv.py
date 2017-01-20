import cv2
import sys

def to_gray(img):
    img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
    return img

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    img = cv2.imread(input_path)
    img = to_gray(img)
    cv2.imwrite(output_path, img)
