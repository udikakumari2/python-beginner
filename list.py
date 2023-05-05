name=['nimal','kamal','nipuna','samadi','saduni']
print(name)
#give new list but not affecting to the original list
print(name[0])
print(name[3])
print(name[-1])#last item of arry
print(name[-2])#print the item before last item
print(name[2:])#all values starting at index of 2
print(name[2:4])#print the all items between index of 2 and 4 excluding index of 4
#if we want to changr item content
name[0]="saman"
print(name)
#to find lagest number of list
numbers=[3,5,1,30,20]
max=numbers[0]
for i in numbers:
    
    if(i>max):
            
            max=i
print(max)

