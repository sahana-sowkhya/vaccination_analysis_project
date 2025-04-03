import pandas as pd
from sqlalchemy import create_engine

# Connect to your SQLite database (adjust the path as needed)
engine = create_engine("sqlite:///../VaccinationDB.db")

# Load the incidence data from Excel
incidence_df = pd.read_excel("../data-set/incidence-rate-data.xlsx")

# Clean the data: drop rows with missing YEAR or INCIDENCE_RATE
incidence_df = incidence_df.dropna(subset=['YEAR', 'INCIDENCE_RATE'])
incidence_df['YEAR'] = incidence_df['YEAR'].astype(int)

# Write the cleaned DataFrame to a new table named "IncidenceData"
incidence_df.to_sql('IncidenceData', con=engine, if_exists='append', index=False)

print("Incidence Data loaded into SQLite successfully!")
