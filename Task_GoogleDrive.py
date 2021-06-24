# 1 - pip install pyautogui
# 2 - install time

import pyautogui
import time

pyautogui.alert("The code is working. Don't use your computer still the tasks will finished")
pyautogui.PAUSE = 0.75

# Open the Google Drive:
pyautogui.press('winleft')
pyautogui.write('firefox')
pyautogui.press('enter')

# A time-sleep
time.sleep(1)
pyautogui.write('https://drive.google.com')
pyautogui.press('enter')

# Now, in WorkSpace:
pyautogui.hotkey('winleft', 'd')

# Click in file and drag:
pyautogui.moveTo(567, 38)
pyautogui.mouseDown()
pyautogui.moveTo(756, 635)

# Change Page:
pyautogui.hotkey('alt', 'tab')

# Index file in Google Drive:
pyautogui.mouseUp()

# Waiting...
time.sleep(5)

pyautogui.alert("Code is finish. You can back to use computer!")
