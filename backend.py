import cv2

# Read image
img = cv2.imread("banana/dum.jpg")
cv2.imshow('Frame',img)

# Convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Green Mask
mask_green = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
count_green = 0
for g in mask_green:
    count_green = count_green + list(g).count(255)
print("Green",count_green)

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
# cv2.imshow('Brown mask', mask_brown)
count_brown = 0
for br in mask_brown:
    count_brown = count_brown + list(br).count(255)
print("Brown",count_brown)

# Final Mask
mask_final = mask_green + mask_yellow + mask_brown
# cv2.imshow('mask',mask_final)
result = cv2.bitwise_and(img,img, mask=mask_final)
cv2.imshow('result',result)

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
if gpercent > 0.80:
    print('Raw')
elif brpercent < 0.75 and ypercent < 0.8:
    print('Very Ripe')
elif ypercent > 0.9:
    print('Ripe')
elif brpercent > 0.75:
    print('Fully Ripe')
else:
    print('Unripe')

cv2.waitKey(0)