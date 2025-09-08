# Libraries
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import f_oneway, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
## set random seed for reproducibility
np.random.seed(42)

## Creating data
n=50
group_A_scores = np.random.normal(70,10,n)
group_B_scores = np.random.normal(75,12,n)
group_C_scores = np.random.normal(80,8,n)

## Creating DataFrame
df = pd.DataFrame({
    "Group":['A']*n + ['B']*n + ['C']*n,
    "Score": np.concatenate([group_A_scores,group_B_scores,group_C_scores])
    })

# ANOVA Analysis
## H0: there are significant differences between group means
## H1: there are no significant differences between group means
group_a_mean = group_A_scores.mean()
group_a_std = group_A_scores.std()
group_b_mean = group_B_scores.mean()
group_b_std = group_B_scores.std()
group_c_mean = group_C_scores.mean()
group_c_std = group_C_scores.std()
print(f"ANOVA Analisys\n",
      f"Group A: mean = {group_a_mean}, std = {group_a_std}\n",
      f"Group B: mean = {group_b_mean}, std = {group_b_std}\n",
      f"Group C: mean = {group_c_mean}, std = {group_c_std}\n"
      )

# Perform ANOVA
f_stat, p_value = f_oneway(group_A_scores,group_B_scores,group_C_scores)
print(f"ANOVA Results:\n",
      f"F-statistic: {f_stat:.4f}\n",
      f"P-value: {p_value}\n"
      )
if p_value < 0.05:
    print("Reject null hypothesis: There are significant differences between group means.\n")
else:
    print("Fail to reject null hypothesis: No significant differences between group means.\n")

# Chi-Square test
# Creating a categorical variable for preference (X o Y)
np.random.seed(42)
preferences = []
for group in df['Group']:
        preferences.append('X' if np.random.random() < 0.5 else 'Y')
df['Preferences'] = preferences

# Creatinf contingency table
congintency_table = pd.crosstab(df['Group'],df['Preferences'])
print(f"Congintency table:\n {congintency_table}\n")

# perform chi-square test
chi2, p_chi, dof, expected = chi2_contingency(congintency_table)
print(
    f"Chi-square Test Results:\n",
    f"Chi-square statistic: {chi2:.4f}\n P-value: {p_chi}\n Degrees od freedom: {dof}\n Expected freciencies:\n {expected}"
)

if p_chi < 0.05:
    print("Reject null hypothesis: There is a significant association between group and preference.\n")
else:
    print("Fail to reject null hypothesis: No significant association between group and preference.\n")
