import cv2
import sys

def global_threshold(img, threshold_value):
    ret, thresh = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
    return thresh

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    threshold_value = int(sys.argv[3])

    img = cv2.imread(input_path)
    img = global_threshold(img, threshold_value)
    cv2.imwrite(output_path, img)
