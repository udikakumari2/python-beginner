str1='Welcome'
print(str1[:6]+' PYnative')#str[start:end]
#q2
strOne = str("pynative")
strTwo = "pynative"
print(strOne == strTwo)
print(strOne is strTwo)
#q3
print("John" > "Jhon")
print("Emma" < "Emm")
#q4
myString = "pynative"
stringList = ["abc", "pynative", "xyz"]

print(stringList[1] == myString)
print(stringList[1] is myString)
#q5
str1 = "My salary is 7000";
str2 = "7000"

print(str1.isdigit())
print(str2.isdigit())
#q6
str1 = "first" 
id(str1) 
str1 = str1+ " Two" 
id(str1)
#q7
str = "My salary is 7000";
print(str.isalnum())
#Choose the correct function to get the character from ASCII number
#The chr() function is used to get the character from the ASCII number. Example: print(chr(112)) will print p
#q8
str1 = "my isname isisis jameis isis bond";
sub = "is";
print(str1.count(sub, 4))
#q9
str = "my name is James bond";
print (str.capitalize())
