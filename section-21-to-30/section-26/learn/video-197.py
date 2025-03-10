numbers = [2, 0, 0, 8, 1, 9, 9, 4]
new_numbers = [item + 1 for item in numbers]
print(new_numbers)

double = [item * 2 for item in range(1, 5) if item % 2 == 0]
print(double)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)