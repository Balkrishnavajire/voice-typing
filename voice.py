import speech_recognition as sr
import subprocess as sp
from pynput.keyboard import Controller as key_controller
from pynput.keyboard import Key
import time
programname="Notepad.exe"
filename="Myfile.txt"
sp.Popen([programname,filename])

voice = sr.Recognizer()
keyboard = key_controller()
def writter():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print ('listening.....')
        audio=r.listen(source)
        audio_final = r.recognize_google(audio,language='en-in')
        print ('now Typing.....')
        for x in audio_final:
             keyboard.type(x)
             time.sleep(0.05)
        keyboard.press(Key.enter)
    writter()

if __name__ == '__main__':
    writter()
