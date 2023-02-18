import datetime
import pyjokes
import speech_recognition as sr
import pyttsx3
import pywhatkit as pw
import wikipedia
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hello Khuzaima I am your Siri")
engine.say("How can i help you")
engine.runAndWait()


def speak(text):
    engine.say(text)
    engine.runAndWait()
def taking_commands():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source) 
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                command = command.replace('siri','')
                print(command)
    except:
        pass
    return command
def wiki():
    command = taking_commands()
    if 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    else:
        speak('Please repeat your query again sir')
def greetings():
    command = taking_commands()
    if 'how are you' in command:
        command = command.replace('how are you','')
        ans = 'i am fine sir'
        speak(ans)
        print(ans)
    elif 'what are you doing' in command:
        command = command.replace('what are you doing','')
        ans = 'nothing sir just waiting for your command to fulfil sir'
        speak(ans)
        print(ans)
    
    elif 'turn off' in command:
        command = command.replace('turn off','')
        ans = 'ok thank you sir'
        speak(ans)
        print(ans)
    else:
        speak('Please repeat your query again sir')
def date_time():
    command = taking_commands()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
    else:
        speak('Please repeat your query again sir')
def youtube_videos():
    command = taking_commands()
    if 'play' in command:
        command = command.replace('play','')
        speak('playing sir')
        pw.playonyt(command)
    else:
        speak('Please repeat your query again sir')
def joking():
    command = taking_commands()
    if 'joke' in command:
        command = command.replace('joke','')
        jokes = pyjokes.get_joke()
        speak(jokes)
    else:
        speak('Please repeat your query again sir')
def opening_web_on_browser():
    command = taking_commands()
    if 'open' in command:
        command = command.replace('open','')
        webbrowser.open(command)
    else:
        speak('Please repeat your query again sir')
def about_siri():
    command = taking_commands()
    if 'tell me about you' in command:
        command = command.replace('tell me about you','')
        ans = 'Siri (/ˈsɪri/ SEER-ee) is a virtual assistant that is part of Apple Inc. iOS, iPadOS, watchOS, macOS, tvOS, and audioOS operating systems'
        speak(ans)
    elif 'who is your founder' in command:
        command = command.replace('who is your founder','')
        ans = 'My founder is Mr. Adam Cheyer'
        speak(ans)
    else:
        speak('Please repeat your query again sir')

def room_cleaner():
    goal_state = {'a':'1','b':'1','c':'1','d':'1'}
    action = 0
    cost = 0
    room_state = {'a':'1','b':'1','c':'1','d':'1'}

    command = taking_commands()
    if 'clean room a' in command:
        command = command.replace('clean room a', '')
        speak('room a is cleaned')
        cost = cost+1
        speak('cost is')
        speak(cost)
    elif 'clean room b' in command:
        command = command.replace('clean room b', '')
        speak('room b is cleaned')
        cost = cost+1
        speak('cost is')
        speak(cost)
    elif 'clean room c' in command:
        command = command.replace('clean room c', '')
        speak('room c is cleaned')
        cost = cost+1
        speak('cost is')
        speak(cost)
    elif 'clean room d' in command:
        command = command.replace('clean room d', '')
        speak('room d is cleaned')
        cost = cost+1
        speak('cost is')
        speak(cost)
    else:
        speak("Please say your query again sir")