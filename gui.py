from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk 
import tkinter.ttk as TTK
from tkinter import filedialog 
import cv2
import numpy as np

# Function definitions
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

def dropdown_click(event):
    global selected
    selected = dropdown.get()

def show_results():
    if selected == 'Banana':
        banana()
    elif selected == 'Orange':
        orange()
    show_res = Label(canvas, text=result, font = ('Times New Roman', '15'), bg = 'white')
    show_res.place(relx = 0.5, rely = 0.9, relwidth = 0.50, relheight = 0.05, anchor = CENTER)

def banana():
    global result
    hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)

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
    # cv2.imshow('Brown', mask_brown)
    count_brown = 0
    for br in mask_brown:
        count_brown = count_brown + list(br).count(255)
    print("Brown",count_brown)

    mask_final = mask_green + mask_yellow + mask_brown

    res = cv2.bitwise_and(original,original, mask=mask_final)
    contours, hierarchy = cv2.findContours(mask_final,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    area = [cv2.contourArea(x) for x in contours]
    max_index = np.argmax(area)
    maxcontour = contours[max_index]
    cv2.drawContours(original,[maxcontour],-1,(0,255,0),2)
    # cv2.imshow('Frame1',original)

    total_count = count_green + count_yellow + count_brown
    print(total_count)

    gpercent = count_green/total_count
    ypercent = count_yellow/total_count
    brpercent = count_brown/total_count
    print(gpercent)
    print(ypercent)
    print(brpercent)

    if gpercent > 0.75:
        result = "Result : Raw (Scale:1)"
        print('Raw')
    elif brpercent < 0.75 and ypercent < 0.8:
        result = "Result : Very Ripe (Scale:4)"
        print('Very Ripe')
    elif ypercent > 0.9:
        result = "Result : Ripe (Scale:3)"
        print('Ripe')
    elif brpercent > 0.8:
        result = "Result : Fully Ripe (Scale:5)"
        print('Over Ripe')
    else:
        result = "Result : Unripe (Scale:2)"
        print('Unripe')


def orange():
    global result
    hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)

    mask_green = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
    count_green = 0
    for g in mask_green:
        count_green = count_green + list(g).count(255)
    print("Green",count_green)

    mask_orange = cv2.inRange(hsv, (10, 100, 20), (20, 255,255))
    mask2 = cv2.inRange(hsv, (11, 40, 215), (179, 255,255))
    count_orange = 0
    for g in mask_orange:
        count_orange = count_orange + list(g).count(255)
    print("Orange",count_orange)

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

    mask_final = mask_green + mask_orange + mask_yellow + mask_brown

    res = cv2.bitwise_and(original,original, mask=mask_final)
    contours, hierarchy = cv2.findContours(mask_green,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    area = [cv2.contourArea(x) for x in contours]
    max_index = np.argmax(area)
    maxcontour = contours[max_index]

    total_count = count_green + count_yellow + count_orange + count_brown
    print(total_count)

    gpercent = count_green/total_count
    opercent = count_orange/total_count
    ypercent = count_yellow/total_count
    brpercent = count_brown/total_count
    print(gpercent)
    print(opercent)
    print(ypercent)
    print(brpercent)

    if gpercent > 0.75:
        result = "Result : Raw (Scale:1)"
        print('Raw')
    elif gpercent >0.35 and ypercent>0.2:
        result = "Result : Unripe (Scale:2)"
        print('Unripe')
    elif opercent > 0.4 and brpercent > 0.4:
        result = "Result : Over Ripe (Scale:5)"
        print('Over Ripe')
    elif opercent >0.6 and brpercent < 0.4 :
        result = "Result : Very Ripe (Scale:4)"
        print('Very Ripe')
    elif opercent < 0.5:
        result = "Result : Ripe (Scale:3)"
        print('Ripe')
    else:
        print('NULL')


##################GUI
root = tk.Tk()
root.title('Ripe Fruit Detector')

canvas = tk.Canvas(root,height = 700,width = 700,bg = "white")
canvas.pack()

label = tk.Label(canvas, text = 'Select the fruit', font = ('Times New Roman', '15'), bg = 'white')
label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

options = [
    "Select Fruit",
    "Banana",
    "Orange",
    "Apple"
]

dropdown = TTK.Combobox(canvas, value=options, font = ('Consolas', '13'))
dropdown.current(0)
dropdown.bind("<<ComboboxSelected>>",dropdown_click)
dropdown.place(relx = 0.5, rely = 0.16, relwidth = 0.30, relheight = 0.05, anchor = CENTER)

open_img_btn = Button(canvas, text = "Choose an Image", command = img_open)
open_img_btn.place(relx = 0.5, rely = 0.25, relwidth = 0.30, relheight = 0.05, anchor = CENTER)

cv2.waitKey(0)

root.mainloop()