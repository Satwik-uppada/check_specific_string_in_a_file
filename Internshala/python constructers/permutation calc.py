def factorial(value):
    fact=1
    for i in range(1,value+1):
        fact=fact*i
    return fact

n=int(input("Enter total no.of things: "))
r=int(input("Enter no.of things to be selected: "))
c=factorial(n)/factorial(n-r)
print(c)
