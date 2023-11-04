
import numpy as np
import pandas as pd

data=pd.read_csv("res_dpre.csv")
data.head()

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

numerical_features = data[['FamilySize','Fare_scaled']]

k = 3

kmeans = KMeans(n_clusters=k, random_state=0)
kmeans.fit(numerical_features)

labels = kmeans.labels_

numerical_features['Cluster'] = kmeans.labels_


print(numerical_features)


plt.scatter(numerical_features['FamilySize'], numerical_features['Fare_scaled'], c=labels)
plt.xlabel('FamilySize')
plt.ylabel('Fare')
plt.title('K-means Clustering of Titanic Data')
plt.show()

cluster_counts = numerical_features['Cluster'].value_counts().sort_index()

# Reset the index to have a standard integer index
cluster_counts = cluster_counts.reset_index()

# Rename the columns to 'Cluster' and 'Count'
cluster_counts.columns = ['Cluster', 'Count']

# Define the file name
file_name = 'k.txt'

# Save the cluster counts to the text file
cluster_counts.to_csv(file_name, header=True, sep='\t', index=False)

print(f"Cluster counts saved to {file_name}")
print("Model Done")