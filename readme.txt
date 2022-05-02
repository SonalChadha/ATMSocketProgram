SONAL CHADHA
010850985

Please follow the steps below to run the ATM Socket Program on turing.csce.uark.edu:

1) Download the server.py and client.py files to your local system.
2) Launch FileZilla and connect to host 'turing.csce.uark.edu', your UARK username, your UARK password, and 
   port 22 and copy the server.py and client.py files from your local to remote server.
3) Launch PuTTY terminal or terminal/cmd on your local and connect to the Turing remote server over SSH with
   your username and password.
4) Start the server on terminal by typing 'python3 server.py'.
5) Launch another PuTTY or terminal/cmd on your local similar to how you did in step 3.
6) Start the client on the second terminal by typing 'python3 client.py'. 
7) Enter the menu choice shown on client terminal to perform withdrawal, deposit, check balance, or quit.
8) You can exit the program by typing '4', which will stop both server and client processes. 
9) To start the program again, keep the terminal on which you had started server open but close the
   terminal on which you had started client. Repeat steps 4-8.