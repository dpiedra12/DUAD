grade_counter = 0
passed_grade_count = 0
failed_grade_count = 0
average_passed_grade = 0
average_failed_grade = 0
total_average_grade = 0

total_grades = int(input("Enter the number of grades: "))

while (grade_counter < total_grades):
    print(f"Enter grade number {grade_counter}")
    grade_counter += 1
    current_grade = int(input("Enter the grade: "))

    if (current_grade < 70):
        failed_grade_count += 1
        average_failed_grade += current_grade
        
    else:
        passed_grade_count += 1
        average_passed_grade += current_grade
    total_average_grade += (current_grade / total_grades)   

average_failed_grade /= failed_grade_count
average_passed_grade /= passed_grade_count

print("")
print(f"The student has this number of passed grades: {passed_grade_count}")
print(f"This is the average of passed grades: {average_passed_grade}")
print(f"The student has this number of failed grades: {failed_grade_count}")
print(f"This is the average of failed grades: {average_failed_grade}")
print(f"This is the total average of grades: {total_average_grade}")
