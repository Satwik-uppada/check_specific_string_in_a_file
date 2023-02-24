import random
name=input("Enter your name: ")
age=int(input("Enter your age: "))
age=str(age)
set=name+age
length=8
password="".join(random.sample(set,length))
print(password)