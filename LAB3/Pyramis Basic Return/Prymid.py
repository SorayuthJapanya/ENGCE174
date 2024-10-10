def draw_pattern(length):
    pattern = []
    for i in range(length):
        line = ""
        for j in range(length - i - 1):
            line += "  "
        for j in range(i + 1):
            line += "*  "
        pattern.append(line)
        print(line)
    return pattern

length = int(input("Enter length: "))
pattern = draw_pattern(length)
