import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from geo_map_utils import show_bubble_geo_map

# Load the dataset
df = pd.read_csv('kvn/kvn_winners.csv')

# Define the city coordinates

city_coords = {
  'Пермь': {'lat': 58.0104, 'lon': 56.2294},
  'Одесса': {'lat': 46.4825, 'lon': 30.7233},
  'Новосибирск': {'lat': 55.0084, 'lon': 82.9357},
  'Харьков': {'lat': 49.9935, 'lon': 36.2304},
  'Ереван': {'lat': 40.1792, 'lon': 44.4991},
  'Баку': {'lat': 40.4093, 'lon': 49.8671},
  'Москва': {'lat': 55.7558, 'lon': 37.6173},
  'Махачкала': {'lat': 42.9849, 'lon': 47.5047},
  'Запорожье': {'lat': 47.8388, 'lon': 35.1396},
  'Томск': {'lat': 56.4846, 'lon': 84.9483},
  'Минск': {'lat': 53.9045, 'lon': 27.5615},
  'Екатеринбург': {'lat': 56.8389, 'lon': 60.6057},
  'Магнитогорск': {'lat': 53.4072, 'lon': 58.9791},
  'Челябинск': {'lat': 55.1644, 'lon': 61.4368},
  'Сочи': {'lat': 43.6028, 'lon': 39.7342},
  'Пятигорск': {'lat': 44.0486, 'lon': 43.0594},
  'Сухум': {'lat': 43.0000, 'lon': 41.0167},
  'Курск': {'lat': 51.7308, 'lon': 36.1939},
  'Армавир': {'lat': 45.0010, 'lon': 41.1322},
  'Брюховецкая': {'lat': 45.8000, 'lon': 38.9833},
  'Самара': {'lat': 53.1959, 'lon': 50.1000},
  'Смоленск': {'lat': 54.7826, 'lon': 32.0453},
  'Тюмень': {'lat': 57.1613, 'lon': 65.5250},
  'Астрахань': {'lat': 46.3497, 'lon': 48.0408},
  'Бишкек': {'lat': 42.8746, 'lon': 74.5698},
  'Астана': {'lat': 51.1694, 'lon': 71.4491},
  'Киров': {'lat': 58.6035, 'lon': 49.6679},
  'Иркутск': {'lat': 52.2869, 'lon': 104.3050},
  'Красноярск': {'lat': 56.0153, 'lon': 92.8932},
  'Альметьевск': {'lat': 54.9014, 'lon': 52.2971},
  'Королёв': {'lat': 55.9142, 'lon': 37.8256},
  'Могилёв': {'lat': 53.9168, 'lon': 30.3449},
  'Ростов-на-Дону': {'lat': 47.2357, 'lon': 39.7015},
}

# Add latitude and longitude for each country
df['lat'] = df['Город'].map(lambda x: city_coords[x]['lat'])
df['lon'] = df['Город'].map(lambda x: city_coords[x]['lon'])
df['text'] = df.apply(lambda row: "", axis=1)


show_bubble_geo_map(df, 'Год')
