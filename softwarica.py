import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

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

# it takes microphone input from user and returns string output
def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 800

        audio = r.listen(source)

    try:
        print("Recognizing... ")
        query = r.recognize_google(audio, language='en-nep')
        print(f'user said: {query}\n')

    except Exception as e:
        print('say that again please.....')
        return "none"
    return query



if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommand().lower()

        # logic for executing task
        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open lms' in query:
            webbrowser.open('https://lms.softwarica.edu.np/')

        elif 'open teams' in query:
            webbrowser.open('https://signup.microsoft.com/create-account/signup')

        elif 'open campus ' in query:
            webbrowser.open('https://campus.softwarica.edu.np/sign-in')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"sir the time is {strTime}")
            speak(f"sir the time is {strTime}")
