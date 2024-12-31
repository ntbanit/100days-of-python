letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

def append_character(result_arr, input_number, source_arr):
    ll = len(source_arr)
    for count in range(0, input_number):
        index = random.randint(0, ll - 1)
        result_arr.append(source_arr[index])
    return result_arr

result = []
append_character(result, nr_letters, letters)
print(result)
append_character(result, nr_symbols, symbols)
print(result)
append_character(result, nr_numbers, numbers)

print(result)

random.shuffle(result)

result_str = ''.join(result)
print(f"You can use this password {result_str}")