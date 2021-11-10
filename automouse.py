import pyautogui
import time
print(pyautogui.size())
pyautogui.moveTo(1,768, duration = 10)
def klikk(): 
    time.sleep(1)     
    pyautogui.click()
 
def a():
    for i in range(50): 
        klikk()
 
a()

