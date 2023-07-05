# Exercise 3

"""
Write a program to accept a string from the user and
display characters that are present at an even index number.
"""

str = input("Please enter a word or sentence: ")

str_length = len(str)

print("Letter at even indexes: \n")

for i in range(0, str_length, 2):
    print(str[i])

