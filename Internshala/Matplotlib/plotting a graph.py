import pandas
Raw_Housing_Data=pandas.read_csv("C:\\Users\\uppada satwik\\Downloads\\M3T2_helper_text\\1. Regression - Module - (Housing Prices).csv")


import matplotlib.pyplot as plt
# plt.plot(Raw_Housing_Data['Sale Price'])
# plt.show()

plt.plot(Raw_Housing_Data['Sale Price'],color="red")
plt.xlabel("Record  Number")
plt.ylabel("Sale Price")
plt.title("My First Graph")
plt.show()