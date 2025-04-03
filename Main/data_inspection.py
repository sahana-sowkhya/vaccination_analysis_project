import pandas as pd

# Read the Excel files into DataFrames
coverage_df = pd.read_excel("../data-set/coverage-data.xlsx")
print("Coverage Data loaded with shape:", coverage_df.shape)

incidence_df = pd.read_excel("../data-set/incidence-rate-data.xlsx")
print("Incidence Data loaded with shape:", incidence_df.shape)

reported_df = pd.read_excel("../data-set/reported-cases-data.xlsx")
print("Reported Cases Data loaded with shape:", reported_df.shape)

vaccine_intro_df = pd.read_excel("../data-set/vaccine-introduction-data.xlsx")
print("Vaccine Introduction Data loaded with shape:", vaccine_intro_df.shape)

vaccine_schedule_df = pd.read_excel("../data-set/vaccine-schedule-data.xlsx")
print("Vaccine Schedule Data loaded with shape:", vaccine_schedule_df.shape)

# Print the first 5 rows of each DataFrame to see the data
print("----- First 5 rows of Coverage Data -----")
print(coverage_df.head())

print("----- First 5 rows of Incidence Data -----")
print(incidence_df.head())

print("----- First 5 rows of Reported Cases Data -----")
print(reported_df.head())

print("----- First 5 rows of Vaccine Introduction Data -----")
print(vaccine_intro_df.head())

print("----- First 5 rows of Vaccine Schedule Data -----")
print(vaccine_schedule_df.head())

# Get general information about the data

print("----- Coverage Data Info -----")
coverage_df.info()  # This prints the type of each column and the count of non-empty entries

print("----- Incidence Data Info -----")
incidence_df.info()

print("----- Reported Cases Data Info -----")
reported_df.info()

print("----- Vaccine Introduction Data Info -----")
vaccine_intro_df.info()

print("----- Vaccine Schedule Data Info -----")
vaccine_schedule_df.info()

# Check for missing values in each DataFrame
print("----- Missing Values in Coverage Data -----")
print(coverage_df.isnull().sum())

print("----- Missing Values in Incidence Data -----")
print(incidence_df.isnull().sum())

print("----- Missing Values in Reported Cases Data -----")
print(reported_df.isnull().sum())

print("----- Missing Values in Vaccine Introduction Data -----")
print(vaccine_intro_df.isnull().sum())

print("----- Missing Values in Vaccine Schedule Data -----")
print(vaccine_schedule_df.isnull().sum())

# Print descriptive statistics for numeric columns in Coverage Data
print("----- Descriptive Statistics for Coverage Data -----")
print(coverage_df.describe())


