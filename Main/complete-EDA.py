import pandas as pd
import matplotlib.pyplot as plt

# =======================
# EDA for Coverage Data
# =======================
coverage_df = pd.read_excel("../data-set/coverage-data.xlsx")

# Clean Coverage Data: drop rows with missing YEAR or COVERAGE, convert YEAR to int, cap COVERAGE at 100
coverage_df = coverage_df.dropna(subset=['YEAR', 'COVERAGE'])
coverage_df['YEAR'] = coverage_df['YEAR'].astype(int)
coverage_df_clean = coverage_df.copy()
coverage_df_clean.loc[coverage_df_clean['COVERAGE'] > 100, 'COVERAGE'] = 100

# Group by YEAR and calculate average COVERAGE
avg_coverage_by_year = coverage_df_clean.groupby('YEAR')['COVERAGE'].mean()
print("Average Vaccination Coverage by Year:")
print(avg_coverage_by_year)

# Plot line chart for average coverage over time
plt.figure(figsize=(10, 6))
avg_coverage_by_year.plot(kind='line', marker='o')
plt.title("Average Vaccination Coverage by Year")
plt.xlabel("Year")
plt.ylabel("Average Coverage (%)")
plt.grid(True)
plt.savefig("coverage_avg_by_year.png")  # Save the plot as an image
plt.show()

# Plot histogram for coverage distribution
plt.figure(figsize=(8, 6))
coverage_df_clean['COVERAGE'].plot(kind='hist', bins=30)
plt.title("Distribution of Vaccination Coverage")
plt.xlabel("Coverage (%)")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("coverage_histogram.png")
plt.show()

# =======================
# EDA for Incidence Data
# =======================
incidence_df = pd.read_excel("../data-set/incidence-rate-data.xlsx")

# Clean Incidence Data: drop rows with missing YEAR or INCIDENCE_RATE, convert YEAR to int
incidence_df = incidence_df.dropna(subset=['YEAR', 'INCIDENCE_RATE'])
incidence_df['YEAR'] = incidence_df['YEAR'].astype(int)

# Group by YEAR and calculate average INCIDENCE_RATE
avg_incidence_by_year = incidence_df.groupby('YEAR')['INCIDENCE_RATE'].mean()
print("Average Incidence Rate by Year:")
print(avg_incidence_by_year)

# Plot line chart for average incidence rate over time
plt.figure(figsize=(10, 6))
avg_incidence_by_year.plot(kind='line', marker='o', color='orange')
plt.title("Average Incidence Rate by Year")
plt.xlabel("Year")
plt.ylabel("Average Incidence Rate")
plt.grid(True)
plt.savefig("incidence_avg_by_year.png")
plt.show()

# Plot histogram for incidence rate distribution
plt.figure(figsize=(8, 6))
incidence_df['INCIDENCE_RATE'].plot(kind='hist', bins=30, color='orange')
plt.title("Distribution of Incidence Rate")
plt.xlabel("Incidence Rate")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("incidence_histogram.png")
plt.show()

# =======================
# EDA for Reported Cases Data
# =======================
reported_df = pd.read_excel("../data-set/reported-cases-data.xlsx")

# Clean Reported Cases Data: drop rows with missing YEAR or CASES, convert YEAR to int
reported_df = reported_df.dropna(subset=['YEAR', 'CASES'])
reported_df['YEAR'] = reported_df['YEAR'].astype(int)

# Group by YEAR and calculate average CASES
avg_reported_by_year = reported_df.groupby('YEAR')['CASES'].mean()
print("Average Reported Cases by Year:")
print(avg_reported_by_year)

# Plot line chart for average reported cases over time
plt.figure(figsize=(10, 6))
avg_reported_by_year.plot(kind='line', marker='o', color='green')
plt.title("Average Reported Cases by Year")
plt.xlabel("Year")
plt.ylabel("Average Reported Cases")
plt.grid(True)
plt.savefig("reported_avg_by_year.png")
plt.show()

# Plot histogram for reported cases distribution
plt.figure(figsize=(8, 6))
reported_df['CASES'].plot(kind='hist', bins=30, color='green')
plt.title("Distribution of Reported Cases")
plt.xlabel("Reported Cases")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("reported_histogram.png")
plt.show()

# =======================
# EDA for Vaccine Introduction Data
# =======================
vaccine_intro_df = pd.read_excel("../data-set/vaccine-introduction-data.xlsx")

# Clean Vaccine Introduction Data: drop rows with missing YEAR, convert YEAR to int
vaccine_intro_df = vaccine_intro_df.dropna(subset=['YEAR'])
vaccine_intro_df['YEAR'] = vaccine_intro_df['YEAR'].astype(int)

# Count the number of vaccine introductions per year where INTRO equals "Yes"
# (Assuming "Yes" indicates the vaccine was introduced)
vaccine_intro_df_yes = vaccine_intro_df[vaccine_intro_df['INTRO'].str.upper() == "YES"]
count_introductions_by_year = vaccine_intro_df_yes.groupby('YEAR').size()
print("Count of Vaccine Introductions (Yes) by Year:")
print(count_introductions_by_year)

# Plot bar chart for the count of vaccine introductions by year
plt.figure(figsize=(10, 6))
count_introductions_by_year.plot(kind='bar', color='purple')
plt.title("Count of Vaccine Introductions (Yes) by Year")
plt.xlabel("Year")
plt.ylabel("Number of Introductions")
plt.grid(True)
plt.savefig("vaccine_intro_count_by_year.png")
plt.show()

# =======================
# EDA for Vaccine Schedule Data
# =======================
vaccine_schedule_df = pd.read_excel("../data-set/vaccine-schedule-data.xlsx")

# Clean Vaccine Schedule Data: drop rows with missing YEAR, convert YEAR to int
vaccine_schedule_df = vaccine_schedule_df.dropna(subset=['YEAR'])
vaccine_schedule_df['YEAR'] = vaccine_schedule_df['YEAR'].astype(int)

# Plot histogram for SCHEDULEROUNDS distribution
plt.figure(figsize=(8, 6))
# Determine the range for schedule rounds based on the max value
max_round = int(vaccine_schedule_df['SCHEDULEROUNDS'].max())
bins = range(1, max_round + 2)  # create bins for each round
vaccine_schedule_df['SCHEDULEROUNDS'].plot(kind='hist', bins=bins, color='brown', align='left')
plt.title("Distribution of Schedule Rounds")
plt.xlabel("Schedule Round")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("vaccine_schedule_rounds_histogram.png")
plt.show()
