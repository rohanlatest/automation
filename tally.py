import pyautogui
import time

pyautogui.doubleClick(pyautogui.locateOnScreen('icon1.png'))
time.sleep(20)

pyautogui.click(pyautogui.locateOnScreen('icon2.png'))

pyautogui.mouseDown(button='right')
pyautogui.click(pyautogui.locateOnScreen('icon3.png'))


pyautogui.click(pyautogui.locateOnScreen('icon4.png'))

pyautogui.write('Hello world!')

pyautogui.click(pyautogui.locateOnScreen('icon5.png'))