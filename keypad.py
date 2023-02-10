import serial
from array import*
import pyttsx3
ser = serial.Serial('COM6')
ser.baudrate = '9600'

arr = []

def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-100)
    engine.say(text)
    engine.runAndWait()


def read(arr):
    new = "" # C A T
    return(new.join(arr))


while True:
    h1 = ser.readline()
    print(h1)
    if h1:
        ss = int(h1.decode('utf-8'))

        if ss == 4: 
            print(read(arr))
            speak(read(arr))

        elif(ss == 1):
            arr.append("C")
            speak("C")
            print("C")
        elif(ss == 2):
            arr.append("A")
            speak("A")
            print("A")
        elif(ss == 3):
            arr.append("T")
            speak("T")
            print("T")
        elif(ss == 5):
            arr.append("T")
            speak("T")
            print("T")    
