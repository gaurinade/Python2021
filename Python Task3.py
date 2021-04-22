# 1. Create a list of 10 elements of four different data types like int, string, complex and float.
L = [10, 'python','3.13',2+3j, 214, 'mango','apple', 5+6j, 45.45, 4]
print(L)

# 2 Create a list of size 5 and execute the slicing structure
l = [10, 20, 30, 40, 50]
print(l[2:4])
print(l[-1])
print(l[:4])

# 3 Write a program to get the sum and multiply of all the items in a given list.
l = [5,10,15,20,3,2]
i = 0
summation = 0
while i < len(l):
    summation = summation + l[i]
    i = i + 1
print('sum:',summation)

j = 0
multiplication = 1
while j < len(l):
    multiplication = multiplication * l[j]
    j = j + 1
print('multiplication:',multiplication)

# 4. Find the largest and smallest number from a given list.
l = [10,32,54,678,212,878,453,872,982,123,864,892,782,561,865,567,213,431,997,329]
print(max(l))
print(min(l))

# 5. Create a new list which contains the specified numbers after removing the even numbers from a
# # predefined list.
L = [10,20,34,45,12,31,53,98,76,78,93]
s = []
i = 0
for i in L:
   if i % 2 != 0:
        s.append(i)
print(s)

# 6. Create a list of elements such that it contains the squares of the first and last 5 elements
# between 1 and 30 (both included).
L = []
for i in range(1,21):
    L.append(i**2)
print(L[:5])
print(L[-5:])

# 7 Write a program to replace the last element in a list with another list.
# Sample input: [1,3,5,7,9,10], [2,4,6,8]
# Expected output: [1,3,5,7,9,2,4,6,8]

L = [1,32,45,23,55,76,12,43,90]
L1 = [23,54,67,89,21]
L3 = L[:len(L)-1]
new_list = L3 + L1
print(new_list)

# 8 Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}
# Expected output: {1:10,2:20,3:30,4:40}

a = {1:10, 2:20}
b = {3:30, 4:40}
c = {**a ,**b}
print(c)

# 9 Create a dictionary that contain numbers in the form(x:x*x)
# where x takes all the values between 1 and n(both 1 and n included).
# Sample input: n=5 Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}

n = int(input("enter a number"))
d = dict()
for x in range(1,n+1):
    d[x] = x * x
print(d)

# 10 Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple
# which contains every number in the form of string.
# Sample input: 34,67,55,33,12,98
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)

numbers = (input('Enter the comma separted numbers:'))
s = numbers.split(',')
tuple = tuple(s)
print(s)
print(tuple)
