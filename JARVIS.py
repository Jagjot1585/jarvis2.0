import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0])



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('rate', 150)
    
def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternnon Sir")
    elif hour>=18 and hour<0:
        speak("Good Evening Sir")
    speak("Boot in Progress, Please Wait. Version-1.5.8.5 Loading ")
    speak("Boot Successful")
    speak("Hello Everyone, I am Jarvis Your Personal assistant. How may I help You?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        
        
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        speak("Recognising...")
        print(f"User Said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please..")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if ("How are You") in query:
            speak("I am Fine")
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'thank you' in query:
            speak('My Pleasure')
            print('My Pleasure')
        elif 'how are you' in query:
            print('I am as Great as Can be, searchhing things for you..You Tell how are you')
            speak('I am as Great as Can be, searchhing things for you..You Tell how are you')
        elif 'great' in query:
            print('That is how to live life...May your day becomes Greatest')
            speak('That is how to live life...may your day becomes Greatest')
        elif 'bye' in query :
            speak('Thanks For gossiping with me... Meet you later...Bye!')
            sys.exit()
            
        
