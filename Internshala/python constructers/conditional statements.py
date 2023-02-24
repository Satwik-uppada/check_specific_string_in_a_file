# i=int(input("Enter a number between 0 and 100:"))
#
# if i>=0 and i<=100:
#     if i>=60 and i<80:
#         print("Okay..!")
#     elif i>=80:
#         print("Good")
#     else:
#         print("Needs improvement")
# else:
#     print("Please provide a suitable number in given interval")



# nested conditional statements

i=int(input("Enter a number : "))

if i>50:
    print("{} is greater than 50.".format(i))
    if i%2 ==0:
        print("{} is an even number".format(i))
    else:
        print("{} is not an even number".format(i))
else:
    print("{} is less than 50.".format(i))
    if i%2 !=0:
        print("{} is an odd number.".format(i))
    else:
        print("{} is not an odd number.".format(i))