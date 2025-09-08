# Libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as linearr

# 1. Dataset
study_hours = np.random.uniform(0,15,60)
age = np.random.randint(18,31,60)
base_note = 40
study_effect = 5
noise = np.random.normal(0,8,60)
exam_note = base_note + study_effect * study_hours + noise
exam_note = np.clip(exam_note,0,100)

df  = pd.DataFrame({
    'Study_hours': study_hours,
    'Exam_note': exam_note,
    'Age': age
}
)

# 2. Correlation Study_hours vs Exam_note
print(f"Correlation matrix: {df['Study_hours'].corr(df['Exam_note'])}")

# 3. Simple linear regression Exam_note ~ Study_hours
X = df[['Study_hours']]
y = df['Exam_note']
simple_model = linearr().fit(X,y)

print(f"Simple Regression:\n Intercept: {simple_model.intercept_}\n Coeficient: {simple_model.coef_[0]}\n")

# 4 multiple linear regresion Exam_note ~ Study_hours + Age
X_m = df[['Study_hours','Age']]
multiple_model = linearr().fit(X_m,y) # y is the same as simple model
print(f"Multiple Regression:\n Intercept: {multiple_model.intercept_}\n Coeficient: {multiple_model.coef_}")

"""
Study hours have a big influence in the exam note.
"""

