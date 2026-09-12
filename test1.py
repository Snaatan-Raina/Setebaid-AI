import pyttsx3
import time

engine = pyttsx3.init()
voices = engine.getProperty("voices")

for i in range(0, len(voices)):
    print(voices[i].id, i)