import sys
import pyautogui
import time
import random

def main(*args):
    if 'click' in args:
        while True:
            pyautogui.click(pyautogui.position(),button='left',clicks=1)
            t = random.randrange(60)
            print(f'after {t} seconds will be refreshed')
            time.sleep(t)
    else:
        try:
            while True:
                img = pyautogui.locateCenterOnScreen(params)
                pyautogui.doubleClick(params)
        except:
            pass
        
    

if __name__ == "__main__":
    main(sys.argv[1])