#Given a list of student greades, calculate the average grade for each student and store them in a dictionary

grades = {'Alice': [85, 90, 92],'Bob': [88, 87, 85],'Charlie': [90, 91, 89]}
average_grade = {}

for student, grades_list in grades.items():
    average_grade[student] = sum(grades_list) / len(grades_list)

print("Average Grades :",average_grade)