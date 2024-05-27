num_students = int(input("Enter the number of students: "))

i = 1
while i <= num_students:
    total_grade = 0
    Num_of_subject =int(input(f"Enter the number of subject for student {i}:"))

    for j in range(1, Num_of_subject+1):
        grades = float(input(f"Enter grade for subject {j} of student {i} :"))
        total_grade += grades
    
    average_grade = total_grade / Num_of_subject
    print(f"Average grade for student {i} is {average_grade}:")
    i += 1