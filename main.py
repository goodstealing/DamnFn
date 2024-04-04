import keyboard
import pyautogui
import pystray
from pystray import MenuItem as item
from PIL import Image
import sys
import os


def on_key_pressed(event):
    """
    Handling key combinations
    """
    if event.event_type == keyboard.KEY_DOWN:
        if event.name.isdigit() and event.name != '0' and keyboard.is_pressed('f'):
            # Get the number of the F key that needs to be emulated
            f_key = 'f' + event.name
            pyautogui.press(f_key)

        elif event.name == '0' and keyboard.is_pressed('alt'):
            pyautogui.press('f10')
        elif event.name == '1' and keyboard.is_pressed('alt'):
            pyautogui.press('f11')
        elif event.name == '2' and keyboard.is_pressed('alt'):
            pyautogui.press('f12')


def create_tray_icon():
    """
    Create icon for system tray
    """
    icon_path = os.path.join(sys._MEIPASS, "icon.png") if hasattr(sys, '_MEIPASS') else "icon.png"
    icon = Image.open(icon_path)
    menu = (item('Exit', quit_application),)
    return pystray.Icon("name", icon, "DamnFn", menu)


def quit_application(icon):
    """
    Exit app
    """
    icon.stop()


# Set up a keypress event handler
keyboard.on_press(on_key_pressed)

# Create and run icon in system tray
tray = create_tray_icon()
tray.run()
