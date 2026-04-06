#Seaborn - Data Visualization Library
#Seaborn has some built in data sets 
#Importing libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#total bill vs tips dataset
tips = sns.load_dataset('tips')
print("shape of Tips dataset:",tips.shape)
print(tips.head())
#visualize the data
sns.set_theme() #set theme
sns.relplot(data = tips,#data to be read
            x = 'total_bill', #x-axis
            y = 'tip', #y-axis
            col = 'time', #different columns for data
            hue = 'smoker', #color of plot
            style = 'smoker', #shape of plot points
            size = 'size') #size of the plot points
plt.show()#to show the plot

#iris flower dataset
iris = sns.load_dataset('iris')
print("shape of Iris dataset:",iris.shape)
print(iris.head())
#Scatter Plot
sns.scatterplot(x = 'sepal_length', y = 'petal_length', hue = 'species',style = 'species', data = iris)
plt.show() #hue sets color changes

#Titanic ship dataset
titanic = sns.load_dataset('titanic')
print("shape of Titanic dataset:",titanic.shape)
print(titanic.head())
#Count Plot
sns.countplot(x = 'survived', hue = 'sex', data = titanic)#no style as countplot
plt.show()#no y axis, as the values of one column are its x axis data
#Bar Plot
sns.barplot(x = 'class', y = 'survived', hue = 'sex', data = titanic)
plt.show()

#house price dataset
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep=r"\s+", skiprows=22, header=None)
#Combine the odd rows with all columns and even rows with only the first two columns
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
# The target variable (last column of the dataset)
boston_target = raw_df.values[1::2, 2]
# Create a DataFrame for the features
house = pd.DataFrame(data, columns=[
    "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"])
house['PRICE'] = boston_target
print("shape of Boston dataset:",house.shape)
print(house.head())

#Distribution Plot
sns.displot(house['PRICE'])
plt.show()

#Correlation - Positive & Negative
correlation = house.corr()
print("Correlation: ")
print(correlation)
#Heat Map
plt.figure(figsize = (10,100))
sns.heatmap(correlation, cbar= True, square=True, fmt = '.1f', annot = True,
            annot_kws = {'size':8}, cmap='Blues')
plt.show()