import plotly.express as px
from constaints import GENRE_COLORS as color_mapping

def get_figure(df, feature='track_popularity'):
    
    """Generates a line chart showing the evolution of a feature 
    ('track_popularity', 'danceability', 'energy', 'valence', 'acousticness', 'speechiness') over time by genre."""
    
    fig = px.line(
        df,
        x='release_year',
        y=feature,
        color='playlist_genre',
        line_shape='spline',
        markers=True,
        title=f"{feature.replace('_', ' ').title()} Evolution Over Time by Genre",
        labels={
            'release_year': 'Release Year',
            feature: feature.replace('_', ' ').title(),
            'playlist_genre': 'Genre'
        },
        color_discrete_map=color_mapping
    )

    fig.update_layout(
        font=dict(family="Segoe UI, Lato, Arial", size=16, color="#222"),
        title=dict(x=0.5, font=dict(size=22)),
        legend=dict(title='Genre', font=dict(size=14)),
        xaxis=dict(title='Year', tickfont=dict(size=14)),
        yaxis=dict(title=feature.replace('_', ' ').title(), tickfont=dict(size=14)),
        hovermode='x unified',
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="white",
        margin=dict(l=60, r=30, t=60, b=60)
    )

    return fig
