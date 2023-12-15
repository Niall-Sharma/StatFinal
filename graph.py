import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("DataSources/Cleaned.csv", on_bad_lines='warn',sep="\t")
dt = pd.read_csv("DataSources/CleanedGeoData.csv", on_bad_lines='warn', sep="\t")

df['City'].astype('str')
df['Country'].astype('str')
df['Price'].astype('str')
df['Cuisine'].astype('str')
df['Award'].astype('str')
print(df['Country'].value_counts())
