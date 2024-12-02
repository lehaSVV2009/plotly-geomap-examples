import pandas as pd

from geo_map_utils import create_geo_map_image
from europe_utils import city_coords, country_flags

# Load the dataset
df = pd.read_csv('europe_cities/europe_cities_ru.csv')

# Add latitude and longitude for each country
df['lat'] = df['Самый населенный город'].map(lambda x: city_coords[x]['lat'])
df['lon'] = df['Самый населенный город'].map(lambda x: city_coords[x]['lon'])
# df['text'] = df.apply(
#     lambda row: f"{country_flags[row['Страна']]} {row['Самый населенный город']} ({row['Население']} млн.чел., {row['Население с агломерацией']} млн.чел.)", axis=1)

df['text'] = df.apply(
    lambda row: f"{country_flags[row['Страна']]} {row['Население с агломерацией']}", axis=1)

create_geo_map_image(df, 'Население с агломерацией',

                     #  'Самый населенный город в стране с агломерацией: Европа',
                     #  "Население города с агломерацией в млн.чел.", 'Население'
                     )
