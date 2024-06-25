students = {}
for i in range(3):
    id: str = input(f"Enter student number {i + 1}: ")
    name = input(f"Enter first name {i + 1}: ")
    students[id] = name

print("Student List:")
for sid in students:
    print(sid, students[sid])

students.pop(id)

id = input("Enter your student number: ")
name = input("Enter your first name: ")
students[id] = name

print("Student List:")
for sid in students:
    print(sid, students[sid])
