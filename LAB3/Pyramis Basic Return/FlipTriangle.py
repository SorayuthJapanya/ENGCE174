def generate_pattern(length):
    result = []
    for i in range(length, 0, -1):
        row = ""
        for j in range(i):
            row += "* "
        result.append(row.strip())  # ใช้ strip() เพื่อลบช่องว่างท้ายบรรทัด
    return result

# การใช้งาน
length = int(input("Enter length: "))
pattern = generate_pattern(length)
for line in pattern:
    print(line)
