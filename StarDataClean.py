import pandas as pd
import requests
import json

starURL = "DataSources/michelin_my_maps.csv"

API_URL = "https://api.api-ninjas.com/v1/city?name="

df = pd.read_csv(starURL)
df.drop(columns=['Address', 'PhoneNumber', 'Url',
                'WebsiteUrl', 'FacilitiesAndServices', "Longitude", "Latitude"], inplace=True)

cleaned = df.dropna(axis = 0)
cleaned['Name'].astype('str')
cleaned['Location'].astype('str')
cleaned['Price'].astype('str')
cleaned['Cuisine'].astype('str')
cleaned['Award'].astype('str')

cleaned.loc[:,'Award'] = cleaned['Award'].astype(str).str[0]

cleaned[['City','Country']] = cleaned.Location.str.split(", ", expand=True)
cleaned.drop(columns=['Location'], inplace=True)
cleaned.drop(columns=['Description'], inplace=True)

priceLevel = pd.Series([len(x) for x in cleaned['Price']])
cleaned.loc[:,'Price Level'] = priceLevel.values
cleaned.loc[:,'Price'] = cleaned['Price'].astype(str).str[0]


cleaned = cleaned.drop(cleaned[cleaned['Award'] == 'B'].index)
cleaned = cleaned.drop(cleaned[cleaned['Award'] == 'G'].index)

cleaned = cleaned.drop(cleaned[cleaned['Cuisine'].str.contains(",")].index)


cleaned.to_csv("DataSources/Cleaned.csv", sep="\t", index=False)
