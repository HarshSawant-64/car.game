command = ""
started = False
while True:
    command = input("> ")
    if command == "start":
        if started:
            print("Car is already  started!")
        else:
            started = True
            print("Car Started:")

    elif command == "stop":
        if not started:
            print("Car is alreday stoped...")
        else:
            started==False
            print("Car stopped")

    elif command == "help":
        print(""" start - to start the car
                  stop - stop the car
                  quit - to quit""")
    elif command == "quit":
        break
    else:
        print("Sorry I dont understand")



