num1=int(input("Enter the number 1: "))
num2=int(input("Enter number 2:"))
if(num1==num2):
    x=num1+num2
    print("sum :",x)
else:
    if num1>num2:
        x=num1-num2
    else:
        x=num2-num1
    print("Difference :",x)
