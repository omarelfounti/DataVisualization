import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import streamlit as st
import pandas as pd

# Load datasets
prices_df = pd.read_csv('fmi_weather_and_price.csv', parse_dates=['Time'])
weather_df = pd.read_csv('fmi_weather.csv', parse_dates=['Time'])

# Remove extra unnamed column if it exists
weather_df = weather_df.loc[:, ~weather_df.columns.str.contains('^Unnamed')]

# Convert 'Time' to datetime format in both DataFrames
prices_df['Time'] = pd.to_datetime(prices_df['Time'], errors='coerce')
weather_df['Time'] = pd.to_datetime(weather_df['Time'], errors='coerce')

# Drop rows where 'Time' is NaT
prices_df.dropna(subset=['Time'], inplace=True)
weather_df.dropna(subset=['Time'], inplace=True)

# Remove duplicates
prices_df.drop_duplicates(subset=['Time'], inplace=True)
weather_df.drop_duplicates(subset=['Time'], inplace=True)

# Check for overlapping timestamps
common_times = set(prices_df['Time']).intersection(set(weather_df['Time']))
print("Total common timestamps:", len(common_times))
print("Example common timestamps:", list(common_times)[:5])

# If timestamps do not match, round them to the nearest hour
prices_df['Time'] = prices_df['Time'].dt.floor('H')
weather_df['Time'] = weather_df['Time'].dt.floor('H')

print("Prices DF - First 5 timestamps:")
print(prices_df[['Time']].head())

print("\nWeather DF - First 5 timestamps:")
print(weather_df[['Time']].head())

# Standardize 'Time' format and remove seconds
prices_df['Time'] = prices_df['Time'].dt.strftime("%Y-%m-%d %H:%M")
weather_df['Time'] = weather_df['Time'].dt.strftime("%Y-%m-%d %H:%M")

# Convert back to datetime format (now without seconds)
prices_df['Time'] = pd.to_datetime(prices_df['Time'], format="%Y-%m-%d %H:%M")
weather_df['Time'] = pd.to_datetime(weather_df['Time'], format="%Y-%m-%d %H:%M")

common_times = set(prices_df['Time']).intersection(set(weather_df['Time']))
print("\nTotal common timestamps:", len(common_times))
print("\nExample common timestamps:", list(common_times)[:5])

print(prices_df['Time'].dt.tz)
print(weather_df['Time'].dt.tz)

prices_df['Time'] = prices_df['Time'].dt.tz_localize('UTC')
weather_df['Time'] = weather_df['Time'].dt.tz_localize('UTC')

# Merge DataFrames
df = pd.merge(prices_df, weather_df, on='Time', how='inner')

# Handle missing values in merged dataset
df.dropna(inplace=True)

# Display first few rows for validation
print("Merged DF - First 5 rows:")
print(df.head())
print("Merged DF - Shape:", df.shape)

# Streamlit app
st.title('Electricity Prices and Weather Conditions in Finland')
st.write(df.head())
