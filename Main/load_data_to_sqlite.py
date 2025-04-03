import pandas as pd
from sqlalchemy import create_engine

# Create an engine to connect to the SQLite database.
engine = create_engine("sqlite:///../VaccinationDB.db")

# Load the cleaned Coverage Data from the Excel file.
coverage_df = pd.read_excel("../data-set/coverage-data.xlsx")

# Rename the column "GROUP" to "group_name" to match the SQL table schema.
coverage_df.rename(columns={"GROUP": "group_name"}, inplace=True)

# Clean the data:
# Drop rows with missing YEAR or COVERAGE values.
coverage_df = coverage_df.dropna(subset=['YEAR', 'COVERAGE'])
# Convert the YEAR column to integer.
coverage_df['YEAR'] = coverage_df['YEAR'].astype(int)
# Cap any COVERAGE values over 100 to 100.
coverage_df.loc[coverage_df['COVERAGE'] > 100, 'COVERAGE'] = 100

# Load the cleaned data into the CoverageData table in the SQLite database.
coverage_df.to_sql('CoverageData', con=engine, if_exists='append', index=False)

print("Coverage Data loaded into SQLite successfully!")
