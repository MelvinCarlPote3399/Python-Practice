# Exercise 4

"""
Remove first n characters from a string
"""

string = input("Please enter a word or sentence: ")
num = int(input("Please enter a number: "))


def remove_chars(word, index):
    new_word = word[index:]
    return new_word


print(f"New word: {remove_chars(string, num)}")
