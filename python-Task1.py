# Problem 1:Create three variables in a single line and assign values to them in such a manner that each one of
# them belongs to a different data type
a,b,c = 21,3.14,"python"
print("a:",a,"b:",b,"C:",c)

#problem 2: Create a variable of type complex and swap it with another variable of type integer.
a = 3 + 4j
b = 65
print(type(a))
print(type(b))
print('Before swapping value of a and b are respectively', a,",", b )
a,b = b,a
print('After swapping value of a and b are respectively', a,",", b)

#problem 3: Swap two numbers using a third variable and do the same task without using any third variable
a = 10
b = 'Python'
print('Before swapping value of a and b are respectively', a,",", b)
c = a
a = b
b = c
print('Before swapping value of a and b are respectively', a,",", b)

a = 10
b = 'Python'
print('a:',a,'b:',b)
a,b = b,a
print('a:',a,'b:',b)
a,b = b,a

#problem 4: Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
#Version.
a = int(input("enter the number to be printed on the screen"))
print(a)

#Problem 5: Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
#another variable called z. Add 30 to z and store the output in variable result and print result as the
#final output.
a = int(input('Enter the 1st number between 2-10:'))
b = int(input('Enter the 2nd number between 2-10:'))
z = a + b
result = 30 + z
print(result)

# problem 6: Write a program to check the data type of the entered values.
a = eval(input("Enter the value of any data type:"))
print(type(a))

# Problem 7: Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.

#Problem 8: If one data type value is assigned to ‘a’ variable and then a different data type value is assigned
# to ‘a’ again. Will it change the value? If Yes then Why?
a = 32
a = 3.14
print(a)
