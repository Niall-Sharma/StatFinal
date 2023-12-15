import pandas as pd
import requests
import json


starURL = "/Users/niallsharma/Documents/StatProject/michelin_my_maps.csv"

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

cleaned[['City','Country']] = cleaned.Location.str.split(",", expand=True)
cleaned.drop(columns=['Location'], inplace=True)
cleaned.drop(columns=['Description'], inplace=True)

priceLevel = pd.Series([len(x) for x in cleaned['Price']])
cleaned.loc[:,'Price Level'] = priceLevel.values
cleaned.loc[:,'Price'] = cleaned['Price'].astype(str).str[0]




jsonThing = '{"name": "Georgian Bluffs","latitude": 44.65, "longitude": -81.0333, "country": "CA", "population": 10479,"is_capital": false}'

parsed = json.loads(jsonThing)
# print(parsed["population"])


cleaned = cleaned.drop(cleaned[cleaned['Award'] == 'B'].index)
cleaned = cleaned.drop(cleaned[cleaned['Award'] == 'G'].index)

cleaned = cleaned.drop(cleaned[cleaned['Cuisine'].str.contains(",")].index)

# response = requests.get(API_URL+"Georgian Bluffs",headers={'X-Api-Key': 'tG20tFTE/3t1wtdivCBbwA==hx8CDERs4x1KyF23'}).json()
# s1 = json.dumps(response[0])
# jsonFile = json.loads(s1)
# print(jsonFile["population"])
populations = []
# for index, row in cleaned.iterrows():
#     response = requests.get(API_URL+row['City'],headers={'X-Api-Key': 'tG20tFTE/3t1wtdivCBbwA==hx8CDERs4x1KyF23'})

#     if response.status_code == requests.codes.ok:
#         asJson = response.json()
#         if(len(asJson) > 0):
#             s1 = json.dumps(asJson[0])
#             jsonFile = json.loads(s1)
#             populations.append(jsonFile["population"])
#         else:
#             populations.append(0)
#     else:
#         print("Error:", response.status_code, response.text)

cleaned.loc[:, "Population"] = populations

cleaned.to_csv("Cleaned.csv", sep="\t")
