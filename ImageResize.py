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
        print(self.original_w, self.original_h)
        tmp_path = filepath.split('/')
        tmp_path.pop()
        self.new_path = "/".join(tmp_path) + "/"

        self.target_path = os.getcwd().replace('\\', '/') + "/web/target-images/"
        # self.target_path = "/web/target-images/"


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
        tmp_path = self.target_path + tmp_filename
        # print(f'Saving file as {tmp_filename}')
        tmp.save(tmp_path)
        # Pixelating the image
        tmp_img = Image.open(tmp_path)
        print(f'Resizing to these parameters: {self.original_w}x{self.original_h}')
        tmp_img = tmp_img.resize((self.original_w, self.original_h))
        tmp_img.save(self.target_path + 'FINAL.png')
        
        os.remove(tmp_path)

    