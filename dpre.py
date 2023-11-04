import numpy as np 
import pandas as pd
import sys
from subprocess import run


file_path=input("Enter Path for preprocessing: ")
df = pd.read_csv(file_path)
   
# Data Cleaning

df.isnull().sum()
df['Age']= df["Age"].fillna(df["Age"].mean())
df['Cabin']=df['Cabin'].fillna(df["Cabin"].mode()[0])
df.Embarked[df.Embarked.isna()]
df['Embarked']=df['Embarked'].fillna(df["Embarked"].mode()[0])
df.Age.isnull().sum()


# Data Transformation
df=pd.get_dummies(df,columns=['Sex','Embarked'])

# Scale the 'Fare' feature by dividing it by the mean fare
mean_fare = df['Fare'].mean()
df['Fare_scaled'] = df['Fare'] / mean_fare

# Data Reduction
df['FamilySize'] = df['SibSp'] + df['Parch']
df.drop(['SibSp','Parch','Fare'],axis=1,inplace=True)


# Data Discretization

bins = [0, 18, 35, 50, 100]
labels = ['0-18', '18-35', '35-50', '50+']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)
df.drop('Age',axis=1,inplace=True)

# Save df to another csv
df.to_csv('res_dpre.csv',index=False)
print("Data saved to res_dpre.csv")

run(['python', 'eda.py', file_path], check=True)