import pyttsx3 

engine = pyttsx3.init()
engine.say(input("Write any test to convert text to speech : "))
engine.runAndWait()