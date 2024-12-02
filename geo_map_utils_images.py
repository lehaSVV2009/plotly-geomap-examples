import base64
import plotly.express as px
import plotly.graph_objects as go

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
        opacity=0,
        zoom=3.3,
    )

    # Update traces for marker appearance
    fig.update_traces(
        textposition='middle right',
        textfont=dict(size=15, color='white', weight="bold"),
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

        # Read the image file and encode it to base64
    with open('football/cup.png', 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    # Adjust image coordinates based on latitude
    def adjust_coordinates(lat, lon):
        lat_adjustment = 1.25 * (1 - abs(lat) / 90)
        return [
            [lon - 1, lat + lat_adjustment],
            [lon + 1, lat + lat_adjustment],
            [lon + 1, lat - lat_adjustment],
            [lon - 1, lat - lat_adjustment]
        ]

    fig.update_layout(
        mapbox_style="white-bg",
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                "source": [
                    "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                ]
            },
            *[
                {
                    "below": 'traces',
                    "sourcetype": "image",
                    "source": f"data:image/png;base64,{encoded_image}",
                    "coordinates": adjust_coordinates(row['lat'], row['lon']),
                } for _, row in df.iterrows()
            ]
        ],
        margin={"r": 0, "t": 0, "l": 0, "b": 0},  # Remove margins
    )
    # Show the plot
    fig.show()
