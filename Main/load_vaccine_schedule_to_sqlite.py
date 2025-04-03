import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///../VaccinationDB.db")

# Load vaccine schedule data
vaccine_schedule_df = pd.read_excel("../data-set/vaccine-schedule-data.xlsx")

# Clean the data: drop rows with missing YEAR
vaccine_schedule_df = vaccine_schedule_df.dropna(subset=['YEAR'])
vaccine_schedule_df['YEAR'] = vaccine_schedule_df['YEAR'].astype(int)

# Write the DataFrame to a table named "VaccineScheduleData"
vaccine_schedule_df.to_sql('VaccineScheduleData', con=engine, if_exists='append', index=False)

print("Vaccine Schedule Data loaded into SQLite successfully!")
