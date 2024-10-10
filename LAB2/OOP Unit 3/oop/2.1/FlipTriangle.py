lenght = int(input("Enter lenght :"))

for i in range(lenght,0,-1):
    for j in range(0,i):
        print("*",end = " ")
    print()