numbers=[2,6,9,10]
numbers.append(30)
print(numbers)
numbers.insert(0,40)
print(numbers)
numbers.remove(6)
print(numbers)
numbers.clear()
numbers=[2,6,5,9,5,10,5]
print(numbers)
numbers.pop()
print(numbers)
#to check index of value
print(numbers.index(6))
#check values in list
print(50 in numbers)
#if there is repeat numbers in the list and get count of them
x=numbers.count(5)
print(x)
#assecnding 
numbers.sort()
print(numbers)
#deccending 
numbers.reverse()
print(numbers)
number2=numbers.copy()
numbers.append(4)
print(number2)#these two independent lists ,if one of list is update and other list is not updated.

#if we want to remove duplicate values
list2=[]
for item in numbers:
    if item  not in list2:
        list2.append(item)


print(list2)
