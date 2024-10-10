#Example 1 : Working with dictionaries 

#Creating a dictionary of student grades
grades = {'Alice': 85,'Bob': 92,'Charlie': 88,'David': 95}

# Accessing Values using keys
print("Bob's grade:", grades['Bob']) #Output : Bob's grade : 92

#Adding a new entry
grades['Eve'] = 90

#Iterating through keys and values
for student ,grade in grades.items():
    print(f"{student}: {grade}")

# Using get() method to aviod keyError
print("Frank's grade:", grades.get('Frank', 'Grade not found'))
