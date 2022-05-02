# SONAL CHADHA
# 010850985

from multiprocessing.sharedctypes import Value
import socket
import sys

class server():
    def __init__(self):
        self.accBalance = int(100) 

    def balanceDisplay(self, serverSocket):
        serverSocket.send(("YOUR BALANCE IS CURRENTLY: $%.0f." % self.accBalance).encode())

    def moneyWithdraw(self, amtToWithdraw, serverSocket):
        if(self.accBalance - amtToWithdraw < 0):
            serverSocket.send(("YOU DO NOT HAVE ENOUGH MONEY IN YOUR ACCOUNT TO WITHDRAW $%.0f." % amtToWithdraw).encode())
        else:
            self.accBalance -= amtToWithdraw
            serverSocket.send(("YOU WITHDREW $%.0f, BALANCE IS NOW $%.0f." % (amtToWithdraw, self.accBalance)).encode())

    def moneyDeposit(self, amtToDeposit, serverSocket):
        self.accBalance += amtToDeposit
        serverSocket.send(("YOU DEPOSITED $%.0f, BALANCE IS NOW $%.0f." % (amtToDeposit, self.accBalance)).encode())

def main():
    socketObj = socket.socket()
    localHost = socket.gethostname()
    port = 7500
    socketObj.bind((localHost, port))

    socketObj.listen(6) 
    print("Socket successfully created and listening from client on port ", port)
    serverSocket, addr = socketObj.accept()
    print('Detected connection to client from ', addr)
    accnt = server()
    while True:
        menuChoice = serverSocket.recv(1024).decode()
        if menuChoice == '1':
            accnt.balanceDisplay(serverSocket)
        elif menuChoice == '2':
            serverSocket.send("Please enter the amount that you would like to withdraw: ".encode())
            try:
                amt = int(serverSocket.recv(1024).decode())
                if(amt >= 0):
                   accnt.moneyWithdraw(amt, serverSocket)
                else:
                    serverSocket.send("INVALID AMOUNT. AMOUNT CAN NOT BE NEGATIVE.".encode())
            except:
                 serverSocket.send("INVALID AMOUNT. AMOUNT MUST BE AN INTEGER VALUE.".encode())
        elif menuChoice == '3':
            serverSocket.send("Please enter the amount that would like to deposit: ".encode())
            try:
                amt = int(serverSocket.recv(1024).decode())
                if(amt >= 0):
                    accnt.moneyDeposit(amt, serverSocket)
                else:
                    serverSocket.send("INVALID AMOUNT. AMOUNT CAN NOT BE NEGATIVE.".encode())
            except ValueError:
                serverSocket.send("INVALID AMOUNT. AMOUNT MUST BE AN INTEGER VALUE.".encode())
        elif menuChoice == '4':
            serverSocket.send("THANKS FOR CHECKING IN WITH US. HAVE A GOOD DAY!".encode())
            break
        else:
            serverSocket.send("INVALID CHOICE. CHOICE MUST BE A NUMBER VALUE FROM 1-4.".encode())
    serverSocket.close()
    sys.exit()

main()