import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("/Users/niallsharma/Documents/StatProject/Cleaned.csv", on_bad_lines='warn',sep="\t")
dt = pd.read_csv("/Users/niallsharma/Documents/StatProject/CleanedGeoData.csv", on_bad_lines='warn', sep="\t")

# df['City'].value_counts()
df['City'].astype('str')
df['Country'].astype('str')
df['Price'].astype('str')
df['Cuisine'].astype('str')
df['Award'].astype('str')
print(df['Country'].value_counts())
