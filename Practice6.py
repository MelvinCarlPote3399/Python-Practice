# Practice question 6

"""
Iterate the given list of numbers and print only those numbers which are divisible by 5
"""

num_list = [10, 20, 33, 46, 55]

print(num_list)
print("These numbers are divisible by 5:\n")

for num in num_list:
    if num % 5 == 0:
        print(num)
