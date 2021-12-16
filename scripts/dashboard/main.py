import dash
import pandas as pd
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go
from mlds6sentiment.environment.base import get_data_paths
from mlds6sentiment.database.io import load_model
from mlds6sentiment.preprocessing.reviews import preprocess_pipe

app = dash.Dash(__name__)
data_paths = get_data_paths()
model_evaluation = load_model(data_paths.models, "evaluation.joblib")
model_confidence = load_model(data_paths.models, "confidence.joblib")

app.layout = html.Div(
        [
            html.H1("Papers Reviews Analysis"),
            html.Div(
                [
                    html.Div(
                        [
                            html.H2("Ingrese su review"),
                            dcc.Input(id="input-text", type="text", placeholder="Este paper está muy malo"),
                            ]
                        ),
                    html.Div(
                        [
                            html.H2("Predicción de evaluación"),
                            dcc.Graph(
                                id="graph-evaluation"
                                ),
                            html.H2("Predicción de confianza"),
                            dcc.Graph(
                                id="graph-confianza"
                                ),
                            ]
                        )
                    ],
                className="twocolumns",
                )
            ]
        )

@app.callback(
        Output("graph-evaluation", "figure"),
        [Input("input-text", "value")]
        )
def update_graph_evaluation(text: str) -> go.Figure:
    if text is None:
        return go.Figure()
    data = pd.DataFrame(
            {
                "id": [1],
                "paper_id": [1],
                "text": [text],
                "timespan": [ "2020-01-01" ],
                "lan": [ "es" ],
                "confidence": [0],
                "evaluation": [0],
                "remarks": [""],
                "orientation": [""]
                },
            )
    preprocessed_data = preprocess_pipe(data)
    evaluation_probs = model_evaluation.predict_proba(preprocessed_data)
    evaluation_prediction = model_evaluation.predict(preprocessed_data)
    labels = ["Rechazado", "Aceptado"]
    fig = px.bar(
            x=labels,
            y=evaluation_probs[0],
            )
    fig.update_layout(
            {
                "title": f"Probablemente será {labels[evaluation_prediction[0]]}",
                "xaxis_title": "Evaluación",
                "yaxis_title": "Probabilidad"
                })
    return fig

@app.callback(
        Output("graph-confianza", "figure"),
        [Input("input-text", "value")]
        )
def update_graph_confidence(text: str) -> go.Figure:
    if text is None:
        return go.Figure()
    data = pd.DataFrame(
            {
                "id": [1],
                "paper_id": [1],
                "text": [text],
                "timespan": [ "2020-01-01" ],
                "lan": [ "es" ],
                "confidence": [0],
                "evaluation": [0],
                "remarks": [""],
                "orientation": [""]
                },
            )
    preprocessed_data = preprocess_pipe(data)
    confidence_probs = model_confidence.predict_proba(preprocessed_data)
    confidence_prediction = model_confidence.predict(preprocessed_data)
    labels = ["No experto", "Experto"]
    fig = px.bar(
            x=labels,
            y=confidence_probs[0],
            )
    fig.update_layout(
            {
                "title": f"Probablemente es un {labels[confidence_prediction[0]]}",
                "xaxis_title": "Confianza",
                "yaxis_title": "Probabilidad"
                })
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
