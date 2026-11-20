
# Employee Data Analysis

# Introduction
# This program is used to analyse employee data.
#
# Objectives:
# 1. Read employee details
# 2. Find total number of employees
# 3. Find department wise employee count
# 4. Calculate average salary
# 5. Find employees from Chennai
# 6. Display and save employee charts


# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os

# Read employee data
df = pd.read_csv(r"C:\Users\HP\Desktop\day6 week assesment\task4\data\employees.csv")

print("Employee Data:")
print(df.head())


# In[2]:

# Total number of employees
print("Total employees:", len(df))

# Department wise employee count
print("\nDepartment-wise employee count:")
print(df["department"].value_counts())

# Calculate average salary
print("\nAverage salary:")
print(df["salary"].mean())

# Employees from Chennai
print("\nEmployees from Chennai:")
print(df[df["city"] == "Chennai"])


# In[3]:

# Calculate average salary execution time

start = time.time()

average_salary = df["salary"].mean()

end = time.time()

print("\nAverage salary execution time:", end - start, "seconds")


# In[4]:

# Create reports folder if it does not exist
os.makedirs("reports", exist_ok=True)

# Display department wise employee chart
df["department"].value_counts().plot(kind="bar", color="skyblue")

plt.title("Department-wise Employee Count")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.tight_layout()

# Save department chart
plt.savefig("reports/department_chart.png")

plt.show()
plt.close()


# In[5]:

# Display salary distribution
df["salary"].plot(kind="hist", color="lightgreen", edgecolor="black")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.tight_layout()

# Save salary chart
plt.savefig("reports/salary_chart.png")

plt.show()
plt.close()


# In[6]:

# Final output
print("\nEmployee Data Analysis Completed")
print("Charts saved successfully in reports folder.")
