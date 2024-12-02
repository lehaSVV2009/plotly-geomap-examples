import os
from dotenv import load_dotenv

import plotly.express as px
import plotly.graph_objects as go

# Load environment variables from .env file
load_dotenv()

mapbox_accesstoken=os.getenv('MAPBOX_ACCESS_TOKEN')

def create_geo_map_image(df, color_prop, map_style='satellite', text_config = { 'size': 15, 'color': 'white', 'weight': 'bold' }, legends=[]):
    # Create the bubble map with scattermapbox
    if color_prop:
        fig = px.scatter_mapbox(
            df,
            lat='lat',
            lon='lon',
            text='text',
            size=color_prop,
            color=color_prop,
            color_continuous_scale=[
                "white",
                "white"
            ],
            opacity=1,
            zoom=3.3,
        )
    else:
        fig = px.scatter_mapbox(
            df,
            lat='lat',
            lon='lon',
            text='text',
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

    if map_style == 'white-bg':
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
            mapbox_style="satellite",
            mapbox_accesstoken=mapbox_accesstoken,
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
        )

    # Show the plot
    fig.show()
