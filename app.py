import pyttsx3
import time
engine = pyttsx3.init()
engine.say("I am Computron version 0.0. Take me to your leader.")
engine.runAndWait()
#here add the wii balance board "starting up"
time.sleep(0.2)
engine.say("All booted up! Waiting for command.")
engine.runAndWait()
