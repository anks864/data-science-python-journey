#Data Standardization
#The process of standardizing the data to a common format and range
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#importing csv file dataset
dataset  = sklearn.datasets.load_breast_cancer()
#print(dataset)
#load data into dataframe
df = pd.DataFrame(data = dataset.data, columns = dataset.feature_names)
print("First five rows in the dataset:")
print(df.head())
print("Shape:",df.shape)
X = df
Y = dataset.target
#print(X)
#print(Y)

#Splitting data into training and test data
X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)
print("X.shape =",X.shape,"X_train.shape =",X_train.shape,"X_test.shape = ",X_test.shape)
print("Std Dev:",dataset.data.std())
scaler = StandardScaler()
scaler.fit(X_train)
X_train_std = scaler.transform(X_train)
print("Std Dev after standardization:",X_train_std.std())
X_test_std = scaler.transform(X_test)