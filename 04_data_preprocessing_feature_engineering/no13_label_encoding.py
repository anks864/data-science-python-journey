#Label Encoding - converting the labels into numeric form

import pandas as pd
from sklearn.preprocessing import LabelEncoder
'''#CANCER DATA
cancer_data = pd.read_csv("breast_cancer_data.csv")
print("First five Rows:")
print(cancer_data.head())

#finding the count of different labels
print("Data Diagnosis:")
print(cancer_data['diagnosis'].value_counts())

#load the label encoder function
label_encode = LabelEncoder()
labels = label_encode.fit_transform(cancer_data.diagnosis)

#appending the labels to the dataframe
cancer_data['target'] = labels
#0 - Benign; 1 - Malignant ( alphabetical order)
print("New First Five Rows:")
print(cancer_data.head())
print(cancer_data['target'].value_counts())
'''
#IRIS DATA
iris_data = pd.read_csv("iris_data.csv")
print("First five Rows:")
print(iris_data.head())

print("Data counts of Species column:")
print(iris_data['Species'].value_counts())
label_encode_iris = LabelEncoder()
iris_labels = label_encode_iris.fit_transform(iris_data.Species)
iris_data['target'] = iris_labels
print("New First Five Rows:")
print(iris_data.head())
print(iris_data['target'].value_counts())