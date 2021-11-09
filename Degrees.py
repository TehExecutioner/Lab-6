# Noah Martinez
# 11/5/21
# Search the internet for how to convert radians to degrees.
# Write a program to compute the conversion given a user input value.
# Print this value as well as the calculated value using the degrees function in the math module.

import math
x=int(input("type an angle that will be converted from radians to degrees: "))
print(x*180//3.14159)
print(math.degrees(x))