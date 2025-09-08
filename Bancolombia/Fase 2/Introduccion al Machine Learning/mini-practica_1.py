import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


# Dataset
np.random.seed(42)

study_hours = np.random.randint(0,15,50)
note = 5*study_hours + np.random.normal(0,5,50)

df = pd.DataFrame({"Study_Hours":study_hours, "Note":note})

# Split dataset in train and test 70% - 30%
X = df[['Study_Hours']]
y = df['Note']
X_train, X_test, y_train,  y_test = train_test_split(X,y,test_size=0.3,random_state=42)


# Train model
model = LinearRegression().fit(X_train,y_train)

# predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Errors
error_train = mean_squared_error(y_train, y_pred_train)
error_test = mean_squared_error(y_test, y_pred_test)    

print(f"Train error: {error_train:.4f}\n Test error: {error_test:.04f}\n")

# Plot the results
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_train, y_train, alpha=0.7, label='Train data')
plt.scatter(X_test, y_test, alpha=0.7, label='Test data', color='red')
plt.plot(X_train, y_pred_train, color='blue', label='Regression line')
plt.xlabel('Study Hours')
plt.ylabel('Note')
plt.legend()
plt.title('Linear Regression Fit')

plt.subplot(1, 2, 2)
plt.scatter(y_test, y_pred_test, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Notes')
plt.ylabel('Predicted Notes')
plt.title('Actual vs Predicted')

plt.tight_layout()
plt.show()

"""
the performance is good, test error < Train error, the model is not overfitting and has learned the true underlying pattern
the model generalizes good, because the variance noise was 25, so the errors are arround 15-24, wich is to close to the theorical minimum of 25
   
"""