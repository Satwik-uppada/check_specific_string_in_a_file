# # fizz buzz
#
# n=int(input("Enter upto how many no's u wanna try: "))
# while n>0:
#
#  for i in range(1,n+1):
#        if i%3==0 and i%5==0:
#           print("Fizz Buzz")
#        elif i%5==0:
#            print("Buzz")
#        elif i%3==0:
#          print("Fizz")
#        else:
#           print(i)
#
# else:
#     print("please provide number greater than 0")

# fizz buzz with function

def fizz_buzz(n):

    output=[]
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            output.append("Fizz Buzz")
        elif i%5==0:
               output.append("Buzz")
        elif i%3==0:
               output.append("Fizz")
        else:
              output.append(str(i))
    return output

print(fizz_buzz(15))