command=""
while True:
    command=input(">")
    if command.lower()=="start":
        print("Car started....")
    elif command.lower()=="stop":
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