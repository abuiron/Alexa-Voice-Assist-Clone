import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import webbrowser
import psutil
from googlesearch import search 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print('Current time is ' + time)
    elif 'who is ' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
        print('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'richest man in the world' in command:
        for result in search('richest man in the world'):
            talk('According to google,' + result)
            print('According to google,' + result)
            break
    elif 'tell me about' in command:
        query = command.replace('tell me about', '')
        for result in search(query):
            talk("According to google," + result)
            break
    elif 'open' in command and ('notepad' in command or 'editor' in command):
        talk('Opening Notepad')
        subprocess.Popen('notepad.exe')
    elif 'search' in command or 'google' in command:
        search_query = command.replace('search', '').replace('google', '')
        talk('Searching on google for ' + search_query)
        url = 'https://www.google.com/search?q=' + search_query
        webbrowser.open(url)
        while any('chrome' in  p.name() for p in psutil.process_iter()):
            pass
        talk('you can say the command again.')
    elif 'exit' in command or 'stop' in command:
        talk('Good Bye...!')
        exit()
    else:
        talk('Please say the command again.')


while True:
    run_alexa()