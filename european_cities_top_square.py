import pandas as pd

from geo_map_utils import show_bubble_geo_map

COORDINATES_PATH = 'european_cities_top_square/coordinates.csv'
STATS_PATH = 'european_cities_top_square/stats.csv'
MERGE_COLUMN='City'
BUBBLE_COLUMN='Square'
LAT_COLUMN='Lat'
LON_COLUMN='Lon'

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