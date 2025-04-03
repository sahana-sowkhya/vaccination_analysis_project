import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///../VaccinationDB.db")

# Load the reported cases data
reported_df = pd.read_excel("../data-set/reported-cases-data.xlsx")

# Clean the data: drop rows with missing YEAR or CASES
reported_df = reported_df.dropna(subset=['YEAR', 'CASES'])
reported_df['YEAR'] = reported_df['YEAR'].astype(int)

# Write the DataFrame to a table named "ReportedCasesData"
reported_df.to_sql('ReportedCasesData', con=engine, if_exists='append', index=False)

print("Reported Cases Data loaded into SQLite successfully!")
