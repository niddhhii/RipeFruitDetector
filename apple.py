import cv2
import numpy as np

# Read image
img1 = cv2.imread("app8.jpg")
img = cv2.resize(img1,(512,512))
cv2.imshow('Frame',img)

# Convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# red Mask
mask_red = cv2.inRange(hsv, (155,25,0), (179,255,255))
count_red = 0
for g in mask_red:
    count_red = count_red + list(g).count(255)
print("Red",count_red)

# Brown Mask
brown1 = cv2.inRange(hsv, (0,100,20), (17,255,255))
brown2 = cv2.inRange(hsv, (170,100,20), (180,255,255))
mask_brown = cv2.bitwise_or(brown1, brown2)

count_brown = 0
for br in mask_brown:
    count_brown = count_brown + list(br).count(255)
print("Brown",count_brown)

# Green Mask
mask_green = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
count_green = 0
for g in mask_green:
    count_green = count_green + list(g).count(255)
print("Green",count_green)


 #Yellow Mask
mask_yellow = cv2.inRange(hsv, (15,0,0), (36, 255, 255))
count_yellow = 0
for y in mask_yellow:
    count_yellow = count_yellow + list(y).count(255)
print("Yellow",count_yellow)


#Final Mask
mask_final = mask_green + mask_yellow +  mask_red +mask_brown


res = cv2.bitwise_and(img,img, mask=mask_final)
contours, hierarchy = cv2.findContours(mask_final,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
area = [cv2.contourArea(x) for x in contours]
max_index = np.argmax(area)
maxcontour = contours[max_index]
cv2.drawContours(img,[maxcontour],-1,(0,0,255),10)
cv2.imshow('Frame',img)

# Calculate the total area
total_count = count_green + count_yellow +  count_red + count_brown
print(total_count)

# Calculate % of each colour
gpercent = count_green/total_count
ypercent = count_yellow/total_count
brpercent = count_brown/total_count
rpercent = count_red/total_count
print(gpercent)
print(ypercent)
#print(brpercent)
print(rpercent)

# Conditions for apple fruit scaling

if gpercent<rpercent:
            
        if (rpercent+ypercent) > 0.65:
            print('Ripe')
        elif (brpercent/ypercent) > 6 and (brpercent/ypercent) < 9 :
            print('Rotten')            
        elif (rpercent+brpercent)>0.8:
            print('Very ripe')
        elif (brpercent+rpercent)>ypercent:
            print('Ripe')
        
        elif gpercent > 0.4:
            print('unripe')
        


else:

    if gpercent>0.8:
        print('Green apple: Ripe')
    else:
        print('Unripe')


     
       









cv2.waitKey(0)