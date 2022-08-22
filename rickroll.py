import time
import pyautogui
import win32gui, win32con
timer = input("enter time:")
timer = float(timer)
the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
time.sleep(timer)
pyautogui.hotkey("win", "m")
cords = None
while cords is None:
    cords = pyautogui.locateCenterOnScreen("opera.png")
pyautogui.click(cords)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://www.youtube.com/watch?v=FqdmWQ-ACv0")
pyautogui.press("enter")
