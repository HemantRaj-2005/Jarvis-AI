import asyncio
import os
import edge_tts
import pygame
import threading

Voice = "en-CA-LiamNeural"
BUFFER_SIZE = 1024

def remove_file(file_path):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        with open(file_path,"wb"):
            pass
        os.remove(file_path)
        break

async def amain(TEXT, output_file) -> None:
    try:
        cm_txt = edge_tts.Communicate(TEXT, Voice)
        await cm_txt.save(output_file)
        thread = threading.Thread(target=play_audio,args=(output_file,))
        thread.start()
        thread.join()
        
    except Exception as e:
        print(f"Error saving audio file: {e}")
        
    finally:
        remove_file(output_file)

def play_audio(file_path):
    try:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()  
        
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)
        
    except Exception as e:
        print(f"Error playing audio file: {e}")
        
    finally:
        pygame.quit()
        
def speak(Text, output_file=None):
    if output_file is None:
        output_file = f"{os.getcwd()}/speech.mp3"
    
    try:
        asyncio.run(amain(Text, output_file))
        play_audio(output_file)
    except Exception as e:
        print(f"Error in speak function: {e}")
    
speak("hello I am Jarvis")
speak("Hello sir, How may I help you today?")
