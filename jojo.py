#pyttsx3 is a text-to-speech conversion library in Python
import pyttsx3
import datetime



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour) #it will give time between 0-24
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jojo your personal assistant. Please tell me sir how may i help you")


if __name__=="__main__":
       wishme()     