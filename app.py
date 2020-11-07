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
def google(key=False):
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        if key:
            output = r.recognize_google(audio, key)
            print("Google Speech Recognition thinks you said " + output)
            return output
        output = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + output)
        return output
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return False
def ibm(key):
    pass

def askWithLogic(which=False):
    """
    parameter which: 0 if Sphinx; 1 if Google; 2 if IBM; 99 if Manual. (99 so it's scalable and backwards compatible even if I add more)
    """
    if not which: 
        which = int(input("Make your choice. \n0 - I want to use Sphinx. (Useful if you don't have an API key for anything and you don't want to use Google, or have no working Internet connection on this PC.\n\
        1 - I want to use Google Speech Recognition (useful if you don't have an API key for anything and have a working Internet connection.)\n\
        2 - I want to use IBM Watson speech recognition. (Requires a free API key.)\n\
        99 - I want to use classic \"What do you want me to say?\" for Computron."))
    if which == 0: 
        apiKeyMightExist = False
        function = sphinx
    if which == 1:
        apiKeyMightExist = True
        apiKeyYesNo = input("\nMake your choice: \n1 - I have an API key for Google Speech Recognition, and I want to type it in.\n2 - Either I don't have an API for Google Speech Recognition, or I don't want to type it in.")
        if apiKeyYesNo[0] == "1":
            apiKey = input("Enter your API key. **This will not be stored anywhere,** you will have to enter it whenever you want to use COMPUTRON.")
        function = google
    if which == 2:
        apiKeyMightExist = True
        apiKeyYesNo = input("\nMake your choice: \n1 - I have an API key for IBM Watson Speech Recognition, and I want to type it in.\n2 - Either I don't have an API for Google Speech Recognition, or I don't want to type it in.")
        if apiKeyYesNo[0] == "1":
            apiKey = input("Enter your API key: ")
        else:
            print("IBM Watson Speech Recognition requires a free API key. You can find it at www.ibm.com/cloud/watson-speech-to-text/pricing.")
            return
        function = ibm
    if which == 99:
        response = input("What would you like me to say? ")
        return response
    if apiKeyMightExist:
        if apiKeyYesNo[0] == "1":
            function(apiKey)
    else:
        audio = function()
    if not audio:
        return "There was an issue with your text to speech. Try again. If you're using anything but Sphinx, check your Internet connection. If that doesn't help or you're using Sphinx, try again later."
    replaceList = ["what is", "why is", "who is", "who are", "why are", "what are", "what am", "who am", "is a"] #this looks complicated but it's just removing the most common starts of questions
    audioWithLogic = _Replace(replaceList, audio)
    rchoice = random.choice(items)
    if rchoice.lower == "the tech robo":
        rchoice = random.choice(items) #lower likelihood of it being thetechrobo
        result = audioWithLogic + " is %s" % random.choice(items)
    return result

engine = pyttsx3.init()
engine.say("I am Compu-tron version Git improved speech recognition. Take me to your leader.")
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

