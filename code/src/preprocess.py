import pandas as pd
import numpy as np

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


def line_chart_df(df):
    """
    Prepares data for temporal analysis (V1).
    Groups data by year and genre for time series analysis.
    """
   
    df['release_year'] = pd.to_datetime(df['track_album_release_date'], errors='coerce').dt.year
    df = df.dropna(subset=['release_year'])
    
    
    features = ['track_popularity', 'danceability', 'energy', 'valence', 'acousticness', 'speechiness']
    
    result = df.groupby(['release_year', 'playlist_genre'])[features].mean().reset_index()
    return result


def area_chart_df(df):
    """
    Computes song count per year and genre for area chart visualization.
    Args:
        df (pd.DataFrame): Raw Spotify data containing release dates and genres.
    Returns:
        pd.DataFrame: DataFrame with 'year', 'Genre', and 'count' columns.
    """
    df_copy = df.copy()
    df_copy['year'] = df_copy['track_album_release_date'].str[:4].astype(int)
    df_copy['year'] = pd.to_datetime(df_copy['track_album_release_date'].str[:4], format='%Y')
    

    area_df = (
        df_copy.groupby(['year', 'playlist_genre'])
        .size()
        .reset_index(name='count')
        .rename(columns={'playlist_genre': 'Genre'})
    )
    
    return area_df

def radar_chart_df(df):
    """
    Computes average audio features per playlist genre for radar chart visualization.
    Args:
        df (pd.DataFrame): Raw Spotify data containing playlist genres and audio features.
    Returns:
        pd.DataFrame: DataFrame with 'Genre' and average audio feature columns.
    """
    audio_features = ['energy', 'valence', 'danceability', 'acousticness', 'speechiness']
    radar_df = (
        df.groupby('playlist_genre')[audio_features]
        .mean()
        .reset_index()
        .rename(columns={'playlist_genre': 'Genre'})
    )
    
    
    return radar_df



# def scatter_chart_df(df):
#     """
#     Prepares data for Energy vs Valence scatter plot with popularity and danceability.

#     Args:
#         df (pd.DataFrame): Raw Spotify data containing energy, valence, track_popularity, danceability, and track info.

#     Returns:
#         pd.DataFrame: DataFrame with energy, valence, track_popularity, danceability, and track information.
#     """
   
#     scatter_df = df[['energy', 'valence', 'track_popularity', 'danceability', 
#                     'track_name', 'track_artist']].dropna()
    
  
#     scatter_df = scatter_df[
#         (scatter_df['track_popularity'] >= 0) & 
#         (scatter_df['track_popularity'] <= 100)
#     ]
    
    
#     for feature in ['energy', 'valence', 'danceability']:
#         scatter_df = scatter_df[
#             (scatter_df[feature] >= 0) & 
#             (scatter_df[feature] <= 1)
#         ]
    
    
#     if len(scatter_df) > 10000:
#         scatter_df = scatter_df.sample(n=10000, random_state=42)
    
#     return scatter_df.reset_index(drop=True)


def violin_plots_df(df):
    """
    Prepares data for violin plots (V5).
    Creates categorical bins for audio features.
    """
    df_clean = df.copy()
    
    df_clean['danceability_bin'] = pd.cut(df_clean['danceability'], 
                                         bins=[0, 0.33, 0.66, 1.0], 
                                         labels=['Low', 'Medium', 'High'])
    
    df_clean['acousticness_bin'] = pd.cut(df_clean['acousticness'], 
                                         bins=[0, 0.5, 1.0], 
                                         labels=['Non-Acoustic', 'Acoustic'])
    
    df_clean['instrumentalness_bin'] = pd.cut(df_clean['instrumentalness'], 
                                             bins=[0, 0.5, 1.0], 
                                             labels=['Non-Instrumental', 'Instrumental'])
    
    df_clean['mode_bin'] = df_clean['mode'].map({0: 'Minor', 1: 'Major'})
    
   
    df_clean['duration_minutes'] = df_clean['duration_ms'] / 60000
    df_clean['duration_bin'] = pd.cut(df_clean['duration_minutes'], 
                                     bins=[0, 3, 4, float('inf')], 
                                     labels=['Short (< 3 min)', 'Medium (3-4 min)', 'Long (> 4 min)'])
    
    df_clean['tempo_bin'] = pd.cut(df_clean['tempo'], 
                                  bins=[0, 90, 120, float('inf')], 
                                  labels=['Slow (< 90 BPM)', 'Medium (90-120 BPM)', 'Fast (> 120 BPM)'])
    
    return df_clean


def scatter_chart_df(df):
    """
    Prepares data for Energy vs Valence scatter plot with popularity and danceability.
    Args:
        df (pd.DataFrame): Raw Spotify data containing energy, valence, track_popularity, danceability, and track info.
    Returns:
        pd.DataFrame: DataFrame with energy, valence, track_popularity, danceability, playlist_genre, and track information.
    """
    scatter_df = df[['energy', 'valence', 'track_popularity', 'danceability',
                    'track_name', 'track_artist', 'playlist_genre']].dropna()
    
    scatter_df = scatter_df[
        (scatter_df['track_popularity'] >= 0) &
        (scatter_df['track_popularity'] <= 100)
    ]
    
    for feature in ['energy', 'valence', 'danceability']:
        scatter_df = scatter_df[
            (scatter_df[feature] >= 0) &
            (scatter_df[feature] <= 1)
        ]
    
    if len(scatter_df) > 10000:
        scatter_df = scatter_df.sample(n=10000, random_state=42)
    
    return scatter_df.reset_index(drop=True)
