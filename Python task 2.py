# problem1: Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.

a = int(input("enter the number:"))
if a % 3 == 0 and a % 5 == 0:
    print("Consultadd - Python Training")
elif a % 3 == 0:
    print("Consultadd")
elif a % 5 == 0:
    print("Python Training")

#Problem 2: Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication
# If User Enter 5 - Average
# Ask user to enter two numbers and keep those numbers in variables num1 and num2 respectively for the first 4 options mentioned above.
# Ask the user to enter two more numbers as first and second for calculating the average as soon as the user chooses an option 5.
# At the end if the answer of any operation is Negative print a statement saying “NEGATIVE” NOTE: At a time a user can only perform one action.

print("""
Enter 1 for Addition
Enter 2 for Subtraction
Enter 3 for Division
Enter 4 for Multiplication
Enter 5 for Average 
""")
a = int(input("Enter the option:"))
if a <= 4:
    num1 = eval(input("enter the first number:"))
    num2 = eval(input("enter the second number:"))
    if a == 1:
        add = num1+num2
        print(add)
        if add < 0:
            print('Negative')
    elif a == 2:
        sub = num1-num2
        print(sub)
        if sub < 0:
            print('Negative')
    elif a == 3:
        div = num1/num2
        print(div)
        if div < 0:
            print('Negative')
    elif a == 4:
        mul = num1*num2
        print(mul)
        if mul < 0:
            print('Negative')

elif a == 5:
    first = eval(input("enter the first number:"))
    second = eval(input("enter the first number:"))
    avg = (first+second)/2
    print(avg)
    if avg < 0:
        print('Negative')

#problem3 Write a program in Python to implement the given flowchart:
a = 10
b = 20
c = 30

avg = (a+b+c)/3
print("Average is", avg)
if avg>a and avg>b and avg>c:
    print("Avg is higher than a b c")
elif avg>a and avg>b:
    print("Avg is higher than a,b")
elif avg>a and avg>c:
    print("Avg is higher than a,c")
elif avg>b and avg>c:
    print("Avg is higher than b,c")
elif avg>a:
    print("Avg is just higher than a")
elif avg>b:
    print("Avg is just higher than b")
elif avg>c:
    print("Avg is just higher than c")

#problem 4: Write a program in Python to break and continue if the following cases occurs:
#If user enters a negative number just break the loop and print “It’s Over”
#If user enters a positive number just continue in the loop and print “Good Going”


# Problem5: Write a program in Python which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200.
for i in range(2000,3200):
    if i % 7 == 0 and i % 5 != 0:
        print(i)

#Problem 6: What is the output of the following code examples?
x = 123
for i in x:
    print(i)
# # Answer: it will give error as x doesnt have range

i= 0
while i < 5:
      print(i)
      i += 1
      if i == 3:
          break
      else:
         print("error")
# Ans: 0
# error
# 1
# error
# 2

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
          break

#answer 0
1
2
3
4

# problem 7 Write a program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected output: 0 1 2 4 5

i = 0
while i < 6:
    if i == 3:
        i=i+1
        continue
    print(i)
    i = i + 1


# Prob8. Write a program that accepts a string as an input from the user and calculate the number of digits and letters.

s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)