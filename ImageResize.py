from PIL import Image

# Remaps a value from one range to another
def remap(val, old_min, old_max, new_min, new_max):
    pass


# Basically a wrapper class for PIL's Image class
class ResizableImage:
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.image = Image.open(self.filepath)
        self.tmp_file = filepath

    
    def resize_image(self, factor):
        self.image 