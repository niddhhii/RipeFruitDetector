from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk 
import tkinter.ttk as TTK
from tkinter import filedialog 
import cv2
import numpy as np

# Function definitions

# Function to open an image
def img_open():
    global original
    filename = filedialog.askopenfilename(initialdir = '/Users/NidhiDedhia/', title = 'Select an Image', filetypes = (('JPG','*.jpg'),('All files','*.*')))
    original = cv2.imread(filename)
    img = Image.open(filename)
    img = img.resize((500, 300), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(img)
    my_label = Label(canvas,image = my_img)
    my_label.image = my_img
    my_label.place(relx = 0.5, rely = 0.53, anchor = CENTER)
    show_res_btn = Button(canvas, text = "Show Results", command = show_results)
    show_res_btn.place(relx = 0.5, rely = 0.8, relwidth = 0.30, relheight = 0.05, anchor = CENTER)

# Function to retrieve the selected value on clicking dropdown
def dropdown_click(event):
    global selected
    selected = dropdown.get()

# Function to show results
def show_results():
    if selected == 'Banana':
        banana()
    elif selected == 'Mango':
        mango()
    elif selected == 'Orange':
        orange()
    elif selected == 'Papaya':
        papaya()
    elif selected == 'Apple':
        apple()
    show_res = Label(canvas, text=result, font = ('Times New Roman', '15'), bg = 'white')
    show_res.place(relx = 0.5, rely = 0.9, relwidth = 0.50, relheight = 0.05, anchor = CENTER)

# Function for green count
def GreenCount(mask_green):
    count_green = 0
    for g in mask_green:
        count_green = count_green + list(g).count(255)
    return count_green

# Function for yellow count
def YellowCount(mask_yellow):
    count_yellow = 0
    for y in mask_yellow:
        count_yellow = count_yellow + list(y).count(255)
    return count_yellow

# Function for brown count
def BrownCount(mask_brown):
    count_brown = 0
    for br in mask_brown:
        count_brown = count_brown + list(br).count(255)
    return count_brown

# Function for orange count
def OrangeCount(mask_orange):
    count_orange = 0
    for g in mask_orange:
        count_orange = count_orange + list(g).count(255)
    return count_orange

# Function for red count
def RedCount(mask_red):
    count_red = 0
    for y in mask_red:
        count_red= count_red+ list(y).count(255)
    return count_red

# Function for finding and drawing contours
def contour(mask_final):
    res = cv2.bitwise_and(original,original, mask=mask_final)
    contours, hierarchy = cv2.findContours(mask_final,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    area = [cv2.contourArea(x) for x in contours]
    max_index = np.argmax(area)
    maxcontour = contours[max_index]
    cv2.drawContours(original,[maxcontour],-1,(0,255,0),2)
    # cv2.imshow('Frame', original)

# Function for scaling banana fruit
def banana():
    global result

    # Converting bgr image to hsv
    hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)

    # Green Color Mask
    mask_green = cv2.inRange(hsv, (36, 30, 0), (70, 255,255))
    count_green = GreenCount(mask_green)

    # Yellow Color Mask
    mask_yellow = cv2.inRange(hsv, (15,60,0), (36, 255, 255))
    count_yellow = YellowCount(mask_yellow)

    # Brown Color Mask
    brown1 = cv2.inRange(hsv, (0,100,0), (17,255,255))
    brown2 = cv2.inRange(hsv, (165,100,20), (180,255,255))
    mask_brown = cv2.bitwise_or(brown1, brown2)
    count_brown = BrownCount(mask_brown)

    # Final Mask Calculation
    mask_final = mask_green + mask_yellow + mask_brown
    contour(mask_final)

    # Calculating total area
    total_count = count_green + count_yellow + count_brown
    gpercent = count_green/total_count
    ypercent = count_yellow/total_count
    brpercent = count_brown/total_count

    # Conditions for scaling of banana
    if gpercent > 0.8:
        result = "Result : Raw (Scale:1)"
        print('Raw')
    elif brpercent < 0.65 and ypercent < 0.8:
        result = "Result : Very Ripe (Scale:4)"
        print('Very Ripe')
    elif ypercent > 0.9:
        result = "Result : Ripe (Scale:3)"
        print('Ripe')
    elif brpercent > 0.65:
        result = "Result : Over Ripe (Scale:5)"
        print('Over Ripe')
    else:
        result = "Result : Unripe (Scale:2)"
        print('Unripe')


# Function for scaling orange fruit
def orange():
    global result
    hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)

    mask_green = cv2.inRange(hsv, (36, 50, 0), (70, 255,255))
    count_green = GreenCount(mask_green)

    mask_yellow = cv2.inRange(hsv, (21,60,0), (36, 255, 255))
    count_yellow = YellowCount(mask_yellow)

    brown1 = cv2.inRange(hsv, (0,50,0), (9,255,255))
    brown2 = cv2.inRange(hsv, (165,100,20), (180,255,255))
    mask_brown = cv2.bitwise_or(brown1, brown2)
    count_brown = BrownCount(mask_brown)
    
    mask_orange = cv2.inRange(hsv, (10, 50, 20), (20, 255,255))
    count_orange = OrangeCount(mask_orange)

    mask_final = mask_green + mask_orange + mask_yellow + mask_brown
    contour(mask_final)

    total_count = count_green + count_yellow + count_orange + count_brown
    gpercent = count_green/total_count
    opercent = count_orange/total_count
    ypercent = count_yellow/total_count
    brpercent = count_brown/total_count

    if gpercent > 0.75:
        result = "Result : Raw (Scale:1)"
        print('Raw')
    elif opercent > 0.8:
        result = "Result : Ripe (Scale:3)"
        print('Ripe')
    elif opercent < 0.4 and brpercent > 0.4:
        result = "Result : Over Ripe (Scale:5)"
        print('Over Ripe')
    elif opercent > 0.4 and brpercent < 0.4 :
        result = "Result : Very Ripe (Scale:4)"
        print('Very Ripe')
    elif ypercent < 0.75 and opercent < 0.5:
        result = "Result : Unripe (Scale:2)"
        print('Unripe')


# Function for scaling papaya fruit
def papaya():
    global result
    hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)

    mask_green = cv2.inRange(hsv, (36, 30, 0), (70, 255,255))
    count_green = GreenCount(mask_green)

    mask_yellow = cv2.inRange(hsv, (15,80,0), (36, 255, 255))
    count_yellow = YellowCount(mask_yellow)

    brown1 = cv2.inRange(hsv, (0,100,0), (15,255,255))
    brown2 = cv2.inRange(hsv, (165,100,20), (180,255,255))
    mask_brown = cv2.bitwise_or(brown1, brown2)
    count_brown = BrownCount(mask_brown)
    
    mask_final = mask_green + mask_yellow + mask_brown
    contour(mask_final)

    total_count = count_green + count_yellow + count_brown
    gpercent = count_green/total_count
    ypercent = count_yellow/total_count
    brpercent = count_brown/total_count

    if gpercent > 0.75:
        result = "Result : Raw (Scale:1)"
        print('Raw')
    elif brpercent > 0.3:
        result = "Result : Over Ripe (Scale:5)"
        print('Over Ripe')
    elif ypercent > 0.75 and gpercent < 0.1 and brpercent < 0.2:
        result = "Result : Ripe (Scale:3)"
        print('Ripe')
    elif brpercent < 0.3 and ypercent < 0.8:
        result = "Result : Very Ripe (Scale:4)"
        print('Very Ripe')
    elif ypercent > 0.5 and gpercent < 0.3 and brpercent < 0.1:
        result = "Result : Unripe (Scale:2)"
        print('Unripe')


# Function for scaling mango fruit
def mango():
    global result
    hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)

    mask_green = cv2.inRange(hsv, (33, 20, 0), (70, 255,255))
    count_green = GreenCount(mask_green)

    mask_yellow = cv2.inRange(hsv, (13,60,0), (33, 255, 255))
    count_yellow = YellowCount(mask_yellow)

    brown1 = cv2.inRange(hsv, (0,20,20), (13,255,255))
    brown2 = cv2.inRange(hsv, (170,100,20), (180,255,255))
    mask_brown = cv2.bitwise_or(brown1, brown2)
    count_brown = BrownCount(mask_brown)

    mask_final = mask_green + mask_yellow + mask_brown
    contour(mask_final)

    total_count = count_green + count_yellow + count_brown
    gpercent = count_green/total_count
    ypercent = count_yellow/total_count
    brpercent = count_brown/total_count

    if gpercent > 0.75:
        result = "Result : Raw (Scale:1)"
        print('Raw')
    elif brpercent > 0.2:
        result = "Result : Over Ripe (Scale:5)"
        print('Over Ripe')
    elif ypercent < 0.65 and gpercent < 0.5:
        result = "Result : Unripe (Scale:2)"
        print('Unripe')
    elif ypercent < 0.88 and brpercent < 0.2:
        result = "Result : Very Ripe (Scale:4)"
        print('Very Ripe')
    elif ypercent > 0.80:
        result = "Result : Ripe (Scale:3)"
        print('Ripe')


# Function for scaling mango fruit
def apple():
    global result
    hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
        
    red1 = cv2.inRange(hsv, (0,90,25), (10, 255, 255))
    red2 = cv2.inRange(hsv, (170,120,70), (180, 255, 255))
    mask_red = cv2.bitwise_or(red1,red2)
    count_red = RedCount(mask_red)

    brown1 = cv2.inRange(hsv, (10,90,10), (15,255,255))
    brown2 = cv2.inRange(hsv, (165,100,20), (170,255,255))
    mask_brown = cv2.bitwise_or(brown1, brown2)
    count_brown = BrownCount(mask_brown)

    mask_green = cv2.inRange(hsv, (36, 70, 0), (70, 255,255))
    count_green = GreenCount(mask_green)

    mask_yellow = cv2.inRange(hsv, (15,80,15), (36, 255, 255))
    count_yellow = YellowCount(mask_yellow)

    mask_final = mask_green + mask_yellow +  mask_red + mask_brown
    contour(mask_final)

    total_count = count_green + count_yellow +  count_red + count_brown
    gpercent = count_green/total_count
    ypercent = count_yellow/total_count
    brpercent = count_brown/total_count
    rpercent = count_red/total_count

    if gpercent > 0.75:
        result = "Result : Raw (Scale:1)"
        print('Raw')
    elif rpercent > 0.8:
        result = "Result : Ripe (Scale:3)"
        print('Ripe')
    elif rpercent > 0.45 and gpercent < 0.1 and brpercent > 0.4:
        result = "Result : Very Ripe (Scale:4)"
        print('Very Ripe')
    elif brpercent > 0.2 and rpercent < 0.2 and ypercent < 0.6:
        result = "Result : Over Ripe (Scale:5)"
        print('Over Ripe')
    elif rpercent < 0.7 and ypercent > 0.15 and brpercent < 0.3 :
        result = "Result : Unripe (Scale:2)"
        print('Unripe')
    


#GUI
root = tk.Tk()
root.title('Ripe Fruit Detector')

canvas = tk.Canvas(root,height = 700,width = 700,bg = "white")
canvas.pack()

label = tk.Label(canvas, text = 'Select the fruit', font = ('Times New Roman', '15'), bg = 'white')
label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

options = [
    "Select Fruit",
    "Apple",
    "Banana",
    "Mango",
    "Orange",
    "Papaya"
]

dropdown = TTK.Combobox(canvas, value=options, font = ('Consolas', '13'))
dropdown.current(0)
dropdown.bind("<<ComboboxSelected>>",dropdown_click)
dropdown.place(relx = 0.5, rely = 0.16, relwidth = 0.30, relheight = 0.05, anchor = CENTER)

open_img_btn = Button(canvas, text = "Choose an Image", command = img_open)
open_img_btn.place(relx = 0.5, rely = 0.25, relwidth = 0.30, relheight = 0.05, anchor = CENTER)

root.mainloop()