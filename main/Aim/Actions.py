# -*- coding: utf-8 -*- 
import pyautogui
import time
from time import sleep
import pynput
from pynput import keyboard


def MoveMouse(tensor):
    c1 = tuple(tensor[1:3].int()) #Top Left Coordinates
    c2 = tuple(tensor[3:5].int()) #Bottom Right Coordinates
    
    x1, y1 = int(c1[0].item()), int(c1[1].item())
    x2, y2 = int(c2[0].item()), int(c2[1].item())
     
    #Move Mouse to center of rectangle
    width = x2 -  x1
    height = y2 - y1 

    x = x1 + int(width/2)
    y =y1 + int(height/2)
    
    #pri nt("CURRENT MOUSE COORDINATES: ", pyautogui.position())
    #print("MOVE MOUSE TO: ", x, y)
    #pyautogui.moveTo(x, y) #Move
    #pyautogui.moveTo(x, y) #Move
    #sleep(1)
    #pyautogui.click()
    #sleep(1)
    #pyautogui.click(clicks=2) #Click
    #sleep(5)
    
    return 

def on_press(key):
    try: #alphanumeric key
        keypressed = key.char
        print("key: ", keypressed)
    except AttributeError: #special key
        keypressed = key
        print("key: ", keypressed)

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc: # Stop listener    
        return False
KeyPressed = ''    
def on_press(key, StartTime):
    CurrentTime = time.time()
    ScanTime = CurrentTime - StartTime
    
    if ScanTime > 5: #Running for 5 seconds
        listener.stop()
        return
    
    print("ON PRESS")
    try:
        KeyPressed = str(key.char)
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        KeyPressed = str(key)
        print('special key {0} pressed'.format(key))
    return

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def KeyboardInput():
    KeyboardScans=0
    StartTime = time.time()
    print("First KeyPressed: ", KeyPressed)
    # Collect events until released
    #with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    #    listener.join()    
     
    with keyboard.Listener(on_press=on_press(None, StartTime), on_release=on_release) as listener:
        listener.join()  
       
    print("Second KeyPressed: ", KeyPressed)
    
    return KeyPressed

    windll.user32.mouse_event(c_uint(0x0001), c_uint(0), c_uint(y),c_uint(0), c_uint(0))