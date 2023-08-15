def GetInputs():
    global name
    global studentId
    global English
    global IT
    global Maths
    global avg
    name=input("Enter name of Student: ")
    studentId=input("Enter StudentID: ")
    English=int(input("Enter English marks: "))
    IT=int(input("Enter IT marks: "))
    Maths=int(input("Enter Maths marks: "))
    avg=(English+IT+Maths)/3
    PrintDetails()
    return avg
    
def getStaus(avg):
    if(avg>=50):
        
        print("You have passed the examination")
    else:
        
        print("You have failed the examination")
        
def PrintDetails():
    print("""\tStudent Name:%s
        StudentID:%s
        Engish : %d
        Maths  : %d
        IT     : %d
        --------------
        Average: %.2f"""%(name,studentId,English,Maths,IT,avg))

avg=GetInputs()
getStaus(avg)


