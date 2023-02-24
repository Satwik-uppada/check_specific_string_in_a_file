f=open("satwik",'w') # 'w' stands for write mode
content=f.write("this is write mode ")  # file content will change with this content (replace)
# disadvantage:
#previous statement replace with new content
f=open("satwik","r")
content= f.read()
print(content)
f.close()