from PIL import Image
from random import randint
import os
import shutil

# Basically a wrapper class for PIL's Image class
class ResizableImage:
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.image = Image.open(self.filepath)
        self.original_w, self.original_h = self.image.size
        tmp_path = filepath.split('/')
        tmp_path.pop()
        self.new_path = "/".join(tmp_path) + "/"

        self.target_path = os.getcwd().replace('\\', '/') + "/web/target-images/"
        self.current_w = None
        self.current_h = None

    def resize(self, w, h):
        # MAYBE TEST
        self.current_w = w
        self.current_h = h
        # 
        tmp_img = self.image.resize((w, h))
        tmp_img.save(self.target_path + 'FINAL.png')
        

    def pixelate_image(self, scale):
        new_w = int(self.original_w*scale)
        new_h = int(self.original_h*scale)
        tmp = self.image.resize((new_w, new_h))
        tmp_filename = f'tmp{int(randint(0,10000))}.png'
        tmp_path = self.target_path + tmp_filename
        tmp.save(tmp_path)

        # Pixelating the image
        tmp_img = Image.open(tmp_path)
        # Resizing image to original size
        if self.current_w is None or self.current_h is None:
            tmp_img = tmp_img.resize((self.original_w, self.original_h))
        else:
            tmp_img = tmp_img.resize((self.current_w, self.current_h))
        tmp_img.save(self.target_path + 'FINAL.png')
        
        os.remove(tmp_path)
    
    def save_img(self, path):
        # basically just need to save FINAL.png to where user wants to save
        final_path = self.target_path + 'FINAL.png'
        shutil.move(final_path, path)
        

    