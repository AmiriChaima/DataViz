
import plotly.graph_objects as go
import numpy as np

def get_figure(df):
    """
    Generates an interactive radar chart of average audio feature profiles by genre.
    
    Args:
        df (pd.DataFrame): DataFrame with genres and their average audio features.
    
    Returns:
        plotly.graph_objs.Figure: A radar chart figure object.
    """
    

    features = ['energy', 'valence', 'danceability', 'acousticness', 'speechiness']
    
  
    colors = {
        'pop': '#FF1744',      # Bright red
        'rap': '#00E676',      # Bright green
        'rock': '#2196F3',     # Bright blue
        'latin': '#FF9800',    # Bright orange
        'edm': '#9C27B0'       # Bright purple
    }
    
    fig = go.Figure()
    
    # Add a trace for each genre
    for _, row in df.iterrows():
        genre = row['Genre'].lower()
        values = [row[feature] for feature in features]
        
        # Close the radar chart by adding the first value at the end
        values += values[:1]
        feature_labels = features + [features[0]]
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=feature_labels,
            fill='toself',
            name=row['Genre'].title(),
            line=dict(color=colors.get(genre, '#FF1744'), width=3),
            fillcolor=colors.get(genre, '#FF1744'),
            opacity=0.3,
            marker=dict(size=8, color=colors.get(genre, '#FF1744')),
            hovertemplate='<b>%{fullData.name}</b><br>' +
                         '%{theta}: %{r:.2f}<br>' +
                         '<extra></extra>'
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1],
                tickvals=[0.2, 0.4, 0.6, 0.8, 1.0],
                ticktext=['0.2', '0.4', '0.6', '0.8', '1.0'],
                gridcolor='#CCCCCC',
                gridwidth=2,
                linecolor='#999999',
                linewidth=2
            ),
            angularaxis=dict(
                tickfont=dict(size=14, color='#333333'),
                gridcolor='#CCCCCC',
                gridwidth=2,
                linecolor='#999999',
                linewidth=2
            ),
            bgcolor='rgba(248,249,250,0.5)'
        ),
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="top",
            y=1,
            xanchor="left",
            x=1.05,
            font=dict(size=14, color='#333333'),
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#CCCCCC',
            borderwidth=1
        ),
        title=dict(
            text="Average Audio Feature Profile by Genre (Radar Chart)",
            x=0.5,
            font=dict(size=20, family="Segoe UI", color='#333333')
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(
            family="Segoe UI",
            size=12,
            color="#333"
        ),
        margin=dict(l=80, r=120, t=80, b=80)
    )
    
    return fig 