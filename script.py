import eel
import time
import easygui




@eel.expose
def closeApp():
    print("bye!")
    exit(0)

@eel.expose
def getFile():
    filename = easygui.fileopenbox()

# init the folder with all front end stuff
eel.init('web')
eel.start('index.html', size=(800, 600))



