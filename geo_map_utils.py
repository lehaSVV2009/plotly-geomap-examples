import plotly.express as px
import plotly.graph_objects as go


def create_geo_map_image(df, title, subtitle, color_prop, title_lat=66, title_lon=10, subtitle_lat=32, subtitle_lon=10):
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
        zoom=3,  # Adjust initial zoom level
    )

    # Update traces for marker appearance
    fig.update_traces(
        textposition='top center',
        textfont=dict(size=15, color='white'),
        # marker=dict(line=dict(width=1, color='black')),
    )

    # Add title and subtitle as additional traces
    if title:
        fig.add_trace(go.Scattermapbox(
            lat=[title_lat],
            lon=[title_lon],
            text=title,
            mode='text',
            showlegend=False,
            textfont=dict(size=20, color="white"),
        ))

    if subtitle:
        fig.add_trace(go.Scattermapbox(
            lat=[subtitle_lat],
            lon=[subtitle_lon],
            text=subtitle,
            mode='text',
            showlegend=False,
            textfont=dict(size=20, color="white"),
        ))

    # Update map layout to use OpenStreetMap
    fig.update_layout(
        mapbox_style="white-bg",
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                # "sourceattribution": "United States Geological Survey",
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
