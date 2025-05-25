import pyautogui
import psutil
import time
from pynput import mouse
from threading import Thread, Event

def is_tibia_running():
    return any(process.info['name'].lower() == 'client.exe' for process in psutil.process_iter(['name']))

def press_key_while_pressed(key, event):
    while not event.is_set():
        if is_tibia_running():
            pyautogui.press(key)
        time.sleep(0.001)  

def on_click(x, y, button, pressed, events):
    if button == mouse.Button.x2:  # MB5
        if pressed:
            events['mb5'].clear()
            Thread(target=press_key_while_pressed, args=('=', events['mb5']), daemon=True).start()
        else:
            events['mb5'].set()
    elif button == mouse.Button.x1:  # MB4
        if pressed:
            events['mb4'].clear()
            Thread(target=press_key_while_pressed, args=('-', events['mb4']), daemon=True).start()
        else:
            events['mb4'].set()
    elif button == mouse.Button.middle:  # Clique do scroll
        if pressed:
            events['middle'].clear()
            Thread(target=press_key_while_pressed, args=('k', events['middle']), daemon=True).start()
        else:
            events['middle'].set()

def main():
    events = {
        'mb5': Event(),
        'mb4': Event(),
        'middle': Event()
    }
    
    listener = mouse.Listener(on_click=lambda x, y, button, pressed: on_click(x, y, button, pressed, events))
    listener.start()

    try:
        while True:
            if is_tibia_running():
                time.sleep(1)
            else:
                listener.stop()
                break
    except KeyboardInterrupt:
        listener.stop()

if __name__ == "__main__":
    main()
