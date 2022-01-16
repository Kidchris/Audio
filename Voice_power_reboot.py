# %% [markdown]
# ## Give command to computer
# - Better use Linux But possible in linux.
# Modules used : 
# - getpass (Build-in)
# - os (Build-in)
# - playsound (Pip install)
# - gtts (Pip install)
# - speech_recognition (Pip install)

# %%
import speech_recognition as sr
# import pyttsx3
import getpass
import gtts
from playsound import playsound as play
import os

user = getpass.getuser()

r = sr.Recognizer()
micros = sr.Microphone.list_microphone_names()
micro_index = micros.index("default")

def speak(audio):
    tt = gtts.gTTS(f"{audio}")
    tt.save("./file.mp3")
    play("./file.mp3")

def listener(indicator ="Command" ):
    with sr.Microphone(device_index=micro_index) as source:
        speak(f"Try Saying {indicator}")
        # r.adjust_for_ambient_noise(source)
        # r.pause_threshold = 0.7
        audio = r.listen(source)
        return audio

def main():
    output = listener("Reboot or Poweroff")
    print(output)
    res = r.recognize_google(output)
    print(res)
    if res.lower() =="reboot":
        print("do you really want to reboot the computer?")
        confirm = listener("yes")
        confirm_output = r.recognize_google(confirm)
        if confirm_output.lower()== "yes":
            os.system("reboot")
        else :
            print("Opreation Canceled Successfully! ")
            
    if res.lower() =="poweroff":
        print("do you really want to Shutdown the computer?")
        confirm = listener("poweroff")
        confirm_output = r.recognize_google(confirm, language='en-in')
        if confirm_output.lower()== "yes":
            os.system("shutdown /r /t 30")
        else :
            print("Opreation Canceled Successfully! ")        
            
    
speak(f"Welcome {user}")
listener("Reboot or Poweroff")
main()
