def pattern(lenght):
    result = ""
    if lenght == 0:
        return result
    else:
        result += pattern(lenght-1)
        result += "* " * lenght + "\n"
        return result

lenght = int(input("number of rows : "))
output = pattern(lenght)
print(output)
