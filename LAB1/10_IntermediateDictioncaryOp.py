# Dictionary intialization
person = {'name':'Alice', 'age':30, 'city': 'New York'}

# Accessing values
print("Name:", person['name'])

# Updating values
person['age'] = 31
print("Updated age:", person['age'])

#Interating through keys and vlues
for key, value in person.items():
    print(f"{key}: {value}")