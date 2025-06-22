import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output
import pandas as pd

import preprocess
import bar_chart
import radar_chart
import line_chart
import area_chart
import scatter_chart
import violin_plots
from constaints import GENRE_COLORS 

# --- Load and preprocess data ---
raw_df = pd.read_csv('./assets/spotify_songs.csv')
bar_df = preprocess.bar_chart_df(raw_df)
line_chart_df = preprocess.line_chart_df(raw_df)
stacked_df = preprocess.area_chart_df(raw_df)
radar_df = preprocess.radar_chart_df(raw_df)
scatter_df = preprocess.scatter_chart_df(raw_df)
violin_df = preprocess.violin_plots_df(raw_df)

all_features = ['track_popularity', 'danceability', 'energy', 'valence', 'acousticness', 'speechiness']
all_genres = ['pop', 'rap', 'rock', 'r&b', 'latin', 'edm']

CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "minHeight": "100vh",
}

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "white",
    "border-right": "1px solid #e6e6e6",
    "box-shadow": "2px 0 5px rgba(0,0,0,0.05)",
    "zIndex": 1000
}

sidebar = html.Div([
    html.H2("🎵 Spotify Trends", className="display-6", style={"color": "#07110B"}),
    html.Hr(),
    dbc.Nav([
        dbc.NavLink("Overview", href="/", active="exact"),
        dbc.NavLink("Line Chart", href="/line-chart", active="exact"),
        dbc.NavLink("Stacked Area", href="/stacked", active="exact"),
        dbc.NavLink("Radar Chart", href="/radar", active="exact"),
        dbc.NavLink("Scatter Plot", href="/scatter", active="exact"),
        dbc.NavLink("Violin Plots", href="/violin", active="exact"),
        dbc.NavLink("Bar Chart", href="/bar", active="exact"),
    ], vertical=True, pills=True)
], style=SIDEBAR_STYLE)

content = html.Div(id="page-content", style=CONTENT_STYLE)

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://use.fontawesome.com/releases/v5.15.4/css/all.css"
]

# --- Initialize app ---
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
app.title = "Exploration of Music Trends on Spotify"

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


# --- Layout rendering based on page ---
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div([
            html.H1(" Project Overview", style={"color": "#040E08", "fontSize": "36px", "marginBottom": "20px"}),
            html.H2("🎯 Objective", style={"color": "#1DB954", "fontSize": "28px", "marginTop": "30px"}),
            html.P("Build an interactive data visualization platform that investigates how different musical features relate to a song’s popularity, with a focus on genre and subgenre, uncovering patterns and correlations between audio attributes and popularity.", style={'margin': '10px 40px', 'fontSize': '18px'}),
            html.H2("👥 Target Audience", style={"color": "#1DB954", "fontSize": "28px", "marginTop": "30px"}),
            html.Ul([
                html.Li("🎶 Music industry professionals (producers, marketers, emerging artists)", style={'fontSize': '18px'}),
                html.Li("📊 Data visualization enthusiasts and analysts", style={'fontSize': '18px'}),
                html.Li("🎓 Students and music lovers", style={'fontSize': '18px'}),
            ], style={'marginLeft': '50px'}),
            html.H2("📊 Dataset Summary", style={"color": "#1DB954", "fontSize": "28px", "marginTop": "30px"}),
            html.Div([
                html.Div([
                    html.Div("🎵", style={'fontSize': '40px'}),
                    html.H3("Tracks", style={'color': '#333', 'marginTop': '10px'}),
                    html.H4("~30,000", style={'color': '#1DB954', 'fontSize': '28px'})
                ], style={'width': '180px', 'display': 'inline-block', 'textAlign': 'center', 'backgroundColor': 'white', 'border': '1px solid #e0e0e0', 'borderRadius': '12px', 'boxShadow': '2px 2px 6px rgba(0,0,0,0.1)', 'padding': '20px', 'margin': '15px'}),
                html.Div([
                    html.Div("🎤", style={'fontSize': '40px'}),
                    html.H3("Unique Artists", style={'color': '#333', 'marginTop': '10px'}),
                    html.H4("10,693", style={'color': '#1DB954', 'fontSize': '28px'})
                ], style={'width': '180px', 'display': 'inline-block', 'textAlign': 'center', 'backgroundColor': 'white', 'border': '1px solid #e0e0e0', 'borderRadius': '12px', 'boxShadow': '2px 2px 6px rgba(0,0,0,0.1)', 'padding': '20px', 'margin': '15px'}),
                html.Div([
                    html.Div("🎼", style={'fontSize': '40px'}),
                    html.H3("Genres", style={'color': '#333', 'marginTop': '10px'}),
                    html.H4("6 Genres", style={'color': '#1DB954', 'fontSize': '28px'}),
                    html.P("Pop, Rap, R&B, Rock, Latin, EDM", style={'fontSize': '14px', 'color': '#777', 'marginTop': '5px'})
                ], style={'width': '200px', 'display': 'inline-block', 'textAlign': 'center', 'backgroundColor': 'white', 'border': '1px solid #e0e0e0', 'borderRadius': '12px', 'boxShadow': '2px 2px 6px rgba(0,0,0,0.1)', 'padding': '20px', 'margin': '15px'}),
                html.Div([
                    html.Div("📄", style={'fontSize': '40px'}),
                    html.H3("Variables", style={'color': '#333', 'marginTop': '10px'}),
                    html.H4("23", style={'color': '#1DB954', 'fontSize': '28px'}),
                    html.P("Metadata + Audio Features", style={'fontSize': '14px', 'color': '#777', 'marginTop': '5px'})
                ], style={'width': '200px', 'display': 'inline-block', 'textAlign': 'center', 'backgroundColor': 'white', 'border': '1px solid #e0e0e0', 'borderRadius': '12px', 'boxShadow': '2px 2px 6px rgba(0,0,0,0.1)', 'padding': '20px', 'margin': '15px'}),
                html.Div([
                    html.Div("📅", style={'fontSize': '40px'}),
                    html.H3("Temporal Coverage", style={'color': '#333', 'marginTop': '10px'}),
                    html.H4("1960s - 2020s", style={'color': '#1DB954', 'fontSize': '28px'})
                ], style={'width': '220px', 'display': 'inline-block', 'textAlign': 'center', 'backgroundColor': 'white', 'border': '1px solid #e0e0e0', 'borderRadius': '12px', 'boxShadow': '2px 2px 6px rgba(0,0,0,0.1)', 'padding': '20px', 'margin': '15px'}),
            ], style={'textAlign': 'center'}),
            html.H2("📌 Target Questions & Visualizations", style={"color": "#1DB954", "fontSize": "28px", "marginTop": "40px"}),
            html.Ul([
                html.Li("🟢 V1 - Multi-line time series chart: How do musical features evolve over time?", style={'fontSize': '18px'}),
                html.Li("🟢 V2 - Stacked Area: Release date distribution across genres", style={'fontSize': '18px'}),
                html.Li("🟢 V3 - Radar Chart: Audio feature patterns by genre", style={'fontSize': '18px'}),
                html.Li("🟢 V4 - Scatter Plot: Feature combinations vs popularity", style={'fontSize': '18px'}),
                html.Li("🟢 V5 - Violin Plots: How features correlate with popularity", style={'fontSize': '18px'}),
                html.Li("🟢 V6 - Bar Chart: Which genres contain the most popular songs", style={'fontSize': '18px'}),
            ], style={'marginLeft': '50px'})
        ])
    elif pathname == "/line-chart":
        return html.Div([
            html.H1("Temporal Trends: Feature Evolution by Genre", style={"color": "#1DB954"}),
            html.P("This visualization represents a multi-line time series chart, it aims at analyzing the temporal trends. It shows how musical features (e.g. popularity, energy, danceability, valence, instrumentalness) evolve over time across different genres (e.g pop, latin, rap, r&b). The X-axis represents years, the Y-axis represents the selected feature value, and each genre is represented by a distinct colored line. Users can choose the feature they want to examine through a dropdown menu and filter genres. This format enables viewers to simultaneously track trends across multiple genres, making it simple to compare patterns and notice changes in musical trends over a period.", style={'margin': '20px 40px', 'font-size': '18px'}),
            html.Div([
                html.P("Select different features and genres to see how musical characteristics evolve over time.", style={"color": "#535353", "marginTop": "1em"}),
                html.Label("Select feature:", style={'fontWeight': 'bold', 'marginRight': '1em'}),
                dcc.Dropdown(
                    id='feature-dropdown',
                    options=[{'label': f.replace('_', ' ').title(), 'value': f} for f in all_features],
                    value='track_popularity',
                    clearable=False,
                    style={'width': '250px', 'display': 'inline-block'}
                ),
                html.Label("Select genres:", style={'fontWeight': 'bold', 'marginLeft': '2em', 'marginRight': '1em'}),
                dcc.Dropdown(
                    id='genre-dropdown',
                    options=[{'label': g.title(), 'value': g} for g in all_genres],
                    value=all_genres,
                    multi=True,
                    style={'width': '350px', 'display': 'inline-block'}
                ),
            ], style={'marginBottom': '1em'}),
            dcc.Graph(id='temporal-graph', config={'displayModeBar': False}),
        ])
    elif pathname == "/bar":
        return html.Div(className='graph-section', children=[
            html.H1("Average Track Popularity by Playlist Genre", style={"color": "#1DB954"}),
            html.P("This bar chart compares the average popularity of songs across different playlist genres such as pop, hip hop, EDM, rock, and others. Each bar represents the mean popularity score for a genre, highlighting which types of playlists tend to include more widely streamed songs. Pop and hip hop lead with higher average popularity, while genres like folk or metal show lower averages, reflecting more niche audiences. Interactive hover tooltips display exact popularity values, and filters allow focusing on specific genres or subgenres for deeper comparisons.", style={'margin': '20px 40px', 'font-size': '18px'}),
            dcc.Graph(
                id='bar-graph',
                figure=bar_chart.get_figure(bar_df),
                config={'displayModeBar': False}
            ),
        ])
    elif pathname == "/stacked":
        return html.Div([
            html.H1("Genre Distribution Over Time", style={"color": "#1DB954"}),
            html.P("This visualization uses a stacked area chart to show the number of songs released over time, sorted by genre. Each colored zone reflects a distinct genre (e.g., Rock, Rap, Pop, etc.), allowing users to observe the evolution of each genre's contribution. Stacked area charts highlight both the total number of song releases and the shifting prominence of genres across decades. This format allows for clear comparisons of how various musical styles have changed, emerged, or declined over time. Interactive filters enable users to focus on specific genres and examine precise release counts.", style={'margin': '20px 40px', 'font-size': '18px'}),
            html.P("Filter genre to see how genre representation changes over the years.", style={"color": "#535353", "marginTop": "1em"}),
            html.Label("Filter genres:", style={'fontWeight': 'bold', 'marginRight': '1em'}),
            dcc.Dropdown(
                id='stacked-genre-dropdown',
                options=[{'label': g.title(), 'value': g} for g in all_genres],
                value=all_genres,
                multi=True,
                style={'width': '400px', 'marginBottom': '1em'}
            ),
            dcc.Graph(id='stacked-graph', config={'displayModeBar': False})
        ])
    elif pathname == "/radar":
        return html.Div(className='radar-chart-container', children=[
            html.H1("Average Audio Feature Profile by Genre", style={"color": "#1DB954"}),
            html.P("This radar chart compares genres across five core audio features: danceability, energy, valence, acousticness, and speechiness. Each genre forms a unique polygon, highlighting its distinctive audio profile. For example, EDM peaks on energy, Rap on speechiness, and Rock on acousticness. The radar format allows users to easily identify which genres dominate extreme moods, and how genres differ in acoustic or electronic emphasis. Interactive tooltips and genre toggles enable detailed examination of individual genre fingerprints while preserving overall comparisons.", style={'margin': '20px 40px', 'font-size': '18px'}),
            html.P("Select genres to compare their audio feature profiles:", style={"color": "#535353", "marginTop": "1em"}),
            html.Label("Select genres:", style={'fontWeight': 'bold', 'marginRight': '1em'}),
            dcc.Dropdown(
                id='radar-genre-dropdown',
                options=[{'label': g.title(), 'value': g} for g in all_genres],
                value=all_genres,
                multi=True,
                style={'width': '400px', 'marginBottom': '1em'}
            ),
            dcc.Graph(id='radar-chart', config={'displayModeBar': False}),
        ])
    
    
    elif pathname == "/scatter":
        return html.Div(className='graph-section', children=[
        html.H1("Energy vs Valence Feature Combinations", style={"color": "#1DB954"}),
        html.P(""" This scatter plot explores how combinations of energy and valence relate to song characteristics across different genres.
Each point represents a song, with energy on the x-axis and valence on the y-axis.
The color of each point reflects its genre, while the size indicates danceability.
Use the dropdown to filter by genre, and the range slider to explore songs within a specific popularity range. 
The Song Popularity range is between 0 and 100, where higher values indicate greater popularity
        
        """, style={'margin': '20px 40px', 'font-size': '18px'}),
        
        html.P("Filter genre to explore how different musical styles relate to energy and valence", style={"color": "#535353", "marginTop": "1em"}),
        html.Label("Filter by Genre:", style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='scatter-genre-dropdown',
            options=[{'label': g.title(), 'value': g} for g in all_genres],
            value=all_genres,
            multi=True,
            style={'width': '400px', 'marginBottom': '1em'}
        ),
        
        html.P("Adjust the popularity range to focus on songs with specific levels of audience appeal.", style={"color": "#535353", "marginTop": "1em"}),
        html.Label("Filter by Popularity Range:", style={'fontWeight': 'bold'}),
        dcc.RangeSlider(
            id='popularity-slider',
            min=0,
            max=100,
            step=1,
            value=[20, 80],
            marks={i: str(i) for i in range(0, 101, 20)},
            tooltip={"placement": "bottom", "always_visible": True},
            allowCross=False,
            className='mb-4'
        ),

        dcc.Graph(
            id='scatter-chart',
            config={'displayModeBar': False}
        ),
    ])


    elif pathname == "/violin":
        return html.Div([
            html.H1("Popularity Distribution by Audio Features", style={"color": "#1DB954"}),
            html.P("This grid of violin plots examines how song popularity varies across key audio features: danceability, acousticness, instrumentalness, mode, duration, and tempo. Each violin shows the full distribution of popularity scores for different bins of the feature. The plots reveal, for example, that highly danceable songs tend to concentrate in higher popularity ranges, while instrumental tracks are much less likely to achieve high popularity. Mode (major/minor) has minimal impact, while shorter durations and medium-fast tempos often correlate with better popularity. Interactive hovers, bin toggles, and zooming allow users to explore density shifts across these dimensions.", style={'margin': '20px 40px', 'font-size': '18px'}),
            html.P("These violin plots show how track popularity is distributed across different audio feature categories.", style={"color": "#535353", "marginTop": "1em"}),
            dcc.Graph(id='violin-graph', figure=violin_plots.get_figure(violin_df), config={'displayModeBar': False}),
        ])
    return html.Div([
        html.H1("404: Not found", className="text-danger"),
        html.Hr(),
        html.P("The pathname was not recognised...", style={"color": "#b3b3b3"}),
    ])






# --- Callbacks ---
@app.callback(
    Output('temporal-graph', 'figure'),
    [Input('feature-dropdown', 'value'), Input('genre-dropdown', 'value')]
)
def update_temporal(feature, genres):
    filtered = line_chart_df[line_chart_df['playlist_genre'].isin(genres)]
    return line_chart.get_figure(filtered, feature)

@app.callback(
    Output('stacked-graph', 'figure'),
    Input('stacked-genre-dropdown', 'value')
)
def update_stacked(selected_genres):
    return area_chart.get_figure(stacked_df, selected_genres)

@app.callback(
    Output('radar-chart', 'figure'),
    Input('radar-genre-dropdown', 'value')
)
def update_radar(selected_genres):
    filtered_radar_df = radar_df[radar_df['Genre'].isin(selected_genres)]
    return radar_chart.get_figure(filtered_radar_df)


@app.callback(
    Output('scatter-chart', 'figure'),
    [Input('scatter-genre-dropdown', 'value'),
     Input('popularity-slider', 'value')]
)
def update_scatter(selected_genres, popularity_range):
    filtered = scatter_df[
        (scatter_df['playlist_genre'].isin(selected_genres)) &
        (scatter_df['track_popularity'] >= popularity_range[0]) &
        (scatter_df['track_popularity'] <= popularity_range[1])
    ]
    return scatter_chart.get_figure(filtered)



# --- Run app ---
if __name__ == '__main__':
    app.run_server(debug=True)

# For gunicorn deployment
server = app.server
