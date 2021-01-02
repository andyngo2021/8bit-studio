from PIL import Image

im = Image.open('lion.png')
w, h = im.size
im = im.resize((w*2, h*2))
im.save('lion.png')
# c.save('cow.png')
# new = im.resize((int(w*0.05), int(h*0.05)))
# new.save('cow1.png')
# w1, h1 = new.size
# new.resize((w1*100, h1*100))

