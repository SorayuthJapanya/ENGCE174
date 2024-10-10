def pattern(lenght):
    if lenght == 0:
        return ""
    else:
        result = pattern(lenght-1)
        result += " " * lenght + "\n"
        result += "* " * lenght + "\n"
        return result

lenght = int(input("number of rows : "))
output = pattern(lenght)
print(output)
