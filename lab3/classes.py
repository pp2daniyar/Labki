#Exercise 1
class getstring:
    def _init_(self):
        self.str1=""
    def getstring(self):
        self.str1=str(input())
    def printstring (self):
        print (self.str1.upper())
str1 =getstring()
str1.getstring()
str1.printstring()

#Exercise 2
from math import *
class shape:
    def _init_(self):
        pass
    def area(self):
        return 0
class square(shape):
    def __init__(self):
        n = int(input())
        self.length =n 
    def area(self):
        return self.length * self.length
aSquare =square()
print (aSquare.area())

#Exercise 3
class Rectangle(shape):
   def __init__(self):
     length = float(input())
     width = float(input())
     self.length = length
     self.width = width
   def area(self):
     print(self.length * self.width)
nRectangle = Rectangle()
nRectangle.area()

#Exercise 4
class Point():
   def __init__(self):
     a = float(input())
     b = float(input())
     pta = int(input())
     ptb = int(input())
     self.pta = pta
     self.ptb = ptb
     self.a = a
     self.b = b
   def show(self):
     print(self.a, self.b)
   def move(self):
     self.a += self.a
     self.b += self.b
     print(self.a, self.b)
   def dist(self):
     da = self.pta - self.a
     db = self.ptb - self.b
     print(sqrt(da ** 2 + db ** 2))
nPoi = Point()
nPoi.show()
nPoi.move()
nPoi.dist()

#Exercise 5
class Account:
   def __init__(self):
     self.balance = 0
   def deposit(self):
     deposit = float(input())
     self.balance += deposit
     print(deposit)
   def withdraw(self):
     summa = float(input())
     if self.balance >= summa:
       self.balance -= summa
       print(summa)
     else:
       print("Insufficient balance")
   def display(self):
     print("\n Net Available Balance=", self.balance)
a = Account()
a.deposit()
a.withdraw()
a.display()

# Exercise 6
numbers = list(map(int, input().split()))
result = list(filter(lambda x: all(x % i != 0 for i in range(2, x)), numbers))
print(result)