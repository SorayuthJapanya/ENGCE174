def pattern(length):
    if length == 0:
        return []
    else:
        result = []
        result.append(' ' * (lengths - length) + '* ' * length)
        result.extend(pattern(length - 1))
        return result

lengths = int(input("number of rows : "))
result = pattern(lengths)
for line in result:
    print(line)