def generate_pattern(length):
    pattern = []
    for i in range(length):
        line = ""
        for j in range(i + 1):
            line += "* "
        pattern.append(line)
        print(line)
    return pattern

length = int(input("Enter length: "))
pattern = generate_pattern(length)
