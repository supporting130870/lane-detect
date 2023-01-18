
#흰선을 감지하여 차선으로 인식.
import cv2
import numpy as np

def roi(img,vertices, color3 = (255,255,255), color1 = 255):
    mask = np.zeros_like(img)
    if (len(img.shape) > 2):
        color = color3
    else:
        color = color1

    cv2.fillPoly(mask, vertices, color)
    Roi_img = cv2.bitwise_and(img, mask)
    return Roi_img

def mark_img(image, b = 200, g = 200, r = 200):
    
    bgr = [b,g,r]

    thresholds = (image[:,:,0] < bgr[0]) \
            | (image[:,:,1] < bgr[1]) \
            | (image[:,:,2] < bgr[2])
    mark[thresholds] = [0,0,0]
    return mark

image = cv2.imread("solidWhiteCurve.jpg")
height, width = image.shape[:2]
vertices = np.array([[(50,height),(width/2-45, height/2+60), (width/2+45, height/2+60), (width-50,height)]], dtype=np.int32)
roi_img = roi(image, vertices) 

mark = np.copy(roi_img)
mark = mark_img(roi_img)

cv2.imshow("white", mark)
cv2.imshow('result',image) 
cv2.waitKey(0) 