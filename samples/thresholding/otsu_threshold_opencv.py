import cv2
import sys

def otsu_threshold(img):
    #convert to grayscale
    img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
    ret, th = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return th

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    img = cv2.imread(input_path)

    img = otsu_threshold(img)
    cv2.imwrite(output_path, img)
