#Exercise 1
def convert (self):
    print (self * 28.3495231)
grams = float(input())
convert(grams)

#Exercise 2
def c(f):
    print ((5 / 9) * (f -32))
f= float(input())
c(f)

#Exercise 3
def solve(numheads,numlegs):
   rabbits = numlegs // 4
   chicken = numheads - rabbits
   print ("Rabbits: " + str(rabbits) + " Chicken: " + str(chicken))
solve(int(input()),int(input()))

#Exercise 4
def is_prime(n):
     if n < 2:
         return False
     for i in range(2, int(n**0.5) + 1):
         if n % i == 0:
             return False
     return True
def filter_prime(lst):
     return [x for x in lst if is_prime(x)]
line = input("Enter a list of numbers separated by spaces: ").split()
numbers = list(map(int, line))
print(filter_prime(numbers))

#Exercise 5
from itertools import permutations

def print_permutations(input_string):
    permuted_strings = [''.join(p) for p in permutations(input_string)]
    
    for permuted_string in permuted_strings:
        print(permuted_string)

user_input = input("Enter a string: ")
print_permutations(user_input)

#Exercise 6
def reverse(str):
    s = str.split(" ")[::-1]
    return " ".join(s)
str= input("Enter sentence")
print(reverse(str))

#Exercise 7
def has(lst):
    count =0
    for i in lst:
        if i==3:
            count+=1
        else: count =0
        if count ==2:
            return True
    return False
line = input("Enter a list of numbers separated by spaces: ").split()
lst=list(map(int, line))
print (has(lst))

#Exercise 8
def has(nums):
    for num in nums:
        if num == 0:
            for i in range(nums.index(num) + 1, len(nums)):
                if nums[i] == 0:
                    for j in range(i + 1, len(nums)):
                        if nums[j] == 7:
                            return True
    return False
line = input("Enter a list of numbers separated by spaces: ").split()
nums=list(map(int, line))
print (has(nums))

#Exercise 9
def v(r):
    print(r**3*4*3.14/4)
r=float(input())
v(r)

#Exercise 10
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list
line = input("Enter a list of numbers separated by spaces: ").split()
nums=list(map(str, line))
print (unique_elements(nums))

#Exercise 11
def palindrom(nums):
    count=0
    a=len(nums)-1
    for i in nums:
        if i==nums[a]:
            count+=1
        a-=1
    if count == len(nums):
        return True
    else: return False
a=str(input())
print(palindrom(a))

#Exercise 12 
def hist(nums):
    for i in nums:
        print(i*"*")
line = input("Enter a list of numbers separated by spaces: ").split()
nums=list(map(int, line))
print (hist(nums))

#Exercise 13
import random
from random import randint
def guess():
    a=randint(1,20)
    return a
a=input("Hello! What is your name? ")
print("Well, "+ a+ ", I am thinking of a number between 1 and 20.")
index=False
count=0
c=guess()
print("Take your guess.")
while (index==False):
    b=int(input())
    count+=1
    if b>c:
        print ("Your guess is too high.")
        print("Take your guess.")
    elif b<c:
        print("Your guess is too low.")
        print("Take your guess.")
    else: index=True
print("Good job, KBTU! You guessed my number in "+ str(count) +"guesses!")