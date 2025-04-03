import pandas as pd
from sqlalchemy import create_engine

# Create an engine to connect to your SQLite database.
# The relative path "sqlite:///../VaccinationDB.db" assumes VaccinationDB.db is one level up from Main.
engine = create_engine("sqlite:///../VaccinationDB.db")

# Export CoverageData table to a DataFrame
coverage_df = pd.read_sql("SELECT * FROM CoverageData", con=engine)

# Save the DataFrame as a CSV file in the "data-set" folder (adjust the path if needed)
coverage_df.to_csv("../data-set/CoverageData.csv", index=False)

print("CoverageData exported to CSV successfully!")

# ----- Repeat similar steps for other tables -----
# For IncidenceData table:
try:
    incidence_df = pd.read_sql("SELECT * FROM IncidenceData", con=engine)
    incidence_df.to_csv("../data-set/IncidenceData.csv", index=False)
    print("IncidenceData exported to CSV successfully!")
except Exception as e:
    print("Could not export IncidenceData:", e)

# For ReportedCasesData table:
try:
    reported_df = pd.read_sql("SELECT * FROM ReportedCasesData", con=engine)
    reported_df.to_csv("../data-set/ReportedCasesData.csv", index=False)
    print("ReportedCasesData exported to CSV successfully!")
except Exception as e:
    print("Could not export ReportedCasesData:", e)

# For VaccineIntroData table:
try:
    vaccine_intro_df = pd.read_sql("SELECT * FROM VaccineIntroData", con=engine)
    vaccine_intro_df.to_csv("../data-set/VaccineIntroData.csv", index=False)
    print("VaccineIntroData exported to CSV successfully!")
except Exception as e:
    print("Could not export VaccineIntroData:", e)

# For VaccineScheduleData table:
try:
    vaccine_schedule_df = pd.read_sql("SELECT * FROM VaccineScheduleData", con=engine)
    vaccine_schedule_df.to_csv("../data-set/VaccineScheduleData.csv", index=False)
    print("VaccineScheduleData exported to CSV successfully!")
except Exception as e:
    print("Could not export VaccineScheduleData:", e)
