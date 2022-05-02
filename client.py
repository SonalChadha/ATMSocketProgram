# SONAL CHADHA
# 010850985

import socket
import sys
from time import sleep

socketObj = socket.socket()
localHost = socket.gethostname()
port = 7500
socketObj.connect((localHost, port))
print("WELCOME TO ATM PROGRAM!")
while True:
    print("\n\n1) Check account balance amount.")
    print("2) Withdraw money from account.")
    print("3) Deposit money into account.")
    print("4) Quit.")
    print("Please enter an option (1-4) from the menu above: ")
    menuChoice = input()
    socketObj.send(str(menuChoice).encode())
    message = socketObj.recv(1024).decode()
    print(message)
    if(str(menuChoice) == '1' or message.split()[0] == "INVALID"):
        continue
    if(message == 'THANKS FOR CHECKING IN WITH US. HAVE A GOOD DAY!'):
        sleep(2)
        sys.exit()
    amt = input()

    socketObj.send(str(amt).encode())
    print(socketObj.recv(1024).decode())