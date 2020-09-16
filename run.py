import sys
import pyautogui

def main(params):
    try:
        while True:
            img = pyautogui.locateCenterOnScreen(params)
            pyautogui.doubleClick(img)
    except:
        pass

if __name__ == "__main__":
    main(sys.argv[1])