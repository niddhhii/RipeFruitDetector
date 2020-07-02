import cv2
import numpy as np

img = cv2.imread('D:\EG\ImageProcessing_Esha\Ripe Fruit Detector-mywork\esha\img7.jpg')
cv2.namedWindow('Original Image')
cv2.imshow('Original Image',img)

mask_green = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
count_green = 0
for g in mask_green:
    count_green = count_green + list(g).count(255)
print("Green",count_green)

mask_yellow = cv2.inRange(hsv, (15,0,0), (36, 255, 255))
count_yellow = 0
for y in mask_yellow:
    count_yellow = count_yellow + list(y).count(255)
print("Yellow",count_yellow)

brown1 = cv2.inRange(hsv, (0,100,20), (17,255,255))
brown2 = cv2.inRange(hsv, (170,100,20), (180,255,255))
mask_brown = cv2.bitwise_or(brown1, brown2)

count_brown = 0
for br in mask_brown:
    count_brown = count_brown + list(br).count(255)
print("Brown",count_brown)

mask_final = mask_green + mask_yellow + mask_brown
