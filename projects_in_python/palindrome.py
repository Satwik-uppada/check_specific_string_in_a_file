n=int(input("Enter the number: "))

def isPalindrome(n):
    string=str(n)
    reverse_string=reversed(string)

    if reverse_string == string:
        print("True")
    else:
        print("False")

isPalindrome(n)