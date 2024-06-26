# -*- coding: utf-8 -*-
"""Clustering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1U_8VTF-j0sLY3Uo-s-gy1RUkuCy9_Zjh
"""

#Importing Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")

#importing datasets

df = pd.read_csv('/content/Mall_Customers.csv')
df.head()

#a visualization comparing spending score with two other factors (Age and Annual Income) for different genders.

fig, ax = plt.subplots(2, figsize=(10,10))
sns.scatterplot(ax=ax[0], data=df, x='Age', y='Spending Score (1-100)', hue='Gender')
sns.scatterplot(ax=ax[1], data=df, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Gender')
plt.show()

# determining the optimal number of clusters by elbow method

ssw = []
clusters = range(1,10)
for i in clusters:
    model = KMeans(n_clusters = i , init='k-means++' , n_init=100)
    model.fit(df[["Spending Score (1-100)" , "Annual Income (k$)"]])
    ssw.append(model.inertia_)
sns.lineplot(data=ssw)
sns.scatterplot(data=ssw)
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Sum of Squared Error')
plt.title('Elbow Plot')
# plt.show()
plt.plot(clusters , ssw)

# performs KMeans clustering on data and assigns cluster labels to each data point

model = KMeans(n_clusters = 5, init='k-means++',n_init=100)
y_predicted  = model.fit_predict(df[["Spending Score (1-100)" , "Annual Income (k$)"]])
y_predicted

model.cluster_centers_

#to add group column to the df
df["Group"] = y_predicted
df

df1=  df[df.Group == 0]
df2=  df[df.Group == 1]
df3=  df[df.Group == 2]
df4=  df[df.Group == 3]
df5=  df[df.Group == 4]
plt.scatter(df1["Spending Score (1-100)"] , df1["Annual Income (k$)"]  , color = "orange" , label = "1")
plt.scatter(df2["Spending Score (1-100)"] , df2["Annual Income (k$)"]  , color = "#228B22" , label = "2")
plt.scatter(df3["Spending Score (1-100)"] , df3["Annual Income (k$)"] , color = "#00BFFF" , label = "3")
plt.scatter(df4["Spending Score (1-100)"] , df4["Annual Income (k$)"], color = "indigo" , label = "4")
plt.scatter(df5["Spending Score (1-100)"] , df5["Annual Income (k$)"] , color = "red" , label = "5")
plt.scatter(model.cluster_centers_[: , 0] ,  model.cluster_centers_[: , 1] , color = "magenta" , marker = "*"  , label =  "Centroids")
plt.legend(loc='upper right'  , bbox_to_anchor=(1.20, 1.015))
plt.title("Clusters")
plt.xlabel("Spending Score")
plt.ylabel("Annual Income")
plt.show()