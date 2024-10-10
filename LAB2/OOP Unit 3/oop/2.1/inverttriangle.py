lenght = int(input("Enter lenght :"))
for i in range(lenght):
    for j in range(lenght-i-1):
        print(" ",end = " ")
    for i in range(i+1):
        print("*",end=" ")     
    print()