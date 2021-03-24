import datetime
import pyttsx3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    speak('Current Time is ' + Time)

def date():
    date = datetime.datetime.now().strftime('%Y:%B:%d')

    speak('Today is ' +  date)

def wishme():
    speak('Hello, Dear!')
    date()
    time()
    speak('Bye')

wishme()