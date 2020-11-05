import pyttsx3
import speech_recognition as sr
import time
import random
from support.items_list import items

def sphinx():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    return r.recognize_sphinx(audio)
def askWithLogic(useSphinx):
    if useSphinx: 
        audio = sphinx()
        audioWithLogic = audio.lower().replace("what is","").replace("why is","").replace("who is","").replace("who are","").replace("why are","").replace("what are","").replace("what am","").replace("who am","").replace("is a","") #this looks complicated but it's just removing the most common starts of questions
        result = audioWithLogic + " is %s" % random.choice(items)
        return result
    if not useSphinx:
        response = input("What would you like me to say? ")
        return response

engine = pyttsx3.init()
engine.say("I am Compu-tron version Git Speech Recognition. Take me to your leader.")
engine.runAndWait()
#here add the wii balance board "starting up"
time.sleep(0.2)
engine.say("All booted up! Waiting for command.")
engine.runAndWait()
while True:
    engine.say(askWithLogic(useSphinx=True))#set to False for classic asking for response at console
    engine.say("Process complete; waiting for command.")
    engine.runAndWait()

#We could add speech recognition and an AI later but not right now. 
#When we pick the random item we should lower the chances of it being thetechrobo - add the following:
#if rchoice.lower() == "the tech robo":
    #pick the choice AGAIN
