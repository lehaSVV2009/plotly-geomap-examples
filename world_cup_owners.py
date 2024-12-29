import pandas as pd

from geo_map_utils import show_bubble_geo_map

# Load the dataset
df = pd.read_csv('football/world_cup_owners/world_cup_owners.csv')

# Add country flags for each country
country_flags = { }

# Define the country coordinates
country_coords = {
    'Уругвай': {'lat': -32.5228, 'lon': -55.7658},
    'Италия': {'lat': 41.8719, 'lon': 12.5674},
    'Франция': {'lat': 46.6034, 'lon': 1.8883},
    'Бразилия': {'lat': -14.2350, 'lon': -51.9253},
    'Швейцария': {'lat': 46.8182, 'lon': 8.2275},
    'Швеция': {'lat': 60.1282, 'lon': 18.6435},
    'Чили': {'lat': -35.6751, 'lon': -71.5430},
    'Англия': {'lat': 52.3555, 'lon': -1.1743},
    'Мексика': {'lat': 23.6345, 'lon': -102.5528},
    'ФРГ': {'lat': 51.1657, 'lon': 10.4515},
    'Аргентина': {'lat': -38.4161, 'lon': -63.6167},
    'Испания': {'lat': 40.4637, 'lon': -3.7492},
    'США': {'lat': 37.0902, 'lon': -95.7129},
    'Республика Корея': {'lat': 35.9078, 'lon': 127.7669},
    'Япония': {'lat': 36.2048, 'lon': 138.2529},
    'Германия': {'lat': 51.1657, 'lon': 10.4515},
    'ЮАР': {'lat': -30.5595, 'lon': 22.9375},
    'Россия': {'lat': 55.7, 'lon': 37.6},
    'Катар': {'lat': 25.3548, 'lon': 51.1839},
}

# Add latitude and longitude for each country
df['lat'] = df['Страна'].map(lambda x: country_coords[x]['lat'])
df['lon'] = df['Страна'].map(lambda x: country_coords[x]['lon'])
df['text'] = df.apply(lambda row: "", axis=1)


show_bubble_geo_map(df, 'Год', map_style='USGS')
