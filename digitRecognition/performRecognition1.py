# Import the modules
import cv2
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np
import time
# Load the classifier
clf = joblib.load("digits_cls.pkl")

# Read the input image 

cap = cv2.VideoCapture(0)

while 1:
    ret,im = cap.read()
    # cv2.imshow('img',img)
    # Convert to grayscale and apply Gaussian filtering
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

    # Threshold the image
    ret, im_th = cv2.threshold(im_gray, 90, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('im_th',im_th)

    # Find contours in the image
    _, contours, _ = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    # ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get rectangles contains each contour
    rects = [cv2.boundingRect(ctr) for ctr in contours]

    # # For each rectangular region, calculate HOG features and predict
    # # the digit using Linear SVM.
    for rect in rects:
        # Draw the rectangles
        cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3) 
    #     # Make the rectangular region around the digit
    #     leng = int(rect[3] * 1.6)
    #     pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
    #     pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
    #     roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
        
    #     # Resize the image
    #     roi = cv2.resize(im_gray, (28, 28), interpolation=cv2.INTER_AREA)
    #     roi = cv2.dilate(roi, (3, 3))
    #     # Calculate the HOG features
    #     roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
    #     nbr = clf.predict(np.array([roi_hog_fd], 'float64'))
    #     cv2.putText(im, str(int(nbr[0])), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)

    cv2.imshow("Resulting Image with Rectangular ROIs", im)
    # time.sleep(2)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# im = cv2.imread("photo_1.jpg")


# cv2.waitKey()\


cap.release()
cv2.destroyAllWindows()