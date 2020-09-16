import sys
import pyautogui

def main(params):
    try:
        while True:
            img = pyautogui.locateCenterOnScreen(params)
            pyautogui.doubleClick(params)
    except:
        pass

if __name__ == "__main__":
    main(sys.argv[1])