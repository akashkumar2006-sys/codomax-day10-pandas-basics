# ==========================================
# Codomax AI/ML Internship - Day 10
# Topic: Pandas Basics
# Author: Akash Kumar Jha
# ==========================================

import pandas as pd

print("=" * 60)
print("          PANDAS BASICS - DAY 10")
print("=" * 60)

# Read CSV
df = pd.read_csv("students.csv")

print("\nComplete Dataset\n")
print(df)

print("\nDataset Information\n")
print(df.info())

print("\nFirst 3 Records\n")
print(df.head(3))

print("\nLast 2 Records\n")
print(df.tail(2))

print("\nStudents with Marks greater than 90\n")
print(df[df["Marks"] > 90])

print("\nAverage Marks")
print(df["Marks"].mean())

print("\nHighest Marks")
print(df["Marks"].max())

print("\nLowest Marks")
print(df["Marks"].min())

print("\nProgram Executed Successfully ✅")
print("=" * 60)
