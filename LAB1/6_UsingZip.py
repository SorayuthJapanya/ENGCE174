names = ["Alice", "Bob", "charlie"]
age = [25, 30, 35]
city = ["New York", "LOs Angeles", "Chicago"]

# Using Zip() for parallel iteration
for name, age, city in zip(names,age,city):
    print(f"{name} is {age} years old and lives in {city}")