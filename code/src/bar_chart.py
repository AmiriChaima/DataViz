import plotly.express as px
from constaints import GENRE_COLORS


def get_figure(df):
    
    """Generates a bar chart showing the average track popularity by playlist genre."""
    
    fig = px.bar(
        df,
        x="Genre",
        y="Average Popularity",
        color="Genre",
        color_discrete_map=GENRE_COLORS,
        hover_data={'Average Popularity': False, 'Genre': False}, 
        title="Average Track Popularity by Playlist Genre"
    )

    fig.update_traces(
        hovertemplate='<b>Genre:</b> %{x}<br><b>Average Popularity:</b> %{y:.1f}<extra></extra>',
        marker_line_color='black',
        marker_line_width=1,
        selected=dict(marker=dict(opacity=1)),
        unselected=dict(marker=dict(opacity=0.4))
    )

    fig.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size=14,
            font_family="Segoe UI",
            font_color="#333",
            bordercolor="#cccccc"
        ),
        clickmode='event+select',
        xaxis_title="Playlist Genre",
        yaxis_title="Average Popularity",
        yaxis=dict(range=[0, 50], gridcolor='#e0e0e0'),
        showlegend=False,
        plot_bgcolor="#f0f2f5",
        paper_bgcolor="white",
        font=dict(family="Segoe UI", size=14, color="#333"),
        title=dict(x=0.5, font=dict(size=20))
    )

    return fig
