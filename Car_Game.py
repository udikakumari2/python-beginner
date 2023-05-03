command=""
start=False
while True:
    command=input(">")
    if command.lower()=="start":
        if start:
            print("Car is already started...")
        else:
            start=True
            print("Car started....")
    elif command.lower()=="stop":
        if not start:
            Print("Car is already stopped...")
        else:
            start=False
            print("Car stopped....")
    elif command.lower()=="help":
        print("""
        start- to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command.lower()=="quit":
        break
    else:
        print("Sorry,I don't understand that ...")