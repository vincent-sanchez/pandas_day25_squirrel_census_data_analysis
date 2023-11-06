# Import required libraries
import pandas as pd

# Lesson 230
df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231106.csv")

# Call group by method
squirrel_count = df.groupby(['Primary Fur Color'])['Primary Fur Color'].count()

# Cal to_csv method
squirrel_count.to_csv('squirrel_count.csv')

# Print contents of dataframe 'squirrel count'
print(squirrel_count)