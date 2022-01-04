# control mouse or keybord
import pyautogui
import time
# calculations
from numpy import * 

# Use pil to take screenshots analyze it and make operations
from PIL import ImageGrab
from PIL import ImageOps

restart = (960,606)
dinosaur = (620, 627)

def restartGame():
    pyautogui.click(restart)
    print('i restarted!')

def image_grab():
    # take screenshot of selected area
    box = ( dinosaur[0]+55 , dinosaur[1], dinosaur[0]+145, dinosaur[1]+5)
    image = ImageGrab.grab(box)
    gray = ImageOps.grayscale(image)
    a = array(gray.getcolors())
    # function to make calculations
    # white is 697
    return a.sum()

def pressSpace():
    pyautogui.press('space')



time.sleep(4)
restartGame()
while True:
    image_grab()
    if (image_grab() != 697):
        pressSpace()
    
      
