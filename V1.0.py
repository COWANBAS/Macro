import pyautogui
import psutil
import time
from pynput import mouse


def is_tibia_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'Tibia.exe':
            return True
    return False

def press_minus_key():
    pyautogui.press('-')


def press_equal_key():
    pyautogui.press('=')

def press_k_key():
    pyautogui.press('k')

def on_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.button8:  # MB5
            if is_tibia_running():
                press_minus_key()
        elif button == mouse.Button.button7:  # MB4
            if is_tibia_running():
                press_equal_key()
        elif button == mouse.Button.middle:  # Clique do scroll
            if is_tibia_running():
                press_k_key()

listener = mouse.Listener(on_click=on_click)
listener.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    listener.stop()