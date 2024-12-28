import pandas as pd

from geo_map_utils import show_bubble_geo_map

COORDINATES_PATH = 'european_cities_with_population_over_1_million/coordinates.csv'
STATS_PATH = 'european_cities_with_population_over_1_million/stats.csv'
MERGE_COLUMN='Город'
BUBBLE_COLUMN='Население'
LAT_COLUMN='Широта'
LON_COLUMN='Долгота'

coords_df = pd.read_csv(COORDINATES_PATH)
stats_df = pd.read_csv(STATS_PATH)
df = pd.merge(coords_df, stats_df, on=MERGE_COLUMN)

show_bubble_geo_map(
  df,
  BUBBLE_COLUMN,
  map_style='satellite',
  lat_prop=LAT_COLUMN,
  lon_prop=LON_COLUMN,
  text_prop=None,
)
