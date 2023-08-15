txt = "Only LKR {price:.2f} !"
print(txt.format(price = 100))
#named indexes:
str1= "She is {fname} and her age is{age}".format(fname = "Shara", age = 21)
#numbered indexes:
str2= "She is {0} and age is{1}".format("Shara", 21)
#empty placeholders:
str3= "She is {} and age is{}".format("Shara", 21)
print(str1)
print(str2)
print(str3)
#Left aligns the result
txt1 = "We have {:<8} eggs."
print(txt1.format(19))
#Right aligns the result
txt1 = "We have {:>8} eggs."
print(txt1.format(19))
#Center aligns the result
txt1 = "We have {:^8} eggs."
print(txt1.format(19))

#, used as a thousand separator:
txt1 = "This car is US$ {:,}."
print(txt1.format(43800000))
#b converts the number into binary format:
txt1 = "The binary of {0} is {0:b}"
print(txt1.format(5))
