import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate',150)     # setting up new voice rate
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello How may I help You ")

engine.runAndWait()
