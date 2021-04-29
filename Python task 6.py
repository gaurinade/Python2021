# 1. Write a program in Python to find out the character in a string which is uppercase using list comprehension.
string = "HeLLo wOrLd"
print("original string is : " + str(string))
res = [c for c in string if c.isupper()]
print("The uppercase characters are : " + str(res))

#2. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects.
# The dictionary should map the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension.

students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
dictionary = zip(students, subjects)
print(dict(dictionary))

#3. 3. Learn More about Yield, next and Generators

# 4.  Write a program in Python using generators to reverse the string.
# Input String = “Consultadd Training”
def reverse_string(string):
    length = len(string)
    for i in range(length - 1, -1, -1):
        yield string[i]

for x in reverse_string("Consultadd Training"):
    print(x)

