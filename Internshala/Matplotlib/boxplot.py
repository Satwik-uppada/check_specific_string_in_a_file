import pandas
Raw_Housing_Data=pandas.read_csv("C:\\Users\\uppada satwik\\Downloads\\M3T2_helper_text\\1. Regression - Module - (Housing Prices).csv")

import matplotlib.pyplot as plt
plt.boxplot(Raw_Housing_Data['Age of House (in Years)'])
plt.show()






















