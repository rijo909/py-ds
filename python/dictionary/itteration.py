# Print Bob's Science score.
# Add a new subject "English" with scores: Alice: 88, Bob: 75, Charlie: 82.
# Find the student with the highest Math score.

students = {
    "Alice": {"Math": 90, "Science": 85},
    "Bob": {"Math": 80, "Science": 88},
    "Charlie": {"Math": 85, "Science": 92}
}
print(students['Bob']['Science'])

# zip
students = {
    "Alice": {"Math": 90, "Science": 85},
    "Bob": {"Math": 80, "Science": 88},
    "Charlie": {"Math": 85, "Science": 92}
}
lst1 = [88, 75, 82]
c1 = 0
for i,j in zip(students, lst1):
    print(i,j)
    students[i]["English"] = j
print(students)

# add through input iteration
# students = {
#     "Alice": {"Math": 90, "Science": 85},
#     "Bob": {"Math": 80, "Science": 88},
#     "Charlie": {"Math": 85, "Science": 92}
# }
# for i in students:
#     n = input(f"Enter marks of {i} : ")
#     students[i]["English"] = n
# print(students)

# items
students = {
    "Alice": {"Math": 90, "Science": 85},
    "Bob": {"Math": 80, "Science": 88},
    "Charlie": {"Math": 85, "Science": 92}
}
for i,j in students.items():
    print(f"Marks of Student {i} : {j}")

# enumerate
students = {
    "Alice": {"Math": 90, "Science": 85},
    "Bob": {"Math": 80, "Science": 88},
    "Charlie": {"Math": 85, "Science": 92}
}
for i,j in enumerate(students):
    print(f"{i} : {j}")

# max mark in maths code :
students = {
    "Alice": {"Math": 90, "Science": 85},
    "Bob": {"Math": 96, "Science": 88},
    "Charlie": {"Math": 85, "Science": 92}
}
max_math_mark = 0
max_math_student = ''
for i in students:
    if students[i]['Math']>max_math_mark:
        max_math_mark = students[i]['Math']
        max_math_student = i
print(f'{max_math_student} scored the highest mark of {max_math_mark}')