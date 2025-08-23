# Libraries
import numpy as np
import pandas as pd
import random

# List of numbers between 100 and 500
listNumbers = [random.uniform(50,500) for _ in range(20)]
# adding manually outliers
listNumbers.append(2000)
listNumbers.append(3000)

# order list
listNumbers.sort() 

# storage in a dataframe
df = pd.DataFrame(listNumbers, columns=['Numbers'])
print(df)

# IQR method
q1 = df['Numbers'].quantile(0.25)
q3 = df['Numbers'].quantile(0.75)
IQR = q3-q1

bot_limit = q1 - 1.5*IQR
top_limit = q3 + 1.5*IQR

outliers_IQR = df[(df['Numbers'] < bot_limit) | (df['Numbers'] > top_limit)]

# Standar deviation method
mean = df['Numbers'].mean()
std_dev = df['Numbers'].std()

outliers_std_dev = df[(df['Numbers'] < mean - 3 *std_dev) | (df['Numbers'] > mean + 3*std_dev)]

print(
    f"Outliers with IQR method:\n {outliers_IQR}\n",
    f"Outliers with standar deviation method:\n {outliers_std_dev}\n"
)