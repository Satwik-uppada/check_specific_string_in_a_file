import pandas
Raw_Housing_Data=pandas.read_csv("C:\\Users\\uppada satwik\\Downloads\\M3T2_helper_text\\1. Regression - Module - (Housing Prices).csv")

import matplotlib.pyplot as plt
plt.scatter(x=Raw_Housing_Data['Flat Area (in Sqft)'],y=Raw_Housing_Data['Sale Price'],color="red")
plt.xlabel("Area")
plt.ylabel("Selling Price")
plt.title("Area vs Selling price")
plt.show()


plt.scatter(x=Raw_Housing_Data['No of Bathrooms'],y=Raw_Housing_Data['Sale Price'],color="skyblue")
plt.xlabel("No of Bathrooms")
plt.ylabel("Selling Price")
plt.title("Bathrooms vs Selling price")
plt.show()



plt.scatter(x=Raw_Housing_Data['Age of House (in Years)'],y=Raw_Housing_Data['Sale Price'],color="blue")
plt.xlabel("Age of House")
plt.ylabel("Selling Price")
plt.title("Age of House vs Selling price")
plt.show()
