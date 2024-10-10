#tuple initialization 
coordinates = (3, 5)

# Unpacking tuples
x ,y = coordinates
print("x-coordinates : ",x)
print("y-coordinates : ",y)

# Tuples as keys in dictionary
location = {(3, 5): "Home", (10,20): "office"}
print("Location at (3,5):",location[(3,5)])