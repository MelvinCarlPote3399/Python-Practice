# Exercise 5

"""
Write a function to return True if the first and last number of a given list is same.
If numbers are different then return False.
"""

list_1 = [10, 20, 30, 40, 10]
list_2 = [75, 65, 35, 75, 30]


def check_list(number_list):
    first_num = number_list[0]
    last_num = number_list[-1]

    if first_num == last_num:
        return True
    else:
        return False


print("Testing our lists\n")

print(f"Testing list 1 --> {list_1}")
print(f"Result is: {check_list(list_1)}\n")
print(f"Testing list 2 --> {list_2}")
print(f"Result is: {check_list(list_2)}\n")