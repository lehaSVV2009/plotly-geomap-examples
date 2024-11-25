import plotly.express as px
import plotly.graph_objects as go
import base64

map_filename = './football/golden_ball.png'
montreal_road_map = base64.b64encode(open(map_filename, 'rb').read())


def create_geo_map_image(df, color_prop, legends=[]):
    # Create the bubble map with scattermapbox
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

    # Update traces for marker appearance
    fig.update_traces(
        textposition='middle right',
        textfont=dict(size=15, color='white', weight="bold"),
        # marker=go.scattermapbox.Marker(symbol='soccer', color='white', size=20),
    )

    # Add legends as additional traces
    for legend in legends:
        fig.add_trace(go.Scattermapbox(
            lat=[legend['lat']],
            lon=[legend['lon']],
            text=legend['text'],
            mode='text',
            showlegend=True,
            textfont=dict(
                size=legend.get('size', 30),
                color=legend.get('color', 'white'),
                weight=legend.get('weight', 'bold')
            ),
        ))

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

    # Show the plot
    fig.show()
