import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-100)
    engine.say(text)
    engine.runAndWait()