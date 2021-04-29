#1. Write a program in Python to allow the error of syntax to be handled using exception handling.
 Syntax errors are not handled by exception.
---------------------------------------------------------------------------------------------------
#2.  Write a program in Python to allow the user to open a file by using the argv module.
# If the entered name is incorrect throw an exception and ask them to enter the name again.
# Make sure to use read only mode.

---------------------------------------------------------------------------------------------------
# 3.Write a program to handle an error if the user entered a number more than four digits
# it should return “The length is too short/long !!! Please provide only four digits”

A = input('Enter the four digit number:')
print(len(A))

try:
    if len(A) < 4:
        raise Exception
    elif len(A) == 4:
        print("entered a correct digit number")
except Exception as x :
    print("The length is too short",x)

try:
    if len(A) > 4:
        raise Exception

except Exception as y :
    print("The length is too long", y)

-------------------------------------------------------------------------
# 4. Create a login page backend to ask users to enter the username and password.
# Make sure to ask for a Re-Type Password and if the password is incorrect give chance to enter it again
# but it should not be more than 3 times.

A = input("enter the Username:")
password = '12345'
i = 0
for i in range(3):
    B = input("enter the Password:")
    if B == password:
        print('correct password')
        break
    else:
        print('Incorrect password, remaining try:', 2-i)
-----------------------------------------------------------------------------------------------------------

#5. Go through the link provided below to understand finally and raise concept:
Done

-----------------------------------------------------------------------------------------------------------
#6. 6. Read doc.txt file using Python File handling concept and return only the even length string from the file.
# Consider the content of doc.txt as given below: