import pandas
Raw_Housing_Data=pandas.read_csv("C:\\Users\\uppada satwik\\Downloads\\M3T2_helper_text\\1. Regression - Module - (Housing Prices).csv")

import matplotlib.pyplot as plt
print(plt.hist(Raw_Housing_Data['Age of House (in Years)'],bins=10))
plt.xlabel("Age of Houses(in Years")
plt.ylabel("No.of Records")
plt.title("Age Wise Distribution of Houses")
plt.show()



