# info: https://www.youtube.com/watch?v=FV7eiqN01hc

import os

os.system("cd RemoteControl")
os.system("git pull")
print("RemoteControl was updated")
os.system("cd RemoteControl/RaspberryPI")
os.system("sudo python RemoteControl/RaspberryPI/MainControl.py")