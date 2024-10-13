from Open_App import open_App
from Web_Open import openweb
import pyautogui as gui
from time import sleep

def Open_Brain(text):
    if "website" in text or "open website named" in text:
        text = text.replace("open","").strip()
        text = text.replace("website","").strip()
        text = text.replace("open website named","").strip()
        openweb(text)
    else:
        text = text.replace("open","").strip()
        text = text.replace("app","").strip()
        open_App(text)
        
def close():
    gui.hotkey('alt','f4')
    
    
