import speech_recognition as sr
import os
import threading
from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)

def print_loop():
    while True:
        print(Fore.GREEN + "I am Listening...",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)


def trans_hindi_to_eng(text):
    eng_txt = translate(text,"en-in")
    return eng_txt

def speech_to_text():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 35000
    recognizer.dynamic_energy_adjustment_damping = 0.03   # as much less, more it will be  active
    recognizer.dynamic_energy_ratio = 1.9
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.4
    recognizer.non_speaking_duration = 0.3

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.GREEN + "I am Listening...",end="",flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\r" + Fore.CYAN + "Recognizing...." , end = "",flush=True)
                recognized_txt = recognizer.recognize_google(audio).lower()
                if recognized_txt:
                    trans_txt = trans_hindi_to_eng(recognized_txt)
                    print("\r" + Fore.LIGHTGREEN_EX + "Hemant : " + trans_txt)
                    return trans_txt
                else:
                    return ""
            except sr.UnknownValueError:
                recognized_txt = ""
            finally:
                print("\r",end="",flush=True)
            
            os.system("cls" if os.name == "nt" else "clear")

        stt_thread = threading.Thread(target=speech_to_text)
        print_thread = threading.Thread(target=print_loop)
        stt_thread.start()
        print_loop.start()
        stt_thread.join()
        print_loop.join()


speech_to_text()
