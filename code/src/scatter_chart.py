import plotly.express as px
from constaints import GENRE_COLORS


def get_figure(df):
    """
    Generates a scatter plot showing Energy vs Valence with genre color and danceability size.
    """

    fig = px.scatter(
        df,
        x='energy',
        y='valence',
        color='playlist_genre',
        size='danceability',
        color_discrete_map=GENRE_COLORS,
        hover_name='track_name',
        hover_data={
            'track_artist': True,
            'energy': ':.2f',
            'valence': ':.2f',
            'track_popularity': True,
            'danceability': ':.2f'
        },
        labels={
            'playlist_genre': 'Genre',
            'track_popularity': 'Popularity',
            'danceability': 'Danceability'
        },
        size_max=15,
        opacity=0.7
    )

    fig.update_traces(
        hovertemplate='<b>%{hovertext}</b><br>' +
                      'Artist: %{customdata[0]}<br>' +
                      'Energy: %{x:.2f}<br>' +
                      'Valence: %{y:.2f}<br>' +
                      'Popularity: %{customdata[1]}<br>' +
                      '<extra></extra>'
    )

    fig.update_layout(
        title=dict(
            text="V4: Energy vs Valence (Color: Genre, Size: Danceability)",
            x=0.5,
            font=dict(size=18, family="Segoe UI", color='#333333')
        ),
        xaxis=dict(title="Energy", range=[0, 1], showgrid=True, gridcolor='lightgray'),
        yaxis=dict(title="Valence", range=[0, 1], showgrid=True, gridcolor='lightgray'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family="Segoe UI", size=14, color="#333"),
        height=600,
        margin=dict(l=60, r=100, t=80, b=60),
        hovermode='closest'
    )

    return fig
