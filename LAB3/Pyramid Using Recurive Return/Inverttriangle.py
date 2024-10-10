def pattern(length, current=1):
    if current > length:
        return []
    else:
        result = []
        result.append("  " * (length - current) + "* " * current)
        result.extend(pattern(length, current + 1))
        return result

length = int(input("number of rows : "))
result = pattern(length)
for line in result:
    print(line)
