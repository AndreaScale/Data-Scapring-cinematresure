import plotly.graph_objects as go
import pandas as pd

df = pd.read_html('coord.html')

fig = go.Figure(data=go.Scattergeo(
        lon = df[0]['Lng'],
        lat = df[0]['Lat'],
        text = df[0]['Movie theater'],
        mode = 'markers',
        ))

fig.update_layout(
        title = 'Movie theater in 1947 USA',
        geo_scope='usa',
    )
fig.show()
