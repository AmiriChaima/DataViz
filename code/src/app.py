# -*- coding: utf-8 -*-
"""
    File name: app.py
    Description: Entry point for the Dash application.
    Author: YOUR_NAME
    Python Version: 3.10+
"""

import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd

import preprocess
import bar_chart

app = dash.Dash(__name__)
app.title = 'Playlist Popularity Dashboard'

raw_df = pd.read_csv('./assets/spotify_songs.csv')

app.layout = html.Div(className='container', children=[
    html.Header(children=[
        html.H1("Average Track Popularity by Playlist Genre"),
        html.H2("Which kind of playlist produces the most highly popular songs?")
    ]),

    html.Main(children=[
        html.Div(className='graph-section', children=[
            dcc.Graph(
                id='graph-1',
                figure=bar_chart.get_figure(preprocess.bar_chart_df(raw_df)),
                config={'displayModeBar': False}
            ),
        ]),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
