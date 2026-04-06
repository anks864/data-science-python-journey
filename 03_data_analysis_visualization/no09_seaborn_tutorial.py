# ==============================
# File: no09_seaborn_tutorial.py
# Topic: Seaborn - Data Visualization
# Description: Covers Seaborn datasets and various plots
# ==============================


# ==============================
# Importing Libraries
# ==============================
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ==============================
# Dataset 1: Tips Dataset
# ==============================
tips = sns.load_dataset('tips')

print("Shape of Tips dataset:", tips.shape)
print(tips.head())

# Visualization: Relational Plot
sns.set_theme()

sns.relplot(
    data=tips,
    x='total_bill',
    y='tip',
    col='time',
    hue='smoker',
    style='smoker',
    size='size'
)

plt.show()


# ==============================
# Dataset 2: Iris Dataset
# ==============================
iris = sns.load_dataset('iris')

print("Shape of Iris dataset:", iris.shape)
print(iris.head())

# Visualization: Scatter Plot
sns.scatterplot(
    x='sepal_length',
    y='petal_length',
    hue='species',
    style='species',
    data=iris
)

plt.show()


# ==============================
# Dataset 3: Titanic Dataset
# ==============================
titanic = sns.load_dataset('titanic')

print("Shape of Titanic dataset:", titanic.shape)
print(titanic.head())

# Visualization: Count Plot
sns.countplot(
    x='survived',
    hue='sex',
    data=titanic
)

plt.show()

# Visualization: Bar Plot
sns.barplot(
    x='class',
    y='survived',
    hue='sex',
    data=titanic
)

plt.show()


# ==============================
# Dataset 4: Boston Housing Dataset
# ==============================
data_url = "http://lib.stat.cmu.edu/datasets/boston"

raw_df = pd.read_csv(
    data_url,
    sep=r"\s+",
    skiprows=22,
    header=None
)

# Combine rows to form dataset
data = np.hstack([
    raw_df.values[::2, :],
    raw_df.values[1::2, :2]
])

# Target variable
boston_target = raw_df.values[1::2, 2]

# Create DataFrame
house = pd.DataFrame(
    data,
    columns=[
        "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM",
        "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"
    ]
)

house['PRICE'] = boston_target

print("Shape of Boston dataset:", house.shape)
print(house.head())


# ==============================
# Visualization: Distribution Plot
# ==============================
sns.displot(house['PRICE'])
plt.show()


# ==============================
# Correlation Analysis
# ==============================
correlation = house.corr()

print("Correlation Matrix:")
print(correlation)


# ==============================
# Visualization: Heatmap
# ==============================
plt.figure(figsize=(10, 10))

sns.heatmap(
    correlation,
    cbar=True,
    square=True,
    fmt='.1f',
    annot=True,
    annot_kws={'size': 8},
    cmap='Blues'
)

plt.show()


# ==============================
# EOF: Feel free to open an issue to report a bug or discrepancy
# ==============================
