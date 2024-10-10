grades = {'Alice': [85, 90, 92], 'Bob': [88, 87, 85], 'Chalie': [90, 91, 89]}
average_grades = {}

for student, grade_list in grades.items():
    average_grades[student] = sum(grade_list) / len(grade_list)
    
print("Average Grades:", average_grades)