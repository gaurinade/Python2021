# 1 Write a program to reverse a string.

s = 'mynameisgauri123'
reversestring = s[::-1]
print('reverse string is', reversestring)

# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12

s = input('enter the string in upper case and lower case:')
upper = 0
lower = 0
for i in s:
    if i >= 'A' and i <= 'Z':
        upper = upper + 1
    elif i >= 'a' and i <= 'z':
        lower = lower + 1
print('upper case:', upper)
print('lower case:', lower)

# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
def UniqueList(L):
    s = []
    for i in L:
        if i not in s:
            s.append(i)
    return s

a = UniqueList([1,2,3,5,6,8,1,4,2,9])
print(a)

# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.


# 5 Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT

s = input('Enter the sentence to make whole string capitalized:')
print('capitalized string is:', s.upper())

# 6. Define a function that can receive two integral numbers in string form and compute their sum and print it in the console.
def calculatesum (a,b):
    s = int(a) + int(b)
    return s

num1 = int(input("enter the 1st number for addition:"))
num2 = int(input("enter the 2nd number for addition:"))
add = calculatesum(num1,num2)
print(add)


# 7. Define a function that can accept two strings as input and print the string with the maximum length in the console.
# If two strings have the same length, then the function should print both the strings line by line.

def maxstring(a, b):
    if len(a) > len(b):
        return (a)
    if len(b) > len(a):
        return (b)


str1 = str(input("enter the 1st string:"))
str2 = str(input("enter the 2nd string:"))

max_str = maxstring(str1, str2)
print(max_str)

# 8. Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included).
def printtuple():
    l = list()
    for i in range(1,21):
        l.append(i**2)
    print(tuple(l))

printtuple()

# 9.Write a function called showNumbers that takes a parameter called limit.
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3) Expected output:0 EVEN 1 ODD 2 EVEN 3 ODD

limit = int(input('enter the limit:'))
def showNumbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            print(i, 'even')
        elif i % 2 != 0:
            print(i, 'odd')

showNumbers(limit)

# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)
a = range(1,21)
b = list(a)
is_even = lambda x: x % 2 == 0
list1 = list(filter(is_even,b))
print(list1)

# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].
a = range(1,21)
b = list(a)
is_even = lambda x: x % 2 == 0
list1 = list(filter(is_even,b))
squareNumber = list(map(lambda x: x**2, list1))
print(squareNumber)

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions
def divbyZero():
    return 5/0
try:
    divbyZero()
except ZeroDivisionError:
    print('Division by zero')

# 13.Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().

import functools
l = [1,2,3,4,5,6,7]
b = functools.reduce(lambda a,d: 10*a+d,l,0)
print(b)

# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.

a = int(input('enter the lower number:'))
b = int(input('enter the higher number:'))
for i in range(a, b+1):
    if ((i % 3 != 0) and (i % 7 == 0)):
        print(i, 'is divisible by 7 and not by  3')

# 16 (i)
# def foo():
#
#     try:
#         return 1
#     finally:
#         return 2
#     k = foo()
#     print(k)

it will print nothing.