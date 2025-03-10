import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {name:random.randint(1, 100) for name in names}
print(student_scores)

passed_students = {key:value for (key, value) in student_scores.items() if value >= 50}
print("Passed ones:")
print(passed_students)