# File commands
# open() -for opening the  file
# satwik is a text file created in python
f=open("satwik",'r') #'r' for read mode
content=f.read()
print(content)
f.close()
# close() -for closing the file

f=open("satwik","r")
content=f.readlines()
print(content)
f.close()
