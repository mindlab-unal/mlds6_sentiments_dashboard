import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# create a dataframe with three categories and 2 columns
df = pd.DataFrame({
    'category': ['a', 'a', 'a', 'b', 'b', 'b'],
    'x': [1, 2, 3, 1, 2, 3],
    'y': [4, 5, 6, 9, 8, 7]
    })

counts = df.groupby('category').agg({"x": "count"}).reset_index()

app = dash.Dash(__name__)
app.layout = html.Div(
        children=[
            html.H1("Sentiment Analysis Dashboard"),
            html.P("This dashboard is a simple example of sentiment analysis using the plotly express library."),
            html.Div(
                [
                    html.Div(
                        [
                            html.H2("Category"),
                            dcc.Dropdown(
                                id="dropdown",
                                options=[
                                    {'label': 'a', 'value': 'a'},
                                    {'label': 'b', 'value': 'b'},
                                    ],
                                value='category'
                                ),
                            html.H2("Age"),
                            dcc.Dropdown(
                                id="age",
                                options=[
                                    {'label': 'a', 'value': 'a'},
                                    {'label': 'b', 'value': 'b'},
                                    ],
                                value='age'
                                ),
                            ]
                        ),
                    html.Div(
                        [
                            dcc.Graph(
                                id='example-graph',
                                ),
                            ]
                        )
                    ],
                className = "twocolumns"
                )
            ]
        )

@app.callback(
    Output("example-graph", "figure"),
    [Input("dropdown", "value")]
    )
def update_figure(selected_dropdown_value: str):
    filtered_data = df.query("category == @selected_dropdown_value")
    fig = px.scatter(filtered_data, x="x", y="y")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
