import eel
import time
import tkinter as tk
from tkinter import filedialog

@eel.expose
def closeApp():
    print("bye!")
    exit(0)

@eel.expose
def getFile():
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    folder = filedialog.askopenfile()
    print(folder.name)

# init the folder with all front end stuff
eel.init('web')
eel.start('index.html', size=(800, 600))



