import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from geo_map_utils import show_bubble_geo_map, MAP_STYLE_USGS

# Load and merge multiple datasets
files = [
    'football/continental_cup/continental_cup_winners_africa.csv',
    'football/continental_cup/continental_cup_winners_asia.csv',
    'football/continental_cup/continental_cup_winners_concacaf.csv',
    'football/continental_cup/continental_cup_winners_copa.csv',
    'football/continental_cup/continental_cup_winners_europe.csv',
    'football/continental_cup/continental_cup_winners_oceania.csv',
]

dfs = [pd.read_csv(file) for file in files]
raw_df = pd.concat(dfs)

# Group by 'Победитель' and aggregate the data
df = raw_df.groupby('Страна').agg(
    Победы=('Год', 'count'),
    Годы=('Год', lambda x: ', '.join(map(str, x)))
).reset_index()

# Add latitude and longitude for each country
country_coords = {
    'Коста-Рика': {'lat': 9.7489, 'lon': -83.7534},
    'Мексика': {'lat': 23.6345, 'lon': -102.5528},
    'Гватемала': {'lat': 15.7835, 'lon': -90.2308},
    'Гаити': {'lat': 18.9712, 'lon': -72.2852},
    'Гондурас': {'lat': 15.2000, 'lon': -86.2419},
    'Канада': {'lat': 45.4215, 'lon': -75.6972},
    'США': {'lat': 37.0902, 'lon': -95.7129},
    'Уругвай': {'lat': -34.9011, 'lon': -56.1645},
    'Бразилия': {'lat': -14.2350, 'lon': -51.9253},
    'Аргентина': {'lat': -39, 'lon': -63},
    'Перу': {'lat': -9.1900, 'lon': -75.0152},
    'Парагвай': {'lat': -23.4425, 'lon': -58.4438},
    'Боливия': {'lat': -16.2902, 'lon': -63.5887},
    'Колумбия': {'lat': 4.5709, 'lon': -74.2973},
    'Чили': {'lat': -35.6751, 'lon': -71.5430},
    'Египет': {'lat': 26.8206, 'lon': 30.8025},
    'Эфиопия': {'lat': 9.1450, 'lon': 40.4897},
    'Гана': {'lat': 7.9465, 'lon': -1.0232},
    'Конго': {'lat': -0.2280, 'lon': 15.8277},
    'ДР Конго': {'lat': -4.0383, 'lon': 21.7587},
    'Судан': {'lat': 12.8628, 'lon': 30.2176},
    'Марокко': {'lat': 31.7917, 'lon': -7.0926},
    'Нигерия': {'lat': 9.0820, 'lon': 8.6753},
    'Камерун': {'lat': 3.8480, 'lon': 11.5021},
    'Алжир': {'lat': 28.0339, 'lon': 1.6596},
    'Кот-д\'Ивуар': {'lat': 7.5399, 'lon': -5.5471},
    'ЮАР': {'lat': -30.5595, 'lon': 22.9375},
    'Тунис': {'lat': 33.8869, 'lon': 9.5375},
    'Замбия': {'lat': -13.1339, 'lon': 27.8493},
    'Сенегал': {'lat': 14.4974, 'lon': -14.4524},
    'СССР': {'lat': 55.7512, 'lon': 37.6184},
    'Испания': {'lat': 40.4637, 'lon': -3.7492},
    'Италия': {'lat': 41.8719, 'lon': 12.5674},
    'Германия': {'lat': 51.1657, 'lon': 10.4515},
    'Чехословакия': {'lat': 49.8175, 'lon': 15.4730},
    'Франция': {'lat': 46.6034, 'lon': 1.8883},
    'Нидерланды': {'lat': 52.1326, 'lon': 5.2913},
    'Дания': {'lat': 56.2639, 'lon': 9.5018},
    'Греция': {'lat': 39.0742, 'lon': 21.8243},
    'Португалия': {'lat': 39.3999, 'lon': -8.2245},
    'Республика Корея': {'lat': 35.9078, 'lon': 127.7669},
    'Израиль': {'lat': 31.0461, 'lon': 34.8516},
    'Иран': {'lat': 32.4279, 'lon': 53.6880},
    'Кувейт': {'lat': 29.3117, 'lon': 47.4818},
    'Саудовская Аравия': {'lat': 23.8859, 'lon': 45.0792},
    'Япония': {'lat': 36.2048, 'lon': 138.2529},
    'Ирак': {'lat': 33.2232, 'lon': 43.6793},
    'Австралия': {'lat': -25.2744, 'lon': 133.7751},
    'Катар': {'lat': 25.3548, 'lon': 51.1839},
    'Новая Зеландия': {'lat': -40.9006, 'lon': 174.8860},
    'Таити': {'lat': -17.6509, 'lon': -149.4260},
}

# Add latitude and longitude for each country
df['lat'] = df['Страна'].map(lambda x: country_coords[x]['lat'])
df['lon'] = df['Страна'].map(lambda x: country_coords[x]['lon'])
df['text'] = df.apply(lambda row: f"", axis=1)


show_bubble_geo_map(df, 'Победы', map_style=MAP_STYLE_USGS)
