import keyboard
import pyautogui
from time import sleep
while True:
    if keyboard.is_pressed("`"):
        while not keyboard.is_pressed("`"):
            keyboard.press_and_release("q")
            sleep(0.1)
    if keyboard.is_pressed("["):
        while not keyboard.is_pressed("]"):
            if keyboard.is_pressed("]"):
                break
            pyautogui.click(duration=0)