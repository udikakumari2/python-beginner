import math

print("Enter point 1 coordinates\n")
x1=int(input("x1: "))
y1=int(input("\ny1: "))
print("\nEnter point 2 coordinates\n")
x2=int(input("x2: "))
y2=int(input("\ny2: "))
n=((x1-x2)**2)+((y1-y2)**2)
result=math.sqrt(n)
print("result "+str(result))
x=(x1+y1)*(x1+y1)
print("("+str(x1)+"+"+str(y1)+")*("+str(x1)+"+"+str(y1)+")="+str(x))

