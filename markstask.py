# Step 1: Create the dictionary
student_marks = {
    "Tushar": 88,
    "Mandar": 76,
    "Vinda": 92,
    "Rashmi": 81
}

# Step 2: Ask the user for a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show a 'not found' message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student '{name}' not found in the records.")