def print_all_patterns(length):
    print("Pattern 1:")
    for i in range(length, 0, -1):
        for j in range(0, length - i):
            print(" ", end=" ")
        for j in range(0, i):
            print("*  ", end=" ")
        print()
    print()
    
    print("Pattern 2:")
    for i in range(length, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print()
    print()
    
    print("Pattern 3:")
    for i in range(length):
        for j in range(length - i - 1):
            print(" ", end=" ")
        for k in range(i + 1):
            print("*", end=" ")
        print()
    print()
    
    print("Pattern 4:")
    for i in range(length):
        for j in range(length - i - 1):
            print(" ", end=" ")
        for k in range(i + 1):
            print("*  ", end=" ")
        print()
    print()
    
    print("Pattern 5:")
    for i in range(length):
        for j in range(i + 1):
            print("*", end=" ")
        print()
    print()

# Example usage
length = int(input("Enter length: "))
print_all_patterns(length)
