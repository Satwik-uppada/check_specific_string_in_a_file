import math

# Simple calculater with some operations

choice = int(input("List of operations performed in this calculater:"
                   "\n1.Addition"
                   "\n2.Subtraction"
                   "\n3.Multiplication"
                   "\n4.Division"
                   "\n5.Remainder"
                   "\n6.H.C.F"
                   "\n7.L.C.M"
                   "\n8.power"
                   "\n9.log"
                   "\n10.square_root"
                   "\n11.Modulo"
                   "\n12.percent"
                   "\nSelect one from above:\n"))  # taking option from user (which operation he/she want to do)



def add(num1, num2):
    try:
        sum = num1 + num2
        return sum
    except:
        return print("Error found in this function")


def subtract(num1, num2):
    try:
        diff = num1 - num2
        return diff
    except:
        return print('Error found in this function.')


def multiply(num1, num2):
    try:
        product = num1 * num2
        return product
    except:
        return print('Error found in this function')


def divide(num1, num2):
    try:
        quotient = num1 / num2
        return quotient
    except:
        return print('Error found in this function')


def rem(num1, num2):
    try:
        remainder = num1 % num2
        return remainder
    except:
        return print('Error found in this function')


def hcf(num1, num2):
    try:
        if num1 > num2:
            smaller_var = num2
        else:
            smaller_var = num1
        for i in range(1, smaller_var + 1):
            if (num1 % i == 0) and (num2 % i == 0):
                hcf = i
        return hcf
    except:
        return print("Error found in this function")


def lcm(num1, num2):
    try:
        if num1 > num2:
            higher_var = num1
        else:
            higher_var = num2
            value = higher_var
        while True:
            if higher_var % num1 == 0 and higher_var % num2 == 0:
                return higher_var
                break
            else:
                higher_var = higher_var + value
    except:
          return print("Error found in this function.")


def log(num, base):
    try:
        log_value = math.log(num, base)
        return log_value
    except:
        return print("Error found in this function.")


def power(num, exp):
    try:
        return num ** exp
    except:
        return print("Error found in this function.")


def square_root(num):
    try:
        return math.sqrt(num)
    except:
        return print("Error found in this function.")


def modulo(num1, num2):
    try:
        if num2 != 0:
            return num1 % num2
        return 'Division by zero not possible'
    except:
        return print("Error found in this function.")


def percent(num1, num2):
    try:
        return round(num1/num2 * 100, 2)
    except:
        return print("Error found in this function.")


if  choice== 10:
    num = int(input("Enter number to find square_root:"))  # taking input as num for only square_root operation
elif choice<13:
    first_number = int(input("Enter first-number: "))  # taking first-number input from user
    second_number = int(input("Enter second-number: "))  # taking second-number input from user
else:
    print("Choose correct operation from above list.")

if choice == 1:
    print("Sum of ({},{}) is: ".format(first_number,second_number),add(first_number, second_number))
elif choice == 2:
    print("Differance of ({},{}) is: ".format(first_number,second_number),subtract(first_number, second_number))
elif choice == 3:
    print("Product of ({},{}) is: ".format(first_number,second_number),multiply(first_number, second_number))
elif choice == 4:
    print("Quotient of ({},{}) is: ".format(first_number,second_number),divide(first_number, second_number))
elif choice == 5:
    print("Remainder of ({},{}) is: ".format(first_number,second_number),rem(first_number, second_number))
elif choice == 6:
    print("H.C.F of ({},{}) is: ".format(first_number,second_number),hcf(first_number, second_number))
elif choice == 7:
    print("L.C.M of ({},{}) is: ".format(first_number,second_number),lcm(first_number, second_number))
elif choice == 8:
    print("{} power of {} is: ".format(first_number,second_number),power(first_number, second_number))
elif choice == 9:
    print("Logarithm of {} having base {} is: ".format(first_number,second_number),log(first_number, second_number))
elif choice == 10:
    print("Square root of {} is: ".format(num),square_root(num))
elif choice == 11:
    print("{} mod {} is: ".format(first_number,second_number),modulo(first_number, second_number))
elif choice == 12:
    print("Percentage of ({},{}) is: ".format(first_number,second_number),percent(first_number, second_number))
else:
    print("Please choose correct operation from above list.")
