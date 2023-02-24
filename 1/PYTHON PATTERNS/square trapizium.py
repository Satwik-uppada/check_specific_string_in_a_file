n=int(input("Enter number of rows you wanna print: "))

for i in range(n):
    for j in range(i,n):
        print(" ",end="")

    for j in range(n):
        print("*" ,end="  ")
    print()

