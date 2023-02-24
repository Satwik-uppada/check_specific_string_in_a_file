f=open("satwik",'a') # 'w' stands for write mode
content=f.write("\nthis will add upon to the previous data in ur file ")  # file content will change with this content (replace)
#advantage:
#previous statement will not replace with new content
# it will add new data to its previous data without erasing
f=open("satwik","r")
content= f.read()
print(content)
f.close()