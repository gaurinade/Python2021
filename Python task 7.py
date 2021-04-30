# 1. Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.

D = int(input("enter the value of D:"))
C = 50
H = 30
result = ((2*C*D)/H) ** 0.5
print(result)

-------------------------------------------------------------------------------------------------
#2 Define a class named Shape and its subclass Square.
# The Square class has an init function which takes length as argument.
# Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default

class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

square_result= Square(5)
print(square_result.area())
-------------------------------------------------------------------------------------------------
# 3.Create a class to find three elements that sum to zero from a set of n real numbers
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Expected output: [[-10,2,8],[-7,-3,10]]

class real_number:
 def threeSum(self, nums):
        nums = sorted(nums)
        result = []
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(real_number().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

-------------------------------------------------------------------------------------------------
# Q4 and Q5 ---> not able to solve