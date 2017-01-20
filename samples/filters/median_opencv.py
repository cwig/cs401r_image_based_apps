import cv2
import sys

def median(img, kernal=3):
    img = cv2.medianBlur(img, kernal)
    return img

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    img = cv2.imread(input_path)

    img = median(img, 21)
    cv2.imwrite(output_path, img)
