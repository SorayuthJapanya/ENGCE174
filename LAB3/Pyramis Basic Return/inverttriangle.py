def generate_triangle_pattern(length):
    result = []
    for i in range(length):
        row = ""
        # เพิ่มช่องว่างทางซ้าย
        for j in range(length - i - 1):
            row += "  "  # เพิ่มช่องว่าง 2 ช่อง
        # เพิ่มเครื่องหมาย *
        for j in range(i + 1):
            row += "* "
        result.append(row.strip())  # ใช้ strip() เพื่อลบช่องว่างท้ายบรรทัด
    return result

# การใช้งาน
length = int(input("Enter length: "))
pattern = generate_triangle_pattern(length)
for line in pattern:
    print(line)
