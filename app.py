import pyttsx3
import SpeechRecognition
import time
from support.items_list import items
engine = pyttsx3.init()
engine.say("I am Computron version 0 point 0 point 2. Take me to your leader.")
engine.runAndWait()
#here add the wii balance board "starting up"
time.sleep(0.2)
engine.say("All booted up! Waiting for command.")
engine.runAndWait()
while True:
    response = input("Please enter the response you would like Computron to say...")
    engine.say(response)
    engine.runAndWait()
    engine.say("Process complete; waiting for command.")
    engine.runAndWait()
#We could add speech recognition and an AI later but not right now. 
#When we pick the random item we should lower the chances of it being thetechrobo - add the following:
#if rchoice.lower() == "thetechrobo":
    #pick the choice AGAIN
