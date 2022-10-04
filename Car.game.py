import time

print ("\nwelcome to Car game! \n Press enter to begin")
engine = False
command = input("\nEnter 'Start' to start the car. \n Enter 'Stop' to stop the car. \n Enter 'quit' to quit the game:\n")
while command.upper()!= "QUIT":
    if command.upper() == "START" and engine == False:
        command = input("\nthe car is started.... \nEnter 'Stop' to stop the car\n")
        engine = True
        
    elif command.upper() == "START" and engine == True:
        command = input("\nThe engine is already on \nEnter 'Stop' to stop the car\n")
        engine = True

    elif command.upper() == "STOP" and engine == True:
        command = input("\nthe car is Stopped.... \nEnter 'Start' to start the car\n")
        engine = False
    elif command.upper() == "STOP" and engine == False:
        command = input("\nThe engine is already off.... \nEnter 'Start' to start the car\n")
        engine = False
    elif command.upper()!= "QUIT" and command.upper()!= "START" and command.upper()!="STOP":
        
        if engine == True:
            print("\nEngline is on\n")
        else:
            print("\nEngine is off\n")
        command = input("please enter valid command!\n")
    
else:
    print("thanks for playing")
    time.sleep(1)