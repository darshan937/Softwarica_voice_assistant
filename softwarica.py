import pyttsx3
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hrs = int(datetime.datetime.now().hour)
    if hrs>=0 and hrs<12:
        print('Hello! good morning')
        speak("Hello! good morning")


    elif hrs>=12 and hrs<17:
        print('Hello! good Afternoon')
        speak("Hello! good Afternoon")

    elif hrs>=17 and hrs<19:
        print('Hello! Good Evening')
        speak("Hello! Good Evening")


    else:
        print('Hello! good night')
        speak("Hello! good night")

    print('I am Softwarica, how can i help you? ')
    speak("I am Softwarica, how can i help you? ")

if __name__ == '__main__':
    wishMe()