#pyttsx3 is a text-to-speech conversion library in Python
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia


# init function to get an engine instance for the speech synthesis
engine=pyttsx3.init('sapi5')

#it is used to get the values of voices,voice etc
voices=engine.getProperty('voices')

# print(voices[1].id)--this is used to set the name of voice i.e DAVID with the id number.
engine.setProperty('voices',voices[1].id)


def speak(audio):
    # say method on the engine that passing input text to be spoken
    engine.say(audio)

    # run and wait method, it processes the voice commands.
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour) #it will give time between 0-24
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jojo. Your personal assistant. Please tell me sir how may i help you")


def takeCommand():
    '''it takes takes microphone input from the user and return string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1 # seconds of non-speaking audio before a phrase is considered complete
        audio=r.listen(source) #Records a single phrase from ``source`` into an ``AudioData`` instance, which it returns.

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print("User said",query)

    except Exception as e:
        print("Please say that again ...")
        return "None" #it returns none if any problem occurs
    return query

    

if __name__=="__main__":
       wishme()     
       while True:
        query=takeCommand().lower()
        #logic for executing the tasks
        if wikipedia in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2) # summary()-This function retrieves the summary from a Wikipedia page on a particular topic.
            speak("According to Wikipedia")
            speak(results)