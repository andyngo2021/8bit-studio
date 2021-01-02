import eel
import time
import tkinter as tk
from tkinter import filedialog
from ImageResize import ResizableImage

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
    tmp = ResizableImage(f)
    tmp.pixelate_image(0.07) 
    # saved as FINAL.png in /target-images/
    f = f.split('/')[6:]
    f = "/".join(f)
    print(f)
    return "target-images/FINAL.png"


@eel.expose
def acceptValFromJS(val):
    print('got',val)
    # possibly map functions for pixelation scheme
    


# init the folder with all front end stuff
eel.init('web')
eel.start('index.html', size=(800, 600))


# val = eel.sendValToPy()
# print(val)
