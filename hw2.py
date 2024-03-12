import pandas as pd
import numpy as np
"""1) From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0)."""
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
result1 = df.loc[::20, ['Manufacturer', 'Model', 'Type']]

"""
2) Replace missing values in Min.Price and Max.Price columns with their respective mean (check documentation)."""
min_price_mean = df['Min.Price'].mean()
max_price_mean = df['Max.Price'].mean()

"""
3) How to get the rows of a dataframe with row sum > 100?"""
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
filtered_rows = df[df.sum(axis=1) > 100]

"""4)Create a 4x4 NumPy array filled with random integers between 1 and 100. Then, reshape 
this array into two separate 2D arrays, where one represents the rows and the other represents the columns. 
Write a function, preferably using a lambda function, to calculate the sum of each row and each column separately, 
and return the results as two separate NumPy arrays
"""
random = np.random.randint(1, 101, size=(4, 4))

rows_array = random.reshape(2, 8)
columns_array = random.T.reshape(2, 8)

sum_row = lambda arr: np.sum(arr, axis=1)
sum_column = lambda arr: np.sum(arr, axis=0)

sum_rows_result = sum_row(rows_array)
sum_columns_result = sum_column(columns_array)
print(sum_rows_result)
print(sum_columns_result)




