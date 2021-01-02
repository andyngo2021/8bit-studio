import eel
import time
import tkinter as tk
from tkinter import filedialog
from ImageResize import ResizableImage
# from helper_functions import *

@eel.expose
def closeApp():
    print("bye!")
    exit(0)

@eel.expose
def getFile():
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    f = filedialog.askopenfile()
    f = f.name
    pixelateImage(f, 1)
    # saved as FINAL.png in /target-images/
    # f = f.split('/')[6:]
    # f = "/".join(f)
    print(f)
    print("HELLO WORLD HI HI")
    # return location of file
    return "target-images/FINAL.png"


@eel.expose
def acceptValFromJS(val):
    print("HIDJKSJFK")
    pixelation_scale = 1/int(val)
    loc = "C:/Users/andyn/Desktop/8bit-studio/web/target-images/FINAL.png"
    pixelateImage(loc, pixelation_scale)
    # inverse poggers

def pixelateImage(location, value):
    tmp = ResizableImage(location)
    tmp.pixelate_image(value)


    



# init the folder with all front end stuff
eel.init('web')
eel.start('index.html', size=(800, 600))


# val = eel.sendValToPy()
# print(val)
