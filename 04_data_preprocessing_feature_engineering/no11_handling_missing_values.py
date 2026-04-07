#Handling Missing Values 
#1. Imputation 2. Dropping
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("Placement_Dataset.csv")
print(dataset.head())
print("Shape of the data:",dataset.shape)
print("No of null values in each column:")
print(dataset.isnull().sum())

#Imputations:Central Tendencies - Mean, Median, Mode
#analyse distrubition of data in the salary(has missing values)
fig, ax = plt.subplots(figsize=(8,8))
sns.histplot(dataset.salary, kde=True, ax=ax)
plt.show()
#Cannot use mean when outliers - not ideal, use median, mode

#Replace with median values
dataset['salary'].fillna(dataset['salary'].median(),inplace=True)
print("No of null values in each row:")
print(dataset.isnull().sum())
print("Salary Values:")
print(dataset['salary'].head())
#Filling with mean/mode value- change median to mean/mode

#Dropping 
salary_dataset = pd.read_csv("Placement_Dataset.csv")
print("Initial shape:",salary_dataset.shape)
salary_dataset = salary_dataset.dropna(how = 'any')
print("No of null values in each column after modifying:")
print(salary_dataset.isnull().sum())
print("Final shape:",salary_dataset.shape)