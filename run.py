import sys
import pyautogui
import time
import random
import winsound

# recom x=756, y=1019

def main(command,*args):
    n = int(input('Set the number of position : '))
    loca = [findpos() for _ in range(n)]
    
    if 'click' in command:
        while True:
            pyautogui.click(random.choice(loca),button='left',clicks=1)
            t = random.randrange(int(command[command.index('click') + 1]),int(command[command.index('click') + 2]))
            print(f'after {t} seconds will be refreshed')
            time.sleep(t)

    elif 'move' in command:
        while True:
            t = random.randrange(int(command[command.index('move') + 1]),int(command[command.index('move') + 2]))
            moveMouse(random.choice(loca),t)
            # time.sleep(t)
    else:
        try:
            while True:
                img = pyautogui.locateCenterOnScreen(params)
                pyautogui.doubleClick(params)
        except:
            pass

def findpos():
    tar_time = time.time() + 2
    while True: 
        if time.time() > tar_time:
            winsound.Beep(440, 250)
            x, y = pyautogui.position()
            return x, y

def moveMouse(pos, duration):
    x, y = pos
    pyautogui.moveTo(x,y,duration)

if __name__ == "__main__":
    main(sys.argv)