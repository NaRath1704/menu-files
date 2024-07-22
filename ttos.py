import gtts  
from playsound import playsound  
import os
mess = input("Enter your  message")
t1 = gtts.gTTS(mess)
t1.save("mess.mp3")   
os.system("vlc /root/python/mess.mp3")


