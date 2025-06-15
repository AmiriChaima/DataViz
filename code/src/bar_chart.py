import plotly.express as px

def get_figure(df):
    """
    Generates an interactive bar chart of average track popularity by playlist genre.

    Returns:
        plotly.graph_objs.Figure: A bar chart figure object.
    """
    
    fig = px.bar(
        df,
        x="Genre",
        y="Average Popularity",
        color="Genre",
        color_discrete_sequence=["#FFA500"] * len(df),
        hover_data={'Average Popularity': True, 'Genre': True},
        title="Average Track Popularity by Playlist Genre"
    )

    fig.update_traces(
        hovertemplate='%{x}<br>%{y:.1f}<extra></extra>',
        marker_line_color='black',
        marker_line_width=1,
        selected=dict(marker=dict(opacity=1)),
        unselected=dict(marker=dict(opacity=0.4))
    )

    fig.update_layout(
        clickmode='event+select',
        xaxis_title="Playlist Genre",
        yaxis_title="Average Popularity",
        yaxis=dict(range=[0, 50]),
        showlegend=False,
        plot_bgcolor="#f0f2f5",
        paper_bgcolor="white",
        font=dict(
            family="Segoe UI",
            size=14,
            color="#333"
        ),
        title=dict(
            x=0.5,
            font=dict(size=20)
        )
    )

    return fig
