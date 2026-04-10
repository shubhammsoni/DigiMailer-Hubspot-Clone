import streamlit as st
import pandas as pd

# Title
st.title("📊 Email Tracker Dashboard")

# Load data
try:
    df = pd.read_csv("tracking_data.csv")
except:
    st.error("No tracking data found!")
    st.stop()

# Show raw data
st.subheader("📁 Raw Data")
st.dataframe(df)

# Metrics
st.subheader("📈 Metrics")

total_opens = len(df[df['type'] == 'open'])
total_clicks = len(df[df['type'] == 'click'])

col1, col2 = st.columns(2)
col1.metric("📬 Opens", total_opens)
col2.metric("🔗 Clicks", total_clicks)

# Per user stats
st.subheader("👤 User Activity")

user_stats = df.groupby(['email', 'type']).size().unstack(fill_value=0)
st.dataframe(user_stats)

# Chart
st.subheader("📊 Activity Chart")

chart_data = df['type'].value_counts()
st.bar_chart(chart_data)