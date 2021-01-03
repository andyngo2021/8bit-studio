import eel
import tkinter as tk
from tkinter import filedialog
from ImageResize import ResizableImage


@eel.expose
def closeApp():
    print("bye!")
    exit(0)

filename = ""

@eel.expose 
def getFile():
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    f = filedialog.askopenfile()
    f = f.name
    pixelateImage(f, 1)
    global filename
    filename = f
    return "target-images/FINAL.png"


@eel.expose
def acceptValFromJS(val):
    #  inverse poggers!
    #  as value of pixelation scale increases, resolution decreases
    pixelation_scale = 1/int(val)
    pixelateImage(filename, pixelation_scale)

tmp = ""
def pixelateImage(location, value):
    global tmp
    tmp = ResizableImage(location)
    tmp.pixelate_image(value)

@eel.expose
def getDimensions():
    w, h = tmp.image.size
    return w, h

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
    f = filedialog.asksaveasfile(filetypes=file_type)
    tmp.save_img(f.name)

# init the folder with all frontend stuff
eel.init('web')
eel.start('index.html', size=(950, 650))
