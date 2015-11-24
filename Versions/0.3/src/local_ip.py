import time
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("duckduckgo.com",80))
os.system("clear")
print (s.getsockname()[0])
s.close()
sleep
