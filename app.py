import pyttsx3
import speech_recognition as sr
import time
import random
from support.items_list import items

def _Replace(list, audio):
    for item in list:
        audio = audio.lower()
        audio = audio.replace(item, "")
    return audio

def sphinx():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        return r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    return False
def google(key):
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        return r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return False
def ibm(key):
    pass

def askWithLogic(which):
    """
    parameter which: 0 if Sphinx; 1 if Google; 2 if IBM; 99 if Manual. (99 so it's scalable and backwards compatible even if I add more)
    """
    if which == 0: 
        function = sphinx
    if which == 99:
        response = input("What would you like me to say? ")
        return response
    audio = function()
    if not audio:
        return "There was an issue with your text to speech. Check your Internet connection, and try again."
    replaceList = ["what is", "why is", "who is", "who are", "why are", "what are", "what am", "who am", "is a"] #this looks complicated but it's just removing the most common starts of questions
    audioWithLogic = _Replace(replaceList, audio)
    rchoice = random.choice(items)
    if rchoice.lower == "the tech robo":
        rchoice = random.choice(items) #lower likelihood of it being thetechrobo
        result = audioWithLogic + " is %s" % random.choice(items)
    return result

engine = pyttsx3.init()
engine.say("I am Compu-tron version 0 point 1. Take me to your leader.")
engine.runAndWait()
#here add the wii balance board "starting up"
time.sleep(0.2)
engine.say("All booted up! Waiting for command.")
engine.runAndWait()
while True:
    engine.say(askWithLogic(which=0))#set to 99 for classic asking for response at console
    engine.say("Process complete; waiting for command.")
    engine.runAndWait()

#We could add an AI later but not right now. 
#Also, it says "you is blah" and stuff instead of "you are" and it doesnt recognize am i but thats for later. Right now it works. :D

