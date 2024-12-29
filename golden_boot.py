import pandas as pd
from geo_map_utils import show_bubble_geo_map, MAP_STYLE_USGS

# Load the dataset
df = pd.read_csv('football/golden_boot.csv')

# Define the country flags
country_flags = {
    'Австрия': '🇦🇹',
    'Аргентина': '🇦🇷',
    'Бельгия': '🇧🇪',
    'Болгария': '🇧🇬',
    'Бразилия': '🇧🇷',
    'Великобритания': '🇬🇧',
    'Греция': '🇬🇷',
    'Италия': '🇮🇹',
    'Кипр': '🇨🇾',
    'Мексика': '🇲🇽',
    'Нидерланды': '🇳🇱',
    'Норвегия': '🇳🇴',
    'Польша': '🇵🇱',
    'Португалия': '🇵🇹',
    'Румыния': '🇷🇴',
    'Турция': '🇹🇷',
    'Уругвай': '🇺🇾',
    'Германия': '🇩🇪',
    'Франция': '🇫🇷',
    'Швеция': '🇸🇪',
    'Югославия': '🇷🇸',
}

# Define the country coordinates
country_coords = {
    'Аргентина': {'lat': -38.4161, 'lon': -63.6167},
    'Уругвай': {'lat': -32.5228, 'lon': -55.7658},
    'Бразилия': {'lat': -14.2350, 'lon': -51.9253},
    'Мексика': {'lat': 23.6345, 'lon': -102.5528},
    'Югославия': {'lat': 50, 'lon': -17},
    'Франция': {'lat': 47.6034, 'lon': 1.8883},
    'Германия': {'lat': 51.1657, 'lon': 10.4515},
    'Нидерланды': {'lat': 52.1326, 'lon': 5.2913},
    'Португалия': {'lat': 39.3999, 'lon': -8.2245},
    'Италия': {'lat': 41.8719, 'lon': 12.5674},
    'Австрия': {'lat': 47.5162, 'lon': 14.5501},
    'Великобритания': {'lat': 54.3555, 'lon': -1.5},
    'Бельгия': {'lat': 49.8503, 'lon': 4.3517},
    'Болгария': {'lat': 42.7339, 'lon': 25.4858},
    'Греция': {'lat': 39.0742, 'lon': 21.8243},
    'Кипр': {'lat': 35.1264, 'lon': 33.4299},
    # 'Мексика': {'lat': 23.6345, 'lon': -102.5528},
    'Норвегия': {'lat': 60.4720, 'lon': 8.4689},
    'Польша': {'lat': 51.9194, 'lon': 20.1451},
    'Румыния': {'lat': 45.9432, 'lon': 24.9668},
    'Турция': {'lat': 38.9637, 'lon': 35.2433},
    # 'Уругвай': {'lat': -32.5228, 'lon': -55.7658},
    'Германия': {'lat': 51, 'lon': 10.4515},
    'Швеция': {'lat': 59.33, 'lon': 16.6435},
    # 'Югославия': {'lat': 44.0165, 'lon': 21.0059},
}

# Add latitude and longitude for each country
df['lat'] = df['Страна'].map(lambda x: country_coords[x]['lat'])
df['lon'] = df['Страна'].map(lambda x: country_coords[x]['lon'])
df['text'] = df.apply(
    lambda row: f"{country_flags[row['Страна']]}   {row['Страна']} ({row['Победы']}, {row['Игроки']})", axis=1)

show_bubble_geo_map(df, 'Победы', map_style=MAP_STYLE_USGS)

