import tkinter as tk
from tkinter import filedialog

def saveFile():
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    file_type = [('PNG', '.png'), ('All Files', '*.*')]
    f = filedialog.asksaveasfile(filetypes=file_type)
    print(f)

saveFile()