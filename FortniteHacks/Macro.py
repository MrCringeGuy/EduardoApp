from pynput.keyboard import *
import keyboard

key = Controller()


while True:
    if keyboard.is_pressed('l'):
        key.press('e')
        key.press('r')
        key.release('e', 'r')