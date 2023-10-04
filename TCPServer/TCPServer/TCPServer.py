from socket import *
import threading
import random

def handleClient(connectionSocket, addr):
    while True:
        recieved = connectionSocket.recv(1024).decode()
        operationInput = recieved.split(',')[0]
        num1 = int(recieved.split(',')[1])
        num2 = int(recieved.split(',')[2])
        sendResult = ""
        if operationInput == 'Random':
            sendResult = random.randint(num1,num2)
        elif operationInput == "Add":
            sendResult = num1 + num2
        elif operationInput == "Subtract":
            sendResult = num1 - num2
        connectionSocket.send(str(sendResult).encode())

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient,args=(connectionSocket,addr)).start()