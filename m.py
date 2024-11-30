from math import sqrt
number=int(input("Enter a number"))
if number >1:
    for k in range (2,int(sqrt(number))+1):
         if (number%k==0):
              print("It is a prime number")
              break
    else:
         print("It's not a prime number")
else:
     print("it is not a prime number")