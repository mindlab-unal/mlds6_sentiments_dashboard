import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# create a dataframe with three categories and 2 columns
df = pd.DataFrame({
    'category': ['a', 'a', 'a', 'b', 'b', 'b'],
    'x': [1, 2, 3, 1, 2, 3],
    'y': [4, 5, 6, 7, 8, 9]
    })

counts = df.groupby('category').agg({"x": "count"}).reset_index()

fig = px.bar(counts, x="category", y="x")

app = dash.Dash(__name__)
app.layout = html.Div(
        children=[
            html.H1("Sentiment Analysis Dashboard"),
            html.P("This dashboard is a simple example of sentiment analysis using the plotly express library."),
            html.H2("First section"),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': 'Montreal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
                ],
                value='MTL'
            ),
            dcc.Graph(
                id='example-graph',
                figure=fig
            ),
            ]
        )

if __name__ == '__main__':
    app.run_server(debug=True)
