
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create marks array for 4 students and 3 subjects
marks = np.array([
    [80, 75, 90],
    [65, 70, 85],
    [90, 88, 95],
    [55, 60, 70]
])

# Print array shape
print("Marks:")
print(marks)
print("Shape:", marks.shape)

# Calculate student averages
student_avg = np.mean(marks, axis=1)
print("Student averages:", student_avg)

# Calculate subject averages
subject_avg = np.mean(marks, axis=0)
print("Subject averages:", subject_avg)

# Add 5 grace marks using broadcasting
grace_marks = marks + 5
print("Marks after grace marks:")
print(grace_marks)

# Calculate weighted scores
weights = np.array([0.4, 0.3, 0.3])
weighted_scores = np.dot(marks, weights)

print("Weighted scores:", weighted_scores)


# Load employee data using Pandas
df = pd.read_csv("employees_task3.csv")

# Display employee data
print("\nEmployee Data:")
print(df)

# Display dataframe information
print("\nData Information:")
df.info()

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Select rows using loc
print("\nUsing loc:")
print(df.loc[0:2, ["name", "department", "salary"]])

# Select rows using iloc
print("\nUsing iloc:")
print(df.iloc[0:3, 0:4])

# Filter employees with salary above 50000
print("\nEmployees with salary above 50000:")
print(df[df["salary"] > 50000])


# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Fill missing salaries with median
median_salary = df["salary"].median()
df["salary"] = df["salary"].fillna(median_salary)

print("\nAfter filling missing salaries:")
print(df["salary"])

# Remove duplicate rows
df = df.drop_duplicates()

# Correct data types
df["id"] = df["id"].astype(int)
df["salary"] = df["salary"].astype(int)

# Display cleaned data
print("\nCleaned Employee Data:")
print(df)

print("\nTotal employees after cleaning:", len(df))
print("Missing salaries after cleaning:", df["salary"].isnull().sum())


# Group employees by department
department_summary = df.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
)

print("\nDepartment Summary:")
print(department_summary)



# Load department details
departments = pd.read_csv("departments.csv")

# Inner join
inner_join = pd.merge(df, departments, on="department", how="inner")

print("\nInner Join:")
print(inner_join)

# Left join
left_join = pd.merge(df, departments, on="department", how="left")

print("\nLeft Join:")
print(left_join)

# Outer join
outer_join = pd.merge(df, departments, on="department", how="outer")

print("\nOuter Join:")
print(outer_join)

# Find departments without employees
empty_departments = outer_join[outer_join["id"].isna()]

print("\nDepartments with no employees:")
print(empty_departments[["department", "head", "budget"]])


# Create charts folder
import os

os.makedirs("charts", exist_ok=True)

# 1. Bar Chart - Department headcount
department_count = df["department"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(department_count.index, department_count.values, color="skyblue", label="Employees")
plt.title("Employees in Each Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.legend()
plt.savefig("charts/bar_chart.png")
plt.close()

print("\nInsight: IT department has the highest number of employees.")

# 2. Histogram - Salary distribution
plt.figure(figsize=(8, 5))
plt.hist(df["salary"], bins=5, color="orange", edgecolor="black", label="Salary")
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("charts/histogram.png")
plt.close()

print("Insight: Most employee salaries are distributed between 30000 and 75000.")

# 3. Scatter Plot - Salary vs Employee ID
plt.figure(figsize=(8, 5))
plt.scatter(df["id"], df["salary"], color="green", label="Employees")
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.savefig("charts/scatter_plot.png")
plt.close()

print("Insight: Employee salaries vary across different employee IDs.")

# 4. Line Chart - Salary by employee
plt.figure(figsize=(8, 5))
plt.plot(df["name"], df["salary"], marker="o", color="red", label="Salary")
plt.title("Employee Salary Comparison")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("charts/line_chart.png")
plt.close()

print("Insight: Karthik has the highest salary among the employees.")
print("\nAll four charts saved successfully!")

