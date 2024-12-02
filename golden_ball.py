import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from geo_map_utils import create_geo_map_image

# Load the dataset
df = pd.read_csv('football/golden_ball.csv')

# Add country flags for each country
country_flags = {
    'Аргентина': '🇦🇷',
    'Франция': '🇫🇷',
    'Германия': '🇩🇪',
    'ФРГ': '🇩🇪',
    'Нидерланды': '🇳🇱',
    'Португалия': '🇵🇹',
    'Италия': '🇮🇹',
    'Великобритания': '🇬🇧',
    'Бразилия': '🇧🇷',
    'Испания': '🇪🇸',
    'СССР': '🇷🇺',
    'Украина': '🇺🇦',
    'Чехия': '🇨🇿',
    'Чехословакия': '🇨🇿',
    'Венгрия': '🇭🇺',
    'Дания': '🇩🇰',
    'Болгария': '🇧🇬',
    'Либерия': '🇱🇷',
    'Хорватия': '🇭🇷',
}

# Add latitude and longitude for each country
country_coords = {
    'Аргентина': {'lat': -34.6037, 'lon': -58.3816},
    'Бразилия': {'lat': -14.2350, 'lon': -51.9253},
    'Либерия': {'lat': 6.4281, 'lon': -9.4295},
    'ФРГ': {'lat': 50, 'lon': -17},
    'СССР': {'lat': 48, 'lon': -17},
    'Чехословакия': {'lat': 46, 'lon': -17},
    'Франция': {'lat': 47.6034, 'lon': 1.8883},
    'Германия': {'lat': 49.5, 'lon': 7.5},
    'Нидерланды': {'lat': 52.1326, 'lon': 5.2913},
    'Португалия': {'lat': 38.5, 'lon': -8.2245},
    'Италия': {'lat': 41.8719, 'lon': 12.5674},
    'Великобритания': {'lat': 54.3555, 'lon': -1.5},
    'Испания': {'lat': 41, 'lon': -2.5},
    'Украина': {'lat': 50.4501, 'lon': 30.5234},  # Updated to Kiev coordinates
    'Чехия': {'lat': 49.92, 'lon': 17.72},
    'Венгрия': {'lat': 47.1625, 'lon': 19.5033},
    'Дания': {'lat': 56.2639, 'lon': 9.5018},
    'Болгария': {'lat': 42.7339, 'lon': 25.4858},
    'Хорватия': {'lat': 45.1, 'lon': 15.2},
}

# Add latitude and longitude for each country
df['lat'] = df['Страна'].map(lambda x: country_coords[x]['lat'])
df['lon'] = df['Страна'].map(lambda x: country_coords[x]['lon'])
df['text'] = df.apply(
    lambda row: f"{country_flags[row['Страна']]}   {row['Страна']} ({row['Победы']}, {row['Игроки']})", axis=1)


create_geo_map_image(df, 'Победы')
