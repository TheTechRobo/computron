import pyttsx3
import speech_recognition as sr
import time
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
    retun r.recognize_sphinx(audio)
def askWithLogic(sphinx):
    if sphinx: 
        audio = sphinx()
        #add logic here
        result = audio #temporary
        return result
    if not sphinx:
        response = input("What would you like me to say? ")
        return response

engine = pyttsx3.init()
engine.say("I am Computron version 0 point 0 point 2. Take me to your leader.")
engine.runAndWait()
#here add the wii balance board "starting up"
time.sleep(0.2)
engine.say("All booted up! Waiting for command.")
engine.runAndWait()
while True:
    ask(sphinx=True) #set to False for classic asking for response at console
    engine.say("Process complete; waiting for command.")
    engine.runAndWait()

#We could add speech recognition and an AI later but not right now. 
#When we pick the random item we should lower the chances of it being thetechrobo - add the following:
#if rchoice.lower() == "thetechrobo":
    #pick the choice AGAIN
