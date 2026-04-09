#Train Test Split
#numerical data pre processing
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#PIMA Diabetes Dataset
diabetes_dataset = pd.read_csv("diabetes.csv")
print("First five Rows:")
print(diabetes_dataset.head())
print("Shape of data:",diabetes_dataset.shape)
print("Statistical Measures:")
print(diabetes_dataset.describe())
print(diabetes_dataset['Outcome'].value_counts())
#0 -> Non-Diabetic; 1 -> Diabetic
print(diabetes_dataset.groupby('Outcome').mean())
#separating the data and labels
X = diabetes_dataset.drop(columns = 'Outcome', axis = 1)
Y = diabetes_dataset['Outcome']

#Standard Scaler - standarization of data
scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)
print("Standardized Data:")
print(standardized_data)
X = standardized_data

#Splitting the data into training and testing data
X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
print("X.shape =",X.shape,"X_train.shape =",X_train.shape,"X_test.shape = ",X_test.shape)