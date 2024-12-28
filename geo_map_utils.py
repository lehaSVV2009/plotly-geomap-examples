import os
from dotenv import load_dotenv

import plotly.express as px
import plotly.graph_objects as go

# Load environment variables from .env file
load_dotenv()

mapbox_accesstoken = os.getenv('MAPBOX_ACCESS_TOKEN')

MAP_STYLE_SIMPLE = 'simple'
MAP_STYLE_USGS = 'USGS'
MAP_STYLE_SATELLITE = 'satellite'

def show_bubble_geo_map(df, color_prop=None, lat_prop='lat', lon_prop='lon', text_prop='text', map_style='satellite', text_config={'size': 15, 'color': 'white', 'weight': 'bold'}, legends=[]):
    if map_style == MAP_STYLE_SIMPLE:
        show_scatter_geo_map(df, color_prop, lat_prop, lon_prop, text_prop, text_config, legends)
    else:
        show_mapbox_bubble_geo_map(df, color_prop, lat_prop, lon_prop, text_prop, map_style, text_config, legends)

def show_mapbox_bubble_geo_map(df, color_prop=None, lat_prop='lat', lon_prop='lon', text_prop='text', map_style='satellite', text_config={'size': 15, 'color': 'white', 'weight': 'bold'}, legends=[]):
    # Create the bubble map with scattermapbox
    fig = px.scatter_mapbox(
        df,
        lat=lat_prop,
        lon=lon_prop,
        text=text_prop,
        size=color_prop,
        color=color_prop,
        color_continuous_scale=[
            "white",
            "white"
        ],
        opacity=1,
        zoom=3.3,
    )

    # Update traces for marker appearance
    if not color_prop:
        fig.update_traces(
            marker=go.scattermapbox.Marker(
                symbol='circle', color='white', size=10),
        )

    fig.update_traces(
        textposition='middle right',
        textfont=dict(
            size=text_config.get('size', 30),
            color=text_config.get('color', 'white'),
            weight=text_config.get('weight', 'bold')
        ),
    )

    # Add legends as additional traces
    for legend in legends:
        fig.add_trace(go.Scattermapbox(
            lat=[legend['lat']],
            lon=[legend['lon']],
            text=legend['text'],
            mode='text',
            textfont=dict(
                size=legend.get('size', 30),
                color=legend.get('color', 'white'),
                weight=legend.get('weight', 'bold')
            ),
        ))

    if map_style == 'USGS':
        fig.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ],
            # mapbox=dict(
            #     style="carto-darkmatter",  # Use OpenStreetMap tiles
            #     zoom=3,  # Adjust the zoom level
            #     center=dict(lat=39.8283, lon=-98.5795)  # Center over USA
            # ),
            margin={"r": 0, "t": 0, "l": 0, "b": 0},  # Remove margins
        )
    else:
        fig.update_layout(
            mapbox_style=map_style,
            mapbox_accesstoken=mapbox_accesstoken,
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
        )

    # Show the plot
    fig.show()
    


def show_scatter_geo_map(df, color_prop=None, lat_prop='lat', lon_prop='lon', text_prop='text', text_config={'size': 8, 'color': 'white', 'weight': 'bold'}, legends=[]):
    fig = px.scatter_geo(df,
                         lat=lat_prop,
                         lon=lon_prop,
                         text=text_prop,
                         size=color_prop,
                         color=color_prop,
                         color_continuous_scale=[
                             "white",
                             "white",
                         ],
                         opacity=1
                         )

    # Update layout for better visualization
    fig.update_traces(textposition='top center',
                      textfont=dict(size=text_config.get('size'), color=text_config.get('color'), weight=text_config.get('weight')),
                      marker=dict(line=dict(width=1, color='black')))

    for legend in legends:
        fig.add_trace(go.Scattergeo(
            lat=[legend['lat']],
            lon=[legend['lon']],
            text=legend['text'],
            mode='text',
            textposition='bottom center',
            showlegend=False,
            textfont=dict(
                size=legend.get('size', 30),
                color=legend.get('color', 'white'),
                weight=legend.get('weight', 'bold')
            ),
        ))

    fig.update_geos(fitbounds="locations")
    fig.update_layout(
        geo=dict(
            coastlinecolor='black',
            showland=True, landcolor='darkgreen',
            showocean=True, oceancolor='black',
            showlakes=True, lakecolor='black',
            showrivers=True, rivercolor='black',
            showframe=False,
        ),
    )

    # Show the plot
    fig.show()
