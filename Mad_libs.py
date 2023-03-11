# Follow the instructions in the tab to the right
# Write your mad libs program here

print("My name is myra, and I love to do Hard things. I love challenges.")
print("I am learning python for the second time so I can get the concepts and be abetter software developer")
user = input (str("Entre a funny word:" ))
user = input (str("Entre your last name: ")) 

print("I love your responce but I can see you love web development")

#import pyttsx3

#engine = pyttsx3.init()

Message = input("My name is myra and I love to do Hard things. I love challenges. I am learning python for the second time so I can get the concepts and be a better software develope" + user + "I love your responce but I can see you love web development")

#engine.say(text)
#engine.runAndWait


from tkinter import *
from gtts import gTTS
from playsound import playsound

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")