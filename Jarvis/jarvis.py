import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait() 


def wishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour >= 0 and hour < 12:
        speak("good morning")  
    elif hour >= 12 and hour < 18:
        speak("good afternoon")  
    else:
        speak("good evining") 
    speak("i am jarvis  how can i help you?")               


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning ........")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing ........")
        query = r.recognize_google(audio,language='en-in')
        print (f"User Said : {query} \n")
    except Exception as e:
        print("say this again please .....")
        return "NONE"  
    return query 


if __name__ == '__main__':
    wishMe()
    while True: 
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia.........')
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query,sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube'in query:
            webbrowser.open("youtube.com")  

        elif 'open facebook' in query:
            webbrowser.open("facebook.com") 

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'play music' in query:
            music_dir = 'd:\\song'
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir,song[1]))
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")   


        elif 'open code' in query:
            codepath ="C:\\Users\\Roman pudasaini\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile( codepath)
