#nested for-loop
for x in range(4):#outer loop
    for y in range(3):#inner loop
        print(f'({x},{y})')

for x in [5,2,5,2,2]:
    print("x"*x)
for x in [5,2,5,2,2]:
    output=''
    for i in range(x):
        output +="x"
    print(output)
    for x in [2,2,2,2,12]:
        output=''
        for i in range(x):
            output +="x"
        print(output)
