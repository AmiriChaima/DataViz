import plotly.graph_objects as go
from plotly.subplots import make_subplots

def get_figure(df):
    """
    Generates a grid of violin plots for popularity distribution (V5).
    """
    features = [
        ('danceability_bin', 'Danceability'),
        ('acousticness_bin', 'Acousticness'),
        ('instrumentalness_bin', 'Instrumentalness'),
        ('mode_bin', 'Mode'),
        ('duration_bin', 'Duration'),
        ('tempo_bin', 'Tempo')
    ]
    
    fig = make_subplots(
        rows=2, cols=3,
        subplot_titles=[feat[1] for feat in features],
        vertical_spacing=0.12,
        horizontal_spacing=0.1
    )
    
    colors = ["#F27040", "#D3E87E", '#C13584']
    
    for i, (feature_col, feature_name) in enumerate(features):
        row = i // 3 + 1
        col = i % 3 + 1
        
        categories = df[feature_col].dropna().unique()
        
        for j, category in enumerate(categories):
            data = df[df[feature_col] == category]['track_popularity']
            
            fig.add_trace(
                go.Violin(
                    y=data,
                    name=str(category),
                    box_visible=True,
                    meanline_visible=True,
                    showlegend=False,
                    line_color=colors[j % len(colors)]
                ),
                row=row, col=col
            )
    
    fig.update_layout(
        title='Popularity Distribution Across Audio Feature Categories',
        font=dict(family="Segoe UI", size=12, color="#333"),
        height=800,
        plot_bgcolor="#f0f2f5",
        paper_bgcolor="white"
    )
    
    return fig
