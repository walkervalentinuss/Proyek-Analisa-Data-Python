import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def create_hour_df(df):
    hour_dataset = sns.boxplot(x='weekday', y='cnt', data=df)
    return hour_dataset

def create_hour_df(df):
    sns.barplot(data=hour_dataset, x="weekday", y="cnt", hue="weathersit", errorbar=None)

with st.sidebar:
    # Menambahkan Logo
    st.image("https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi.huffpost.com%2Fgen%2F1160899%2Fimages%2Fo-CITI-BIKE-facebook.jpg&f=1&nofb=1&ipt=282e630cd158137f871e10a736669be0280d3290fb92064ded477f56e23d7416&ipo=images")
    st.header("BIKE SHARING 2011 - 2012")

day_df = pd.read_csv("day.csv")
hour_dataset = pd.read_csv("hour_df_cleaned.csv")

st.header('Dashboard Project Bike Sharing :sparkles:')

st.subheader("Distribution of bike rentals per day")
fig, ax = plt.subplots(figsize=(20, 10))

sns.boxplot(
    y="Count",
    x="Weekdays",
    data=hour_dataset
)

# # Distribution of bike rentals per day

