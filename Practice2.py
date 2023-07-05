"""
Write a program to iterate the first 10 numbers and in
each iteration, print the sum of the current and previous number
"""

# Done using a simple for loop, and the range function

previous_num = 0
for i in range(0, 10, 1):
    sum = previous_num + i
    print(f"Current number: {i} Previous num: {previous_num} "
          f"Sum: {sum}")
    previous_num = i
