import pandas
Raw_Housing_Data=pandas.read_csv("C:\\Users\\uppada satwik\\Downloads\\M3T2_helper_text\\1. Regression - Module - (Housing Prices).csv")

print(Raw_Housing_Data.groupby("Condition of the House")['ID'].count())

values=(30,1701,14031,5679,172)
labels=('Bad',"Excellent","Fair","Good","Okay")

import matplotlib.pyplot as plt
plt.bar(labels,values,color="blue",linewidth="5",linestyle="dashed")
plt.xlabel("Condition if the House")
plt.ylabel("Count of the House")
plt.title("Bar graph ")
plt.show()

