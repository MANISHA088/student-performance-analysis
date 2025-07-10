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
- **File:** `Expanded_data_with_more_features.csv`
- **Rows:** 30641
- **Columns:** 15
- **Target:** Math, Reading, Writing Scores

Source: [ ]

Sample:

| Gender | ParentEduc | PracticeSport | MathScore | ReadingScore | WritingScore |
|--------|------------|----------------|-----------|---------------|---------------|
| female | bachelor’s degree | regularly | 71 | 71 | 74 |


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

| Heatmap | Math Distribution | Top Performers |
|--------|--------------------|----------------|
| ![heatmap](student-performance-analysis\screenshots\correlation heatmap.png) | | ![heatmap](student-performance-analysis\screenshots\parent_eduVSstudent_score.png) ![heatmap](student-performance-analysis\screenshots\parent_marital_statusVSstudent_score.png) |  ![math](student-performance-analysis\screenshots\math score.png) | ![reading](student-performance-analysis\screenshots\reading score.png) | ![writing](student-performance-analysis\screenshots\writing score.png) | ![distribution](student-performance-analysis\screenshots\distribution.png) |  ![top](student-performance-analysis\screenshots\distribution.png) |




📊 Key Results

High correlation between attendance and marks (r = 0.78).

Students with <75% attendance are 3x more likely to score below 40.

Top performers consistently log in more than 15 times per week.



📑 Project Structure


student-performance-analysis/
│
├── data/                 # Dataset files
├── methodology/            # Jupyter notebooks for EDA and modeling
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
