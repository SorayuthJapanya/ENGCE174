def pattern(length):
    if length == 0:
        return
    else:
        pattern(length - 1)
        print(' ' * (lengths - length) + '* ' * length)

lengths = int(input("number of rows : "))
pattern(lengths)
