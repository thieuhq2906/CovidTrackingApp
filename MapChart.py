import geopandas as gpd
import io
import pandas as pd
import UpdateAndReadData.readdata as READ
import numpy as np
from fiona import _shim, schema
import datetime
def GetMapChart():
    df = READ.dataCovid
    df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
    df['total_vaccinations_per_hundred'] = df['total_vaccinations_per_hundred'].replace(np.nan, -1)
    delta = datetime.timedelta(days=1)
    condition = (df['date'] == max(df['date'])-delta)
    data = df.loc[condition]
    ratetotal = []
    for row_index,row in data.iterrows():
        rate = max(df.loc[df['location']== row['location']]['total_vaccinations_per_hundred'])
        if rate == -1:
            rate = np.nan
        ratetotal.append(rate)
    #print(data['total_cases'])
    data['Rate of total vaccinated'] = ratetotal
    data = data[['iso_code','Rate of total vaccinated','location','new_cases','new_deaths']]
    #print(data[data['location'] == 'Vietnam'].info())
    gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    #print(gdf.info())
    #data.to_csv("out.csv")
    merged = gdf.merge(data, left_on = 'iso_a3', right_on = 'iso_code')
    #print(merged.head(2))
    #merged.plot(column='total_cases', cmap='BuGn', scheme='quantiles')
    map = merged.explore(column='Rate of total vaccinated',cmap='Blues',legend = True,scheme='quantiles',tooltip = ['location','Rate of total vaccinated','new_cases','new_deaths'])
    map.zoom_start = 20 
    data = io.BytesIO()
    map.save(data, close_file=False)
    return data 