# def square(num):
#     result=num*num
#     return result
#
# a=int(input("Enter a Number to find square: "))
#
# print(square(a))



# n=int(input("Enter total no.of things: "))
# r=int(input("Enter no.of things to be selected: "))
#
# fact_n=1
# for i in range(1,n+1):
#     fact_n=fact_n * i
#
# fact_r=1
# for i in range(1,r+1):
#     fact_r=fact_r * i
#
# fact_n_r=1
# for i in range(1,(n-r)+1):
#     fact_n_r=fact_n_r * i
#
#
# c=fact_n/(fact_r * (fact_n_r))
# print(c)
#
# def fun(n,l=[]):
#     for i in range(n):
#         l.append(i*i)
#         print(i)
# fun(2)

# i=0
# while i<6:
#     print(i)
#     i+=2
# else:
#     print(0)

# i=1
# while True:
#     if i%9==0:
#         break
#     print(i+4)
#     i+=2
#
# string_l='internshala'
# for i in range(len(string_l)):
#     print(string_l)
#     string_l='z'

def func(x,y):
    if x>y:
        return x
    elif x==y:
        return x,y
    else:
        return y

print(func(20,30))


