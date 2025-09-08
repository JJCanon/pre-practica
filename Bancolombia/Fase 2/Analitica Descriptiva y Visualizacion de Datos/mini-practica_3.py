# Libraries
import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt

# Creating data
data = {
    "Income":[random.uniform(1000,10000) for _ in range(20)],
    "Age":[random.uniform(20,60) for _ in range(20)]
}

# storing dataframe
df = pd.DataFrame(data)
print(df)

# Graphs
plt.figure(figsize=(12,4))

## Histogram
plt.subplot(1,3,1)
plt.hist(df['Income'],bins=6,edgecolor="black")
plt.title("Income Histogram")
plt.xlabel("Income ($)")
plt.ylabel("Frequency")

## Boxplot
plt.subplot(1,3,2)
sns.boxplot(y=df['Income'])
plt.title("Income Boxplot")

## Scatterplot
plt.subplot(1,3,3)
plt.scatter(df['Age'],df['Income'],c="blue")
plt.title("scatterplot: Age vs Income")
plt.xlabel("Age")
plt.ylabel("Income ($)")

## Show graphs
plt.tight_layout()
plt.show()
