from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket  = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    print('Choose an operation: Random, Add or Subtract:')
    operationInput = input()
    while operationInput != 'Random' and operationInput != 'Add' and operationInput != 'Subtract':
        print('Choose an operation: Random, Add or Subtract:')
        operationInput = input()

    CorrectOrder = True
    
    while CorrectOrder:
        print('Pick number 1:')
        num1 = int(input())
        #it is int, so when inputing str it crashes
    
        print('Pick number 2:')
        num2 = int(input())
        #it is int, so when inputing str it crashes
    
        if num2 > num1 and operationInput == 'Random':
            CorrectOrder = False
        elif num1 > num2 and operationInput == 'Random':
            print('Error: Number 2 must be higher than Number 1, when choosing Random')
        elif num1 == num2 and operationInput == 'Random':
            print('Error: Number 1 and Number 2 cannot be the same, when choosing Random')
        elif num1 == str and operationInput == 'Random':
            print('Error: Number 1 must consist of numbers and not letters')
        elif num2 == str and operationInput == 'Random':
            print('Error: Number 2 must consist of numbers and not letters')
        elif num1 == str and operationInput == 'Add':
            print('Error: Number 1 must consist of numbers and not letters')
        elif num2 == str and operationInput == 'Add':
            print('Error: Number 2 must consist of numbers and not letters')
        elif num1 == str and operationInput == 'Subtract':
            print('Error: Number 1 must consist of numbers and not letters')
        elif num2 == str and operationInput == 'Subtract':
            print('Error: Number 2 must consist of numbers and not letters')
    
        if operationInput == 'Add' or operationInput == 'Subtract':
            CorrectOrder = False


    sendString = str(operationInput+','+str(num1)+','+str(num2)).encode()
    clientSocket.send(sendString)
    recievedResult = clientSocket.recv(1024).decode()
    print(recievedResult)