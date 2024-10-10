def pattern(length):
    result = ""
    if length == 0:
        return result
    else:
        result += pattern(length - 1)
        result += ' ' * (lengths - length) + '* ' * length + '\n'
        return result

lengths = int(input("number of rows : "))
output = pattern(lengths)
print(output)
