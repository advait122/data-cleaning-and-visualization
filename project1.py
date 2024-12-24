import pandas as pd
import matplotlib.pyplot as plt

#Data Cleaning

df = pd.read_csv(r"C:\Users\ADVAIT\Desktop\dataset.csv")
df= df.drop_duplicates()
df = df[df["Competitors"] != "-1"]
values_to_drop = [-1]
df = df[~df.isin(values_to_drop).any(axis=1)]
df['Salary Estimate'] = df['Salary Estimate'].str.replace('(Glassdoor est.)', '', regex=False)
print(df)

#Data Visualization

salary_counts = df['Salary Estimate'].value_counts()
plt.figure(figsize=(12, 6))
plt.bar(salary_counts.index, salary_counts.values, width=0.6, color='skyblue')
plt.title('Frequency of Salary Estimates', fontsize=16, fontweight='bold')
plt.xlabel('Salary Estimate', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.show()
