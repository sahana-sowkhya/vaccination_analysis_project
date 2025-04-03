import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///../VaccinationDB.db")

# Load vaccine introduction data
vaccine_intro_df = pd.read_excel("../data-set/vaccine-introduction-data.xlsx")

# Clean the data: drop rows with missing YEAR
vaccine_intro_df = vaccine_intro_df.dropna(subset=['YEAR'])
vaccine_intro_df['YEAR'] = vaccine_intro_df['YEAR'].astype(int)

# Write the DataFrame to a table named "VaccineIntroData"
vaccine_intro_df.to_sql('VaccineIntroData', con=engine, if_exists='append', index=False)

print("Vaccine Introduction Data loaded into SQLite successfully!")
