# print statement
print("Hello LPU")  # printing statement

# taking input and storing it  im a variable


# Data types-> int ,float , str ,bool ,None

age = 56
height = 182.4
name = "Satwik"
value = True

print(type(height))  # printing the type of height
print(type(value))  # printing the type of value
print(type(age))  # printing the type of age
type(name)  # it will not print anything in pycharm ....but the line will give an output in jupyter notebook


# taking default input as string
inp = str(input())
print(inp)
print(type(inp))

num= int(input("Enter any integer: "))
print(type(num))
print("The value u entered is :: ", num)


# In python, we can assign string data type in three types according to our necessary

# first one: using single quotes/double quotes if we have double quotes/single quotes in out string.(vice versa)
print('he is ,"a python staff". this is the first class')
print("he is ,'a python staff'. this is the first class")

# second one:using three double quotes
print("""he is ,"a python staff". this is the first class""")

# Third one:using right slash before quotes in text
print("he is ,\"a python staff\". this is the first class")

