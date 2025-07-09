# student-performance-analysis
📊 Interactive dashboard and data analysis to identify student performance trends, highlight at-risk students, and support academic interventions using Python 


📚 Overview

This project analyzes student academic performance using a dataset containing marks, attendance, and login records. The goal is to identify performance trends, highlight at-risk students, and provide actionable insights for academic interventions.

🏆 Problem Statement

Institutions need early warnings for students who might fail or drop out.

By analyzing academic and behavioral data, we aim to spot performance trends and risk areas, enabling targeted support for struggling students.

🎯 Objectives

Calculate averages, correlations, and the impact of absenteeism on performance.

Visualize top vs. struggling students using bar charts and heatmaps.

Build a dashboard to support academic interventions.




📁 Dataset Description
Fields: Student ID, Name, Marks, Attendance (%), Logins (per week)

Source: [ ]

Sample:




🛠️ Approach & Methodology

Data Cleaning:

Handle missing/null values.

Convert data types as needed.


Exploratory Data Analysis (EDA):

Calculate mean, median, and standard deviation for marks and attendance.

Analyze correlation between attendance, logins, and marks.

Identify students at risk (e.g., marks < 40 or attendance < 75%).



Visualization:

Bar charts: Top vs. struggling students.

Heatmaps: Correlation matrix for all features.

Additional: Distribution of marks, attendance patterns.



🖼️ Output Screenshots



📊 Key Results

High correlation between attendance and marks (r = 0.78).

Students with <75% attendance are 3x more likely to score below 40.

Top performers consistently log in more than 15 times per week.



📑 Project Structure


student-performance-analysis/
│
├── data/                 # Dataset files
├── notebooks/            # Jupyter notebooks for EDA and modeling
├── src/                  # Source code for dashboard/app
├── screenshots/          # Output screenshots
├── README.md
├── requirements.txt




📝 Dependencies

Python 3.8+ , 
pandas , 
numpy , 
matplotlib , 
seaborn , 
streamlit (for dashboard)

🚀 Future Work
Integrate more features (assignment scores, extracurriculars).
Predictive modeling for at-risk students using machine learning.
Real-time dashboard integration with school databases.
