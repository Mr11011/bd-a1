import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
from subprocess import run

file_path=input("Enter Path For Visuals: ")
df = pd.read_csv(file_path)

# Extract data from 'Pclass' and 'Fare_scaled' columns
Pclass_df = df['Pclass']
fare_df = df['Fare_scaled']
plt.scatter(Pclass_df, fare_df, marker='o')
plt.title('Pclass vs. Fare')
plt.xlabel('Fare')
plt.ylabel('Pclass')
plt.savefig('vis.png', dpi=300, bbox_inches='tight')
print("visual done")

run(['python', 'model.py', file_path], check=True)
