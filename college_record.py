import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Create a sample dataset (if you don't have a CSV file)
data = {
    'StudentID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'M'],
    'Major': ['CS', 'Math', 'Physics', 'CS', 'Math', 'Physics', 'CS', 'Math'],
    'Exam1': [85, 90, 78, 92, 88, 75, 95, 80],
    'Exam2': [88, 85, 80, 90, 92, 70, 98, 82],
    'Attendance_%': [90, 95, 85, 98, 80, 70, 99, 88]
}
df = pd.DataFrame(data)

# If you have a CSV file named 'student_records.csv', you can load it instead:
# df = pd.read_csv('student_records.csv')

print("--- 1. Initial Data Overview ---")
print(df.head()) # Display the first 5 rows
print("\nData Types:")
print(df.dtypes) # Check data types
print("\nMissing Values:")
print(df.isnull().sum()) # Check for missing values

# 2. Data Cleaning (Example: handle missing attendance by filling with mean)
# In this specific sample, there are no missing values, but this is how you would
# handle them if they existed:
# df['Attendance_%'].fillna(df['Attendance_%'].mean(), inplace=True)

# 3. Data Analysis - Descriptive Statistics
print("\n--- 2. Descriptive Statistics ---")
print(df[['Exam1', 'Exam2', 'Attendance_%']].describe()) # Summary statistics for numerical columns

# Calculate total marks and average exam score
df['TotalMarks'] = df['Exam1'] + df['Exam2']
df['AverageScore'] = df[['Exam1', 'Exam2']].mean(axis=1)
print("\nDataFrame with new calculated columns:")
print(df[['Name', 'TotalMarks', 'AverageScore']].head())

# 4. Grouped Analysis
# print("\n--- 3. Grouped Analysis (by Major) ---")
# major_group = df.groupby('Major').agg(
#     Average_Exam1=('Exam1', 'mean'),
#     Count=('StudentID', 'size'),
#     Median_Attendance=('Attendance_%', 'median':
# )
# print(major_group)

# // ...existing code...
print("\n--- 3. Grouped Analysis (by Major) ---")
major_group = df.groupby('Major').agg(
    Average_Exam1=('Exam1', 'mean'),
    Count=('StudentID', 'size'),
    Median_Attendance=('Attendance_%', 'median')
)
print(major_group)
# ...existing code...

print("\n--- 4. Data Visualization ---")

# Plot a histogram of average scores
plt.figure(figsize=(8, 5))
plt.hist(df['AverageScore'], bins=5, color='green', edgecolor='black')
plt.title('Distribution of Student Average Scores')
plt.xlabel('Average Score')
plt.ylabel('Number of Students')
plt.grid(axis='y', alpha=0.7)
plt.show()

# Plot average score by major
major_group['Average_Exam1'].plot(kind='bar', color='skyblue')
plt.title('Average Exam 1 Score by Major')
plt.ylabel('Average Score')
plt.xlabel('Major')
plt.xticks(rotation=0)
plt.show()
