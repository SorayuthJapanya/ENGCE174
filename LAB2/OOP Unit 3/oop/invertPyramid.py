def pattern(length):
    if length == 0:
        return
    else:
        print(' ' * (lengths - length) + '* ' * length)
        pattern(length - 1)

lengths = int(input("number of rows : "))
pattern(lengths)
