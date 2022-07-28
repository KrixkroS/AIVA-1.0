import speech_recognition as speer
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyjokescli


listener = speer.Recognizer()
engine = pyttsx3.init()
engine.say('Hey aiva here')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with speer.Microphone() as source:
             print('listening...')
             voice = listener.listen(source)
             command = listener.recognize_google(voice)
             command = command.lower()
             if 'aiva' in command:
               command = command.replace('aiva', '')
               print(command)
    except:
        pass
    return command


def run_aiva():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time =  datetime.datetime.now().strftime('%H %M %S')
        print(time)
        talk('current time is' + time)
    elif 'what is' in command:
        object = command.replace('what is', '')
        info = wikipedia.summary(object, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk('here is a joke for you')
        talk(pyjokes.get_joke())
    else:
        talk('Sorry could you please repeat it again')

while True:
    run_aiva()
