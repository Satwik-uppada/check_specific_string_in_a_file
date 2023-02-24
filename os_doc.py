import os
## current working directory
print(os.getcwd())
## change the directory
print(os.chdir("C:\\Users\\uppada satwik\\OneDrive\\Documents"))
print(os.getcwd())

# all the contents(sub_folders and files in cwd)
print(os.listdir())

#make/create a new folder/directory
os.mkdir("C:\\Users\\uppada satwik\\Downloads\\heck","w")
os.write("happy birthday bro")



