import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

with st.sidebar:
    # Menambahkan Logo
    st.image("https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi.huffpost.com%2Fgen%2F1160899%2Fimages%2Fo-CITI-BIKE-facebook.jpg&f=1&nofb=1&ipt=282e630cd158137f871e10a736669be0280d3290fb92064ded477f56e23d7416&ipo=images")
    st.header("BIKE SHARING 2011 - 2012")

day_df = pd.read_csv("../Dashboard/day_df_cleaned.csv")
hour_dataset = pd.read_csv("../Dashboard/hour_df_cleaned.csv")

st.header('Dashboard Project Bike Sharing :sparkles:')

fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(data=hour_dataset, x="weekday", y="cnt", hue="weathersit", errorbar=None)

ax.set_title("Number of Customers Based on Weathersit", loc="center", fontsize=50)
ax.set_ylabel("Count")
ax.set_xlabel("Weekday")
ax.tick_params(axis='x', labelsize=30)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(20, 10))
sns.boxplot(x='weekday', y='cnt', data=hour_dataset)

ax.set_title("Distribution of bike rentals per day", loc="center", fontsize=50)
ax.set_ylabel("Count")
ax.set_xlabel("Weekday")
ax.tick_params(axis='x', labelsize=30)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)


st.caption('Copyright (c) walkervalentinuss')