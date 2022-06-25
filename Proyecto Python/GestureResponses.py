#import webBrowser 
from math import e
import webbrowser
import time
import sys
import threading
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import subprocess

from PyQt5.QtCore import endl
keyboard = KeyboardController()
mouse = MouseController()

class GResponses:  

    
    def main(Status_dedos,count):
        
        if Status_dedos['INDEX']==True and Status_dedos['MIDDLE'] and count==2:
            mouse.scroll(0, -0.5)
            print('index and middle')
            
        elif Status_dedos['PINKY']==True and Status_dedos['THUMB']==True and count==2:
            keyboard.press(Key.media_volume_down)
            print('Pinky and THUMB')
            
        elif Status_dedos['INDEX']==True and Status_dedos['MIDDLE']==True and Status_dedos['RING']==True and Status_dedos['THUMB']==True and count==4:
                keyboard.press(Key.media_previous)
                print('THUMB')
                    
        elif Status_dedos['INDEX']==True and Status_dedos['MIDDLE']==True and Status_dedos['RING']==True  and count==3:
                keyboard.press(Key.media_next)
                print('INDEX,MIDDLE,RING')
                
            
        elif Status_dedos['INDEX']==True and count==1:
            mouse.scroll(0, 0.5)
            print("INDEX")
            
        elif Status_dedos['THUMB']==True and count==1:
            
            print("THUMB")
                      
            

        elif Status_dedos['MIDDLE']==True and count==1:
            subprocess.call("taskkill /f /im python.exe", shell=True)
            print('MIDDLE ')
            
        elif Status_dedos['RING']==True and count==1:
            
            print('RING')
            
        
            
        elif Status_dedos['PINKY']==True and count==1:
            keyboard.press(Key.media_volume_up)
            print('PINKY')

    
def confirmation(Status_dedos,count):
    while True:
        if Status_dedos['INDEX']==True and Status_dedos['PINKY'] and count==2:
            break
    pass
        
  
                
        
    

        
            