import pyttsx3
import time
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty("voices")

i=19
engine.setProperty("voice", voices[i].id)
engine.setProperty("rate", 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    time.sleep(0.5)
 
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for background noise...")
        r.adjust_for_ambient_noise(source, duration=1)

        print("Listening...")
        audio = SSr.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(f"User said: {query}\n")
        return query

    except sr.UnknownValueError:
        print("I could not understand you.")
        return ""

    except sr.RequestError as error:
        print(f"Speech service error: {error}")
        return "None"
    return query        


if __name__ == "__main__":
    speak("aur Dhruv bhai kae se ho, Radhe Radhe guru ji")
    query = takeCommand().lower()
