import keyboard
import pyautogui
from time import sleep
dashOn = False
clickOn = False
while True:
    if keyboard.is_pressed("`"):
        dashOn = not dashOn
        sleep(0.1)
        print(dashOn)     
    if keyboard.is_pressed("["):
        clickOn = not clickOn
        sleep(0.1)
        print(clickOn)
    if dashOn:
        keyboard.press_and_release("q")
        sleep(0.1)
    if clickOn:
        pyautogui.click(duration=0)