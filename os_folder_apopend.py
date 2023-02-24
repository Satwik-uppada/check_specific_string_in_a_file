import os
our_folder="C:\\Users\\uppada satwik\\Downloads\\heck"
os.chdir(our_folder)

contents=os.listdir()

files=[]
for name in contents:
    if os.path.isfile(name):
        files.append(name)
# print(contents)
# print(files)
Docs=['pdf','']
Audios=[]
Misc=[]
Videos=["mp4","mkv"]
Images=["jpeg","jpg","png","webp","gif","svg"]

folder_names=["Docs","Images",'Videos',"Misc","Audios"]
for i in folder_names:
    os.mkdir(i)
for filename in files:
    ext=filename.split(" . ")[-1]
    source=