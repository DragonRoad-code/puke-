import cv2
import numpy as np
# open camera
camera = cv2.VideoCapture(1)
while True:
    ret,frame = camera.read()
    cv2.imshow('organe',frame)
    # frame change
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bulr=cv2.medianBlur(gray,3)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    closed = cv2.morphologyEx(bulr, cv2.MORPH_CLOSE, kernel)
    opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)
    _,threshold=cv2.threshold(opened,165,255,cv2.THRESH_BINARY)
    canny = cv2.Canny(threshold,50,150)
    # draw shape
    # _, contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # draw=cv2.drawContours(canny, contours, 0, (0, 0, 255), 3)
    #
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        c = sorted(contours, key=cv2.contourArea, reverse=True)[1]
        rect = cv2.minAreaRect(c)
        box = np.int0(cv2.boxPoints(rect))  # box
        draw_img = cv2.drawContours(frame, [box], -1, (0, 0, 255), 3)
        print("box[0]:", box[0])
        print("box[1]:", box[1])
        print("box[2]:", box[2])
        print("box[3]:", box[3])
    else:
        draw_img=frame

    cv2.imshow('canny',canny)
    cv2.imshow('gray',gray)
    cv2.imshow("closed", closed)
    cv2.imshow("opened", opened)
    cv2.imshow("dram_img",draw_img)
    if cv2.waitKey(1) == ord('q'):
        break
# get puke

# correction

# Template matching