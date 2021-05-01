# 1. Create a list of given structure and get the Access list as provided below:
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

# Access list: [1, 2, 3, 4]
print(x[5][0:4])

# Access list: [600, 700]
print(x[-3:-1])

# Access list: [100, 300, 500, 600, 800]
print(x[::2])

# Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
print(x[::-1])

# Access list: [10]
print(x[5][5][0])

# Access list: [ ]
print(x[:0])

----------------------------------------------------------------------------------------------------------------

# 2. Create a list of thousand numbers using range and xrange and see the difference between each other.

L = list(range(0,1001))
print(L)

----------------------------------------------------------------------------------------------------------------

#3. How Tuple is beneficial as compared to the list?
1. Tuple consume less memory as compared to the list
2. The implication of iterations is comparatively Faster than list
3. The unexpected changes and errors are more likely to occur in list than  tuple

----------------------------------------------------------------------------------------------------------------

# 4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
# the number which is divisible by 3 and is a multiple of 2.

seq = [x for x in range(1,1101)]
result = filter(lambda x: x % 3 == 0 and x % 2 == 0,seq)
print(list(result))

----------------------------------------------------------------------------------------------------------------
# 5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
# string with their index

----------------------------------------------------------------------------------------------------------------

# 6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
# string which is having an even length.


A = "hello my name is Gauri Nade"
B = A.split(" ")

Result = filter(lambda x: len(x)%2==0,B)
output = " ".join(list(Result))

print(output)

----------------------------------------------------------------------------------------------------------------


----------------------------------------------------------------------------------------------------------------
# 8. Write a program in Python to complete the following task:
# Create two lists such as even_list and odd_list
# Ask user to enter a number in the range of 1,50 and make sure if the entered number is
# even, append it to the even_list and if the entered number is odd append it to the odd_list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you enter all the 5 elements, calculate the sum of the list and return the
# maximum of the list.

even_list = []
odd_list = []
i = 0

while True:
    A = int(input('Enter the number in range 1-50'))
    if A % 2 == 0:
        even_list.append(A)
        if len(even_list) == 5:
            break
    if A % 2 != 0:
        odd_list.append(A)
        if len(odd_list) > 6:
            break

print('even list: ',even_list)
print('Odd list:', odd_list)
print("sum of even list", sum(even_list))
print('sum of odd list', sum(odd_list))

----------------------------------------------------------------------------------------------------------------
# 9.Write a program to find out the occurrence of a specific character from an alphanumeric string.
# Sample input: 12abcbacbaba344ab
# Expected output: a=5 b=5 c=2

inputString = input("Enter a string: ")

i = ''
for char in inputString:
    if char not in i:
        print(char, '- ', inputString.count(char))
        i = i+char


----------------------------------------------------------------------------------------------------------------
# 10. Generate and print another tuple whose values are even numbers in the given tuple
# (1,2,3,4,5,6,7,8,9,10).

given_Tuple = (1,2,3,4,5,6,7,8,9,10)
new = []
for i in given_Tuple:
    if i%2 == 0:
        new.append(i)
print(tuple(new))
