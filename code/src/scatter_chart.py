
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def get_figure(df):
    """
    Generates a scatter plot showing Energy vs Valence with popularity as color and danceability as size.
    
    Args:
        df (pd.DataFrame): DataFrame with energy, valence, track_popularity, and danceability.
    
    Returns:
        plotly.graph_objs.Figure: A scatter plot figure object.
    """
    
    if len(df) > 5000:
        df_sample = df.sample(n=5000, random_state=42)
    else:
        df_sample = df
    
  
    fig = px.scatter(
        df_sample,
        x='energy',
        y='valence',
        color='track_popularity',
        size='danceability',
        hover_name='track_name',
        hover_data={
            'track_artist': True,
            'energy': ':.2f',
            'valence': ':.2f', 
            'track_popularity': True,
            'danceability': ':.2f'
        },
        labels={
            'energy': 'Energy',
            'valence': 'Valence', 
            'track_popularity': 'Popularity',
            'danceability': 'Danceability',
            'track_artist': 'Artist'
        },
        color_continuous_scale='Viridis',  
        size_max=15,
        opacity=0.7
    )
    
   
    fig.update_traces(
        hovertemplate='<b>%{hovertext}</b><br>' +
                     'Artist: %{customdata[0]}<br>' +
                     'Energy: %{x:.2f}<br>' +
                     'Valence: %{y:.2f}<br>' +
                     'Popularity: %{marker.color}<br>' +
                     'Danceability: %{marker.size:.2f}<br>' +
                     '<extra></extra>'
    )
    
    # Update layout
    fig.update_layout(
        title=dict(
            text="V4: Energy vs Valence (Bubble Size: Danceability, Color: Popularity)",
            x=0.5,
            font=dict(size=18, family="Segoe UI", color='#333333')
        ),
        xaxis=dict(
            title="Energy",
            showgrid=True,
            gridcolor='lightgray',
            gridwidth=1,
            range=[0, 1],
            tickformat='.1f'
        ),
        yaxis=dict(
            title="Valence", 
            showgrid=True,
            gridcolor='lightgray',
            gridwidth=1,
            range=[0, 1],
            tickformat='.1f'
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(
            family="Segoe UI",
            size=12,
            color="#333"
        ),
        coloraxis_colorbar=dict(
            title="Popularity",
            tickmode="linear",
            tick0=0,
            dtick=20
        ),
        height=600,
        margin=dict(l=60, r=100, t=80, b=60),
        hovermode='closest'
    )
    
    
    return fig 