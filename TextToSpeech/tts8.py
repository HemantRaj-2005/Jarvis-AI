import requests
import playsound
import os
from typing import Union

def generate_audio(message: str, voice : str="Brian"):
    url : str = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={{{message}}}"
    
    headers = {'User Agent':'Mozilla/5.0(Macintosh;intel Mac OS 10_15_7)AppleWebKit/537.36(KHTML,like Geoko)Chrome/119.0.0.0 Safari/537.36'}
    
    try:
        result = requests.get(utl=url, headers=headers)
        return result.content
    except:
        return None
    
    
def speak(message : str, voice : str = "Brain", folder : str = "", extension : str = ".mp3")->Union[None,str]:
    try:
        result_content = generate_audio