lenght = int(input("Enter lenght :"))
for i in range(lenght):
    for j in range(lenght-i-1):
        print(" " ,end=" ")
    for j in range(i+1):
        print("*  ",end= " ")
    print()