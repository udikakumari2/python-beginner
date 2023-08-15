def recur_factorial(n):
    
   if n == 1:  
       return n  
   else:
      global x
      return n+recur_factorial(n-1)
u=int(input("enetr number:"))
recur_factorial(u)
print("The tptal of Given Number: ",recur_factorial(u))
