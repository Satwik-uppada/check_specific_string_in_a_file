import pandas
Raw_Housing_Data=pandas.read_csv("C:\\Users\\uppada satwik\\Downloads\\M3T2_helper_text\\1. Regression - Module - (Housing Prices).csv")
print(Raw_Housing_Data)

print(Raw_Housing_Data.dtypes)
print(Raw_Housing_Data.head(10))

print(Raw_Housing_Data.tail(10))

print(Raw_Housing_Data.describe())

print(Raw_Housing_Data.describe(include='all'))

print(Raw_Housing_Data.info())

print(Raw_Housing_Data['Sale Price'].mean())

print(Raw_Housing_Data['Sale Price'].min())

print(Raw_Housing_Data['Sale Price'].max())


print(Raw_Housing_Data['Sale Price'].std())

print(Raw_Housing_Data['Sale Price'].quantile(.25))


print(Raw_Housing_Data['Sale Price'].unique())

print(Raw_Housing_Data['Condition of the House'].unique())


print("-----------------------------------------------------------------------------------------------------------------------------------")

import numpy as np
print(np.std(Raw_Housing_Data['Sale Price']))

print(Raw_Housing_Data['Sale Price'].std()-np.std(Raw_Housing_Data['Sale Price']))

print(np.std(Raw_Housing_Data['Sale Price'],ddof = 1))