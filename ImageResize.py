from PIL import Image
from random import randint
import os
# Remaps a value from one range to another
def remap(val, old_min, old_max, new_min, new_max):
    pass


# Basically a wrapper class for PIL's Image class
class ResizableImage:
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.image = Image.open(self.filepath)
        self.original_w, self.original_h = self.image.size
        tmp_path = filepath.split('/')
        tmp_path.pop()
        self.new_path = "/".join(tmp_path) + "/"

        self.placeholder = ""

    def resize_image(self, scale):
        new_w = int(self.original_w*scale)
        new_h = int(self.original_h*scale)
        tmp = self.image.resize((new_w, new_h))
        tmp_filename = f'tmp{int(randint(0,10000))}.png'
        tmp_path = self.new_path + tmp_filename
        print(f'Saving file as {tmp_filename}')
        tmp.save(tmp_path)

        # then delete tmp?

    def pixelate_image(self, scale):
        new_w = int(self.original_w*scale)
        new_h = int(self.original_h*scale)
        tmp = self.image.resize((new_w, new_h))
        tmp_filename = f'tmp{int(randint(0,10000))}.png'
        tmp_path = self.new_path + tmp_filename
        # print(f'Saving file as {tmp_filename}')
        tmp.save(tmp_path)
        # Pixelating the image
        tmp_img = Image.open(tmp_path)
        tmp_img = tmp_img.resize((self.original_w, self.original_w))
        tmp_img.save('FINAL.png')
        
        os.remove(tmp_path)
