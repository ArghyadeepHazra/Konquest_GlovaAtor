import serial
from array import*
from twilio.rest import Client
from tkinter import *
import pyttsx3
import random
import continuous_threading
import speak
import threading
from PIL import Image, ImageTk 
import Sms



ser = serial.Serial('COM8')
ser.baudrate = '9600'

def readSerial():
    h1 = ser.readline()
    if h1:
        ss = int(h1.decode('utf-8'))
        if ss == 4: 
           food () 
           print("Food Done")
        if ss == 5 :
            call()
            print("sms")
t1 = continuous_threading.PeriodicThread(0.1,readSerial)


root = Tk()

# All Frame 
Main_frame = LabelFrame(root , padx = 100 , pady = 7 , borderwidth=3, relief= "raised") # inside padding 
Main_frame.grid( row = 0 , column = 1 , padx = 20, pady = 60) # outside pading 

Display_frame = LabelFrame(root , padx= 55 , pady = 10 ,borderwidth=3, relief= "raised") # inside padding 
Display_frame.grid( row  = 0, column = 0 , padx = 150 , pady = 10 ,) # outside pading


# Display_frame Widget

lable_Display = Label(Display_frame , text = "GlovaAtor" , font = ("Comic Sans MS" , 14 , "bold" ) , bg = "#C4C4C4" )
lable_Display.grid(row= 0,  column= 0 ,padx = 20 ,  pady = 10)

Display_Image = ImageTk.PhotoImage(Image.open("Image/Background.png"))
Default_Label = Label(Display_frame ,image = Display_Image)
Default_Label.grid(row = 1 , column = 0 , pady = 20)


def food_label() :
    lable_Display.config(text = "I Wanna Eat Food")


def sms_label():
    lable_Display.config(text = "Send Sms")
   
def joke_arr():
    cars = ["Teacher: Why do humans have different blood groups. Student: So that mosquitoes can enjoy different flavous", 
        "Why should you never trust stairs?They’re always up to something",
        "What kind of shorts do clouds wear?Thunderpants" ,
        "How do you open a banana? With a mon-key." ,
        "Why does Humpty Dumpty love autumn? Because he had a great fall."]
    return random.choice(cars)

def joke():
    img_joke = ImageTk.PhotoImage(Image.open("Image/joke.png"))
    Default_Label.configure(image=img_joke)
    Default_Label.image = img_joke
    ans = joke_arr()
    speak.speak(ans)    


def food () :
    img_food = ImageTk.PhotoImage(Image.open("Image/food.png"))
    Default_Label.configure(image=img_food)
    Default_Label.image = img_food
    food_label()
    speak.speak("I Wanna Eat Food")

def make_call():
    account_sid = "ACc7d414df5a2772ddffae6e54f79f6756"
    auth_token = "28c73df22d8c9e3edc3a11aecc66dd02"
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml',
                            to='+918210410103',
                            from_='+19402919532')
    print(call.sid)

def sms():
    img_sms = ImageTk.PhotoImage(Image.open("Image/Send.jpg"))
    Default_Label.configure(image=img_sms)
    Default_Label.image = img_sms
    sms_label()
    Sms.sms()
    speak.speak("message send successfully")

def call():
    img_sms = ImageTk.PhotoImage(Image.open("Image/Send.jpg"))
    Default_Label.configure(image=img_sms)
    Default_Label.image = img_sms
    make_call()
    speak.speak("call send successfully")





t1.start()
root.mainloop()