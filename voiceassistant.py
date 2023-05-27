import pyttsx3
import datetime
import webbrowser
import wikipedia
import speech_recognition as sr
import os
import time
import pyautogui
import pyjokes
import pywhatkit


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


def bolo(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        bolo("good morning")
    elif hour>=12  and hour<16:
        bolo("good afternoon")
    else:
        bolo("good evening")   

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...") 
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"usercommand is{query}")
    except Exception as a:
        print(a)
        print("Say Again")
        return "none"
    return query

if __name__ == '__main__':
    wishme()


    while True:

        query = takecommand().lower()

        if 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
        elif 'wikipedia' in query:
            query=query.replace('wikipedia', '')
            result=wikipedia.summary(query,sentences=3)
            bolo("according to wikipedia")
            print(result)
            bolo(result)
        elif 'open notepad' in query:
            bolo("opening notepad")
            p="C:\\Windows\\System32\\notepad.exe"
            os.startfile(p)
        elif 'open google chrome' in query:
            bolo("opening google chrome")
            p="C:\\Users\\Public\\Desktop\\Google Chrome.lnk"
            os.startfile(p)
        elif 'current time' in query:
            bolo(time.strftime("%H %M %S %p"))
        elif 'play game' in query:
            webbrowser.open("https://youtu.be/2L6gsn7rGqI")
        elif 'vega movies' in query:
            webbrowser.open("https://vegamovies.chat/")
        elif 'volume up' in query:
            bolo("ok sir")
            pyautogui.press("volumeup")
        elif 'volume down' in query:
            bolo("ok sir")
            pyautogui.press("volumedown")
        elif 'mute' in query:
            bolo("ok sir")
            pyautogui.press("volumemute")
        elif 'unmute' in query:
            bolo("ok sir")
            pyautogui.press("volumeunmute")
        elif 'jokes' in query:
            bolo(pyjokes.get_jokes())
        elif 'play song'in query:
            bolo("playing...")
            song=query.replace("play song","")
            pywhatkit.playonyt(song)
    

        else:
            bolo("ok bye")
            exit()