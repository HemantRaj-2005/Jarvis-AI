import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


logging.getLogger('selenium').setLevel(logging.WARNING)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--disable-blink-features=AutomationControl")

chrome_service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=chrome_service,options=chrome_options)

driver.get("https://tts.5e7en.me/")

def speak(text):
    try:
        element_to_click = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="text"]')))
        element_to_click.click()
        
        element_to_click.send_keys(text)
        print(text)
        
        sleep_duration = min(0.2+len(text)//10,15)
        
        button_to_click = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="button"]')))
        button_to_click.click()
        
        time.sleep(sleep_duration)
        
        element_to_click.clear()
        
    except Exception as E:
        print(E)
        
speak("hello")
speak("hey there I am Jarvis")
speak("Allow me to introduce myself, I am jarvis")