import pandas as pd
import requests
import json


df = pd.read_csv("/Users/niallsharma/Documents/StatProject/geonames-all-cities-with-a-population-1000.csv", sep=";")
dt = pd.read_csv("/Users/niallsharma/Documents/StatProject/Cleaned.csv", on_bad_lines='warn', sep="\t")

df.drop(columns=['Geoname ID', "ASCII Name", "Alternate Names", "Feature Class", "Feature Code", "Country Code", "Country Code 2", 
                 "Admin1 Code", "Admin2 Code", "Admin3 Code", "Admin4 Code", "Elevation", "DIgital Elevation Model", "Timezone", "Modification date", "LABEL EN", "Coordinates"], inplace=True)

cleaned = df.dropna(axis = 0)

cleaned["Country name EN"].astype("str")
dt["Country"].astype("str")

booleans = cleaned["Country name EN"].isin(dt["Country"])

cleaned = cleaned.loc[booleans, :]

print(cleaned.to_string())
cleaned.to_csv("CleanedGeoData.csv", sep="\t")

