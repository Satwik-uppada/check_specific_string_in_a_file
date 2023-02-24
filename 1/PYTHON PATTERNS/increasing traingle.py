n=int(input("Enter number of rows you wanna print: "))

for i in range(n):
    for j in range(i+1):
        print("*" ,end=" ")
    print()