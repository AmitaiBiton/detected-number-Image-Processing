import cv2
import numpy as np

def detect_circles(image_path ,number):
    img = cv2.imread(image_path, 0)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR);
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 2, 15, param1=150, param2=30, minRadius=11, maxRadius=13);
    circles = np.uint16(np.around(circles));
    print(circles)
    for i in circles[0,:]:
        #cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1)
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),4)

    print("number  we  locked :", number)
    print("Number of performances: " , circles.shape[1])
    cv2.imshow('sd' , cimg)
    cv2.waitKeyEx()

if  __name__ == "__main__":
    # the main idea is the number 6 have the max circle in all number so i use to find circle  in open cv
    # and update the range to hi value then i get only six
    number = 6
    cimg = detect_circles("sudoku-original.jpg" , 6)





