import eel
import tkinter as tk
from tkinter import filedialog
from ImageResize import ResizableImage

# Global Variables that are probably unecessary
filename = ""
tmp = ""

def pixelateImage(location, value):
    global tmp
    tmp = ResizableImage(location)
    tmp.pixelate_image(value)

@eel.expose
def closeApp():
    print("Closing 8-Bit Studio...")
    exit(0)

@eel.expose 
def getFile():
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    try:
        f = filedialog.askopenfile()
        f = f.name
        pixelateImage(f, 1)
        global filename
        filename = f
    except:
        pass
    return "target-images/FINAL.png"

@eel.expose
def acceptValFromJS(val):
    #  as value of pixelation scale increases, resolution decreases
    pixelation_scale = 1/int(val)
    pixelateImage(filename, pixelation_scale)

@eel.expose
def getDimensions():
    try:
        _tmp = ResizableImage(filename)
        w, h = _tmp.image.size
        return w, h
    except:
        return None

@eel.expose
def getJSDim(w, h):
    w = int(w)
    h = int(h)
    tmp.resize(w, h)

@eel.expose
def saveFile():
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    file_type = [('PNG', '.png'), ('All Files', '*.*')]
    try:
        f = filedialog.asksaveasfile(filetypes=file_type)
        tmp.save_img(f.name)
    except:
        pass
    

# init frontend folder
eel.init('web')
eel.start('index.html', size=(950, 650))
