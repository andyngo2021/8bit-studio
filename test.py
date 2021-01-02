# from PIL import Image
# im = Image.open('lion.png')
# w,h=im.size
# print(w, h)
# im=im.resize((int(w*0.05), int(h*0.05)))
# im.save('small.png')
# z = Image.open('small.png')
# print(f'Resizing with {w} x {h}')
# z=z.resize((w,h))
# z.save('FINAL.png')

from ImageResize import ResizableImage
import tkinter as tk
from tkinter import filedialog
# from tkinter.filedialog import asksaveasfile 
# implement save folder later

root = tk.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)
folder = filedialog.askopenfile()
print(folder.name)

i = ResizableImage(folder.name)
i.pixelate_image(0.07)