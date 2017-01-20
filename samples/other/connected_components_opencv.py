import cv2
import sys
import matplotlib.pyplot as plt

def connect_components(img):

    #In this case we are using the otsu threshold
    #But that is probably not the generally case
    img = cv2.medianBlur(img, 21)
    img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
    ret, th = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    connectivity = 4
    output = cv2.connectedComponentsWithStats(th, connectivity, cv2.CV_32S)
    return output[1]

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    img = cv2.imread(input_path)

    img = connect_components(img)
    plt.imsave(output_path, img, cmap='spectral')
