import pandas as pd

# --- Step 1: Load the data using the correct relative path ---
coverage_df = pd.read_excel("../data-set/coverage-data.xlsx")
incidence_df = pd.read_excel("../data-set/incidence-rate-data.xlsx")
reported_df = pd.read_excel("../data-set/reported-cases-data.xlsx")
vaccine_intro_df = pd.read_excel("../data-set/vaccine-introduction-data.xlsx")
vaccine_schedule_df = pd.read_excel("../data-set/vaccine-schedule-data.xlsx")

# --- Step 2: Drop rows with missing YEAR in Coverage Data ---
coverage_df = coverage_df.dropna(subset=['YEAR'])

# --- Step 3: Convert YEAR to integer for Coverage Data ---
coverage_df['YEAR'] = coverage_df['YEAR'].astype(int)

# --- Step 4: Remove rows where COVERAGE is missing ---
coverage_df_clean = coverage_df.dropna(subset=['COVERAGE'])

# --- Step 5: Cap the COVERAGE values at 100 ---
coverage_df_clean.loc[coverage_df_clean['COVERAGE'] > 100, 'COVERAGE'] = 100

# --- Step 6: Print some results to check our cleaning ---
print("Cleaned Coverage Data Shape:", coverage_df_clean.shape)
print("Cleaned Coverage Data - Descriptive Stats:")
print(coverage_df_clean['COVERAGE'].describe())
print("First 5 rows of Cleaned Coverage Data:")
print(coverage_df_clean.head())
