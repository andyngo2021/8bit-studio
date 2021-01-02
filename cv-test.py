from PIL import Image

img = Image.open('whs.png')
img = img.convert('RGBA')
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1]== 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        if item[0] > 150:
            newData.append((0, 0, 0, 255))
        else:
            newData.append(item)
            print(item)

img.putdata(newData)
img.save('test.png', 'PNG')