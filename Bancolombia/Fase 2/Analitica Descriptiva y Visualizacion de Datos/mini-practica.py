# libraries
import numpy as np
import pandas as pd
import random

# List of numbers between 50 and 500
listNumbers = [random.uniform(50,500) for _ in range(15)]
# storage in a dataframe
df = pd.DataFrame(listNumbers, columns=['Numbers'])

# Descriptive analytic
## middle trend measures-> mean, median, mode.
mean = df['Numbers'].mean()
median = df['Numbers'].median()
mode = df['Numbers'].mode()[0]

## dispersion measures -> variance, standar deviation, coefficient of variation, Q1, Q3.
variance = df['Numbers'].var()
standar_desviation = df['Numbers'].std()
coefficient_of_variation = standar_desviation / mean
q1 = df['Numbers'].quantile(0.25)
q2 = df['Numbers'].quantile(0.75)

print(f"Mean: {mean}\n",
      f"Median: {median}\n",
      f"Mode: {mode}\n",
      f"Variance: {variance}\n",
      f"Standar desviation: {standar_desviation}\n",
      f"Coefficient of variation: {coefficient_of_variation}\n",
      f"Q1: {q1}\n",
      f"Q2: {q2}\n"
      )