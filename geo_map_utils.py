import plotly.express as px
import plotly.graph_objects as go


def create_geo_map_image(df, title, subtitle, color_prop, title_lat=66, title_lon=10, subtitle_lat=32, subtitle_lon=10,):
    # Create the bubble map
    fig = px.scatter_geo(df,
                         lat='lat',
                         lon='lon',
                         text='text',
                         size=color_prop,
                         color=color_prop,
                         color_continuous_scale=[
                             "gray",
                             "white",
                         ],
                         )

    # Update layout for better visualization
    fig.update_traces(textposition='top center',
                      textfont=dict(size=8, color='white'),
                      marker=dict(line=dict(width=1, color='black')))

    if title:
        fig.add_trace(go.Scattergeo(
            lat=[title_lat],
            lon=[title_lon],
            textposition='bottom center',
            text=title,
            mode='text',
            showlegend=False,
            textfont=dict(size=20, color="white"),
        ))

    if subtitle:
        fig.add_trace(go.Scattergeo(
            lat=[subtitle_lat],
            lon=[subtitle_lon],
            textposition='top center',
            text=subtitle,
            mode='text',
            showlegend=False,
            textfont=dict(size=10, color="white"),
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
