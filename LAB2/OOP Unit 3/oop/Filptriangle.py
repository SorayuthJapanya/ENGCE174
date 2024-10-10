def pattern(lenght):
    if lenght == 0:
        return
    else:
        pattern(lenght-1)
        print(" "*lenght)
        print("* "*lenght)

lenght = int(input("number of rows : "))
pattern(lenght)
