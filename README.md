# Vaccination Data Analysis and Visualization

## Overview

This project analyzes global vaccination data to understand trends in vaccination coverage, disease incidence, and vaccine effectiveness. The data is cleaned using Python, stored in a structured SQLite database, and visualized with interactive dashboards in Power BI. The insights derived from this analysis are intended to inform public health strategies, resource allocation, and vaccination policy recommendations.

## Problem Statement

Analyze global vaccination data to understand:
- Trends in vaccination coverage
- Disease incidence and its correlation with vaccination rates
- Effectiveness of vaccination programs

The cleaned data is stored in a SQL database and visualized via Power BI dashboards to provide actionable insights for public health policy, resource allocation, and disease prevention strategies.

## Business Use Cases

- **Public Health Strategy:**  
  Assess the effectiveness of vaccination programs in different regions and prioritize areas with low coverage.

- **Disease Prevention:**  
  Identify diseases with high incidence rates despite vaccination efforts to highlight potential vaccine inefficacies or the need for booster doses.

- **Resource Allocation:**  
  Determine regions with low vaccination coverage to plan targeted resource distribution and forecast vaccine demand.

- **Global Health Policy:**  
  Provide data-driven recommendations for vaccination policies and track progress towards international health targets.

## Project Structure

vaccination_analysis_project/ │ ├── data-set/
│ ├── coverage-data.xlsx │ ├── incidence-rate-data.xlsx │ ├── reported-cases-data.xlsx │ ├── vaccine-introduction-data.xlsx │ └── vaccine-schedule-data.xlsx │ ├── Main/
│ ├── data_inspection.py # Inspect raw data │ ├── data_cleaning.py # Clean the data │ ├── complete-EDA.py # Exploratory Data Analysis (EDA) │ ├── load_data_to_sqlite.py # Load Coverage Data into SQLite │ ├── load_incidence_to_sqlite.py # Load Incidence Data into SQLite │ ├── load_reported_to_sqlite.py # Load Reported Cases Data into SQLite │ ├── load_vaccine_intro_to_sqlite.py # Load Vaccine Introduction Data │ ├── load_vaccine_schedule_to_sqlite.py # Load Vaccine Schedule Data │ ├── export_to_csv.py # Export SQL tables to CSV files │ └── complete-EDA.py # Full EDA with visuals (saved images) │ └── VaccinationDB.db # SQLite database file


## Data Sets Explanation

**Coverage Data:**
- **Variables:** Group, Code, Name, Year, Antigen, Antigen_Description, Coverage_Category, Coverage_Category_Description, Target_Number, Doses, Coverage

**Incidence Rate Data:**
- **Variables:** Group, Code, Name, Year, Disease, Disease_Description, Denominator, Incidence_Rate

**Reported Cases Data:**
- **Variables:** Group, Code, Name, Year, Disease, Disease_Description, Cases

**Vaccine Introduction Data:**
- **Variables:** ISO_3_Code, Country_Name, WHO_Region, Year, Description, Intro

**Vaccine Schedule Data:**
- **Variables:** ISO_3_Code, Country_Name, WHO_Region, Year, Vaccine_Code, Vaccine_Description, Schedule_Rounds, Target_Pop, Target_Pop_Description, Geoarea, Age_Administered, Source_Comment

## Approach

### Data Cleaning & EDA (Python)
- **Data Cleaning:**  
  Handle missing values (impute or drop), normalize units, and ensure date consistency.
  
- **Exploratory Data Analysis (EDA):**  
  Use statistical summaries, line charts, histograms, and other visualizations to understand trends in vaccination coverage, disease incidence, and reported cases.

### SQL Database Setup
- **Database Design:**  
  Create tables (e.g., CoverageData, IncidenceData, etc.) in an SQLite database.
  
- **Data Loading:**  
  Use Python (with SQLAlchemy) to load cleaned data into the SQL database.

### Power BI Integration & Visualization
- **Import CSV Files:**  
  Export SQL tables to CSV and import them into Power BI.
  
- **Dashboard Creation:**  
  Build interactive dashboards with visuals such as line charts, bar charts, maps, and slicers to explore the data.
  
- **Interactivity:**  
  Use slicers (e.g., for YEAR, Country, Vaccine Type) to allow users to filter and interact with the visuals.

## Steps to Build the Power BI Dashboard

1. **Open Power BI Desktop** and click **Get Data → Text/CSV** to import each CSV file (e.g., `CoverageData.csv`, `IncidenceData.csv`, etc.).
2. **Review Data in Data View:**  
   Verify that all data is imported correctly.
3. **Switch to Report View** and create visuals:
   - **Line Chart:** Drag `YEAR` to the Axis and `COVERAGE` to Values to show trends.
   - **Bar Chart:** Use similar fields for incidence or reported cases.
   - **Map Visual:** If applicable, use geographical fields to show data on a world map.
   - **Slicers:** Add slicers for `YEAR`, `Country`, and `Vaccine Type` to filter data interactively.
4. **Format and Arrange:**  
   Organize visuals, add text boxes for titles, and apply a consistent theme.
5. **Save and Publish:**  
   Save your dashboard as a `.pbix` file and optionally publish to the Power BI Service.

## Documentation and Deliverables

### Deliverables:
- **Source Code:** Python scripts for data extraction, cleaning, EDA, and database loading.
- **SQL Database:** A structured SQLite database (`VaccinationDB.db`) with normalized tables.
- **Power BI Reports:** Interactive dashboards saved as a `.pbix` file.
- **Documentation:** This README file and a detailed project report summarizing your process, challenges, and insights.

## Contributors

- **Project Created By:** Sahana H M

## Conclusion

This project provides an end-to-end solution for analyzing vaccination data. It involves data cleaning and exploratory analysis using Python, storing clean data in an SQL database, and creating interactive, insightful dashboards with Power BI. The final deliverables include a comprehensive set of scripts, a structured database, polished visualizations, and detailed documentation to support public health decision-making.

