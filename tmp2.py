import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)
folder = filedialog.askdirectory()
print(folder)