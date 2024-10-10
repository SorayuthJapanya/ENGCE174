def generate_pattern(length):
    result = []
    for i in range(length, 0, -1):
        row = ""
        for j in range(0, length - i):
            row += "  "  # เพิ่มช่องว่าง 2 ช่อง
        for j in range(0, i):
            row += "*  "  # เพิ่มเครื่องหมาย * และช่องว่าง
        result.append(row)
    return result

# การใช้งาน
length = int(input("Enter length: "))
pattern = generate_pattern(length)
for line in pattern:
    print(line)
