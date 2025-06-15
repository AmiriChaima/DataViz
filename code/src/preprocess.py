def bar_chart_df(df):
    """
    Computes average popularity per playlist genre from a raw dataframe.

    Args:
        df (pd.DataFrame): Raw Spotify data containing 'playlist_genre' and 'track_popularity'.

    Returns:
        pd.DataFrame: DataFrame with 'Genre' and 'Average Popularity' columns.
    """
    return (
        df.groupby('playlist_genre')['track_popularity']
        .mean()
        .reset_index()
        .rename(columns={'playlist_genre': 'Genre', 'track_popularity': 'Average Popularity'})
        .sort_values(by='Average Popularity', ascending=False)
    )
