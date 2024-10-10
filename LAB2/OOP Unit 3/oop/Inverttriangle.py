def pattern(length, current=1):
    if current > length:
        return
    else:
        print("  " * (length - current) + "* " * current)
        pattern(length, current + 1)

length = int(input("number of rows : "))
pattern(length)
