import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
engine.setProperty('voice', 'english')  # Set the voice to English
engine.say("Hello, I am your text-to-speech engine.")
engine.runAndWait()
engine.say("I can convert text to speech.")
engine.runAndWait()