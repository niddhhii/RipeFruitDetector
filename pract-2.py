import cv2
import numpy as np

# Read image
img = cv2.imread("o-3.jpg")
cv2.imshow('Frame',img)

# Convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Green Mask
mask_green = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
count_green = 0
for g in mask_green:
    count_green = count_green + list(g).count(255)
print("Green",count_green)

# Orange Mask
mask_orange = cv2.inRange(hsv, (10, 100, 20), (20, 255,255))
mask2 = cv2.inRange(hsv, (11, 40, 215), (179, 255,255))
count_orange = 0
for g in mask_orange:
    count_orange = count_orange + list(g).count(255)
print("Orange",count_orange)


# Yellow Mask
mask_yellow = cv2.inRange(hsv, (15,0,0), (36, 255, 255))
count_yellow = 0
for y in mask_yellow:
    count_yellow = count_yellow + list(y).count(255)
print("Yellow",count_yellow)

# Brown Mask
brown1 = cv2.inRange(hsv, (0,100,20), (17,255,255))
brown2 = cv2.inRange(hsv, (170,100,20), (180,255,255))
mask_brown = cv2.bitwise_or(brown1, brown2)

count_brown = 0
for br in mask_brown:
    count_brown = count_brown + list(br).count(255)
print("Brown",count_brown)

# Final Mask
mask_final = mask_green + mask_orange + mask_yellow + mask_brown

res = cv2.bitwise_and(img,img, mask=mask_final)
contours, hierarchy = cv2.findContours(mask_green,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
area = [cv2.contourArea(x) for x in contours]
max_index = np.argmax(area)
maxcontour = contours[max_index]
#cv2.drawContours(img,[maxcontour],-1,(0,255,0),10)
#cv2.imshow('Frame1',img)

# Calculate the total area
total_count = count_green + count_yellow + count_orange + count_brown
print(total_count)

# Calculate % of each colour
gpercent = count_green/total_count
opercent = count_orange/total_count
ypercent = count_yellow/total_count
brpercent = count_brown/total_count
print(gpercent)
print(opercent)
print(ypercent)
print(brpercent)

# Conditions for Banana fruit scaling
if gpercent > 0.75:
    print('Raw')
elif gpercent >0.35 and ypercent>0.2:
    print('Unripe')
elif opercent > 0.4 and brpercent > 0.4:
    print('Over Ripe')
elif opercent >0.6 and brpercent < 0.4 :
    print('Very Ripe')
elif opercent < 0.5:
    print('Ripe')

else:
    print('NULL')

cv2.waitKey(0)
'''
# Yellow Mask
mask_yellow = cv2.inRange(hsv, (15,0,0), (36, 255, 255))
count_yellow = 0
for y in mask_yellow:
    count_yellow = count_yellow + list(y).count(255)
print("Yellow",count_yellow)

# Brown Mask
brown1 = cv2.inRange(hsv, (0,100,20), (17,255,255))
brown2 = cv2.inRange(hsv, (170,100,20), (180,255,255))
mask_brown = cv2.bitwise_or(brown1, brown2)

count_brown = 0
for br in mask_brown:
    count_brown = count_brown + list(br).count(255)
print("Brown",count_brown)

# Final Mask
mask_final = mask_green + mask_yellow + mask_brown


res = cv2.bitwise_and(img,img, mask=mask_final)
contours, hierarchy = cv2.findContours(mask_final,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
area = [cv2.contourArea(x) for x in contours]
max_index = np.argmax(area)
maxcontour = contours[max_index]
cv2.drawContours(img,[maxcontour],-1,(0,255,0),10)
cv2.imshow('Frame1',img)

# Calculate the total area
total_count = count_green + count_yellow + count_brown
print(total_count)

# Calculate % of each colour
gpercent = count_green/total_count
ypercent = count_yellow/total_count
brpercent = count_brown/total_count
print(gpercent)
print(ypercent)
print(brpercent)

# Conditions for Banana fruit scaling
if gpercent > 0.75:
    print('Raw')
elif brpercent < 0.75 and ypercent < 0.8:
    print('Very Ripe')
elif ypercent > 0.9:
    print('Ripe')
elif brpercent > 0.8:
    print('Fully Ripe')
else:
    print('Unripe')

cv2.waitKey(0)'''