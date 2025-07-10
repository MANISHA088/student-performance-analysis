# src/dashboard.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title="Student Performance Dashboard")

# --- Load Data ---
@st.cache_data
def load_data():
    return pd.read_csv('data/student_performance.csv')

df = load_data()

# --- Title ---
st.title("📊 Student Performance Analysis Dashboard")
st.markdown("Identify trends, top performers, and students at risk.")

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filters")
min_attendance = st.sidebar.slider("Minimum Attendance (%)", 0, 100, 50)
min_marks = st.sidebar.slider("Minimum Marks", 0, 100, 40)

filtered_df = df[(df['Attendance'] >= min_attendance) & (df['Marks'] >= min_marks)]

# --- Key Metrics ---
col1, col2, col3 = st.columns(3)
col1.metric("Average Marks", f"{df['Marks'].mean():.2f}")
col2.metric("Average Attendance", f"{df['Attendance'].mean():.2f}%")
col3.metric("Avg. Weekly Logins", f"{df['Logins'].mean():.1f}")

# --- At Risk Students ---
at_risk = df[(df['Marks'] < 40) | (df['Attendance'] < 75)]
st.subheader("⚠️ At-Risk Students")
st.dataframe(at_risk, use_container_width=True)

# --- Visualizations ---
st.subheader("📈 Visual Analysis")

# Marks Distribution
fig1, ax1 = plt.subplots()
sns.histplot(df['Marks'], bins=20, kde=True, ax=ax1, color="skyblue")
ax1.set_title("Distribution of Marks")
st.pyplot(fig1)

# Attendance vs Marks
fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x='Attendance', y='Marks', hue='Logins', palette='viridis', ax=ax2)
ax2.set_title("Attendance vs Marks (Colored by Logins)")
st.pyplot(fig2)

# Correlation Heatmap
fig3, ax3 = plt.subplots()
sns.heatmap(df[['Marks', 'Attendance', 'Logins']].corr(), annot=True, cmap='coolwarm', ax=ax3)
ax3.set_title("Correlation Matrix")
st.pyplot(fig3)
