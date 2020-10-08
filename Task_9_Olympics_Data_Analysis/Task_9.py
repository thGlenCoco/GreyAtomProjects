#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "./Olympics_Cleaned.csv"
user_data_dir = "."

#Path of the file is stored in the variable path
data = pd.read_csv(path)

#Code starts here
data.rename(columns = {"Total" : "Total_Medals"}, inplace = True)

# Data Loading
data.head()

# Summer or Winter
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'],'Both',data['Better_Event'])

better_event = data['Better_Event'].value_counts().index[0]
print(better_event)

# Top 10
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries = top_countries[:-1]

def top_ten(top_countries,column):

    country_list = list((top_countries.nlargest(10,column)["Country_Name"]))
    return country_list

top_10_summer = top_ten(top_countries,"Total_Summer")
top_10_winter = top_ten(top_countries,"Total_Winter")
top_10 = top_ten(top_countries,"Total_Medals")

print(top_10_summer)
print(top_10_winter)
print(top_10)
common = [i for i in top_10_summer if i in top_10_winter and i in top_10]

# Plotting top 10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot("Country_Name","Total_Summer",kind="bar")
winter_df.plot("Country_Name","Total_Winter",kind="bar")

# Top Performing Countries
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

winter_df["Golden_Ratio"] = winter_df["Gold_Winter"]/winter_df["Total_Winter"]
winter_max_ratio = max(winter_df["Golden_Ratio"])
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df["Golden_Ratio"] = top_df["Gold_Total"]/top_df["Total_Medals"]
top_max_ratio = max(top_df["Golden_Ratio"])
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']

# Best in the world
data_1 = data[:-1]

data_1["Total_Points"] = data["Gold_Total"] * 3 + data["Silver_Total"] * 2 + data["Bronze_Total"] * 1
most_points = max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(most_points)
print(best_country)

# Plotting the best
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
