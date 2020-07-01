from tkinter import *
from PIL import ImageTk, Image 
from tkinter import filedialog 
import cv2

my_img = cv2.imread('butterfly.jpg')

def open_img(): 

    global my_img
    x = openfilename() 

    img = Image.open(x) 

    img = img.resize((500, 250), Image.ANTIALIAS) 

    my_img = ImageTk.PhotoImage(img) 

    my_label = Label(image=my_img)
    my_label.pack()

    

def openfilename(): 

    filename = filedialog.askopenfilename(title ='"pen') 

    return filename 

root = Tk()
root.title('Ripe fruit detector')
root.geometry("700x700")




clicked = StringVar()

drop = OptionMenu(root, clicked, 'Apple','Grapes','Banana','Strawberry','Watermelon')
drop.pack()

myButton = Button(root, text = "Open image", command = open_img) .pack()

root.mainloop()