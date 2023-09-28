from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import pickle
import dash_bootstrap_components as dbc
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

control = dbc.Card([
    html.Div(
        [
            dbc.Label("Crypto-Currency :-"),
            dcc.Dropdown({
                'BTC-USD.csv': 'BTC',
                'ETC-USD.csv': 'ETC',
                'CRO-USD.csv': 'CRO'
            },
                value="BTC-USD.csv", id="demo-dropdown"
            ),
            dbc.Label("Model"),
            dcc.Dropdown({
                'arima.pickle': 'ARIMA',
                'arma.pickle': 'ARMA',
                'bilstm_model_k_100_o_110_feature_1.h5': 'BILSTM Model predicting only closing price',
                'conv_bilstm_k_100_o_110_feature_1.h5': 'Conventional-BILSTM Model predicting only closing price',
                'conv_lstm_k_100_o_110_feature_1.h5': 'Conventional-LSTM Model predicting only closing price',
                'conv_model_k_100_o_110_feature_1.h5': 'Conventional Model predicting only closing price',
                'dense_k_100_o_110_feature_1.h5': 'Dense Model predicting only closing price',
                'lstm_bilstm_k_100_o_110_feature_1.h5': 'LSTM-BILSTM Model predicting only closing price',
                'lstm_model_k_100_o_110_feature_1.h5': 'LSTM Model predicting only closing price',
                'multi_step_dense_k_100_o_110_feature_1.h5': 'Multi Step Dense Model predicting only closing price',
                'bilstm_model_k_100_o_110_feature_4.h5': 'BILSTM Model predicting all four feature',
                'conv_bilstm_k_100_o_110_feature_4.h5': 'Conventional-BILSTM Model predicting all four feature',
                'conv_lstm_k_100_o_110_feature_4.h5': 'Conventional-LSTM Model predicting all four feature',
                'conv_model_k_100_o_110_feature_4.h5': 'Conventional Model predicting all four feature',
                'dense_k_100_o_110_feature_4.h5': 'Dense Model predicting all four feature',
                'lstm_bilstm_k_100_o_110_feature_4.h5': 'LSTM-BILSTM Model predicting all four feature',
                'lstm_model_k_100_o_110_feature_4.h5': 'LSTM Model predicting all four feature',
                'multi_step_dense_k_100_o_110_feature_4.h5': 'Multi Step Dense Model predicting all four feature',
            },
                value="arima.pickle", id="model", optionHeight=55,
            ),
        ]
    ),
    html.Br(),
    html.Div(
        [
            dbc.Label("Date :-"),
            html.Br(),
            dcc.DatePickerRange(id='demo-date', start_date='2018-09-17', end_date='2019-01-24')
        ]
    ),
    html.Div(id='dd-output-container'),
], body=True)

app.layout = dbc.Container(
    [
        html.H1("Cryptocurrency Chart"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(control, md=4),
                dbc.Col(dcc.Graph(id="finance"), md=8),
            ],
            align="center",
        ),
        dbc.Row(dcc.Graph(id="candle"), align='center')
    ],
    fluid=True,
)


@app.callback(
    [Output('dd-output-container', 'children'), Output('finance', 'figure'), Output('candle', 'figure')],
    [Input('demo-dropdown', 'value'), Input('demo-date', 'start_date'), Input('demo-date', 'end_date'),Input('model','value')]
)
def update_output(value, start_date, end_date,model):
    pass


if __name__ == '__main__':
    app.run_server(debug=True)
