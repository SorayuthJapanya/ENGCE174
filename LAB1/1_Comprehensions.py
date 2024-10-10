#List COmprehension
squares = [x**2 for x in range(10)]

# Directionary comprehension
squares_dict = {x: x**2 for x in range(5)}

# Set comprehension
even_squares = {x**2 for x in range(10) if x % 2 == 0}    #แสดงตัวที่หารแล้วไม่มีเศษ หรือหารได้ลงตัว

print(squares)
print(squares_dict)
print(even_squares)