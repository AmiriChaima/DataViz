import plotly.graph_objects as go
import plotly.express as px
from constaints import GENRE_COLORS

def get_figure(df, selected_genres=None):
    
    """Generates a stacked area chart showing the distribution of genres over time."""
    
    if selected_genres is not None:
        df = df[df['Genre'].isin(selected_genres)]
    
    pivot_df = df.pivot(index='year', columns='Genre', values='count').fillna(0)
    
    fig = go.Figure()

    for genre in pivot_df.columns:
        fig.add_trace(go.Scatter(
            x=pivot_df.index,
            y=pivot_df[genre],
            mode='lines',
            stackgroup='one',
            name=genre,
            line=dict(width=2, color=GENRE_COLORS.get(genre.lower(), '#17becf'))
        ))

    fig.update_layout(
        title='Genre Distribution Over Time',
        xaxis_title='Release Year',
        yaxis_title='Number of Songs',
        legend=dict(title='Genre', font=dict(size=14)),
        font=dict(family="Segoe UI, Lato, Arial", size=16, color="#222"),
        hovermode='x unified',
        plot_bgcolor="#f8f9fa",
        paper_bgcolor="white",
        margin=dict(l=60, r=30, t=60, b=60),
        xaxis=dict(
            rangeselector=dict(
                buttons=[
                    dict(count=10, label="Last 10Y", step="year", stepmode="backward"),
                    dict(count=20, label="Last 20Y", step="year", stepmode="backward"),
                    dict(step="all", label="All Data")
                ],
                bgcolor='#FFFFFF',
                activecolor='#1DB954',
                font=dict(size=14)
            ),
            rangeslider=dict(visible=True),
            type="date"
        )
    )

    return fig
