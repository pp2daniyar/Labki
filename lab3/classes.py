#Exercise 1
class getstring:
    def _init_(self):
        self.str1=""
    def getstring(self):
        self.str1=input()
    def printstring (self):
        print (self.str1.upper)
str1 =getstring()
str1.getstring()
str1.printstring()

#Exercise 2
class shape:
    def _init_(self):
        pass
    def area(self):
        return 0
class square(shape):
    def __init__(self):
        n = int(input())
        shape._init_(self)
        self.length =n 
aSquare =square()
print (aSquare.area())
