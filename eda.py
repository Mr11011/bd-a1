import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
from subprocess import run

file_path=input("Enter Path for Insights: ")
df = pd.read_csv(file_path)
df.describe()
df.value_counts()

fig, ax = plt.subplots(figsize=(9, 10))

df.hist(ax=ax, grid=False)
df.corr()
# Specify the numerical column for which you want to detect outliers
numerical_column = 'FamilySize'


# Calculate the IQR (Interquartile Range) for the chosen column
Q1 = df[numerical_column].quantile(0.25)
Q3 = df[numerical_column].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify and save outliers in a separate DataFrame
outliers = df[(df[numerical_column] < lower_bound) | (df[numerical_column] > upper_bound)]

# Save the outliers to a text file
outliers.to_csv('outliers.txt', index=False)

# Print the outliers for further inspection (optional)
print("Outliers:")
print(outliers)

# Identify and save outliers in a separate DataFrame
outliers = df[(df[numerical_column] < lower_bound) | (df[numerical_column] > upper_bound)]
outliers.to_csv('outliers.txt', index=False)
print("Outliers:")
print(outliers)

# Define your insights
insight_1 ="Several passengers in the dataset have larger family sizes, with a FamilySize of 4 or more. For example, passenger '8' has a FamilySize of 4, and passenger '863' has a FamilySize of 10. These family sizes are larger than the average family size."
insight_2 = "The 'Fare_scaled' column shows varying fare values, with a range from 0.598 to 2.159. Some passengers, like '863,' paid significantly higher fares compared to the average fare."
insight_3 = "The repeated 'B96 B98' cabin suggests that the Titanic had shared accommodations or cabins, possibly due to traveling as a group or family. It's important to explore the reasons behind this shared cabin and how it might have impacted the passengers' experiences on the ship."

# Save insights as text files
with open("eda-in-1.txt", "w") as file1:
    file1.write("Insight 1: " + insight_1)

with open("eda-in-2.txt", "w") as file2:
    file2.write("Insight 2: " + insight_2)

with open("eda-in-3.txt", "w") as file3:
    file3.write("Insight 3: " + insight_3)

print("Insight done")
run(['python', 'vis.py', file_path], check=True)