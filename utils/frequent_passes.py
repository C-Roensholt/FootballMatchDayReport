import numpy as np
from utils.metadata import *

def plot_cluster(fig, ax, df, team):
    
    TEAM_COLORS = {'home': home_color, 'away': away_color}
    n_top_clusters_to_plot = 5
    
    clusters_to_plot = df['cluster'].value_counts().index[:n_top_clusters_to_plot]
    df.reset_index(drop=True, inplace=True)
    for i in range(len(clusters_to_plot)):
        ax.arrow(df['x'][i], df['y'][i],
                 df['endX'][i], df['endY'][i],
                 width=3, head_width=4, head_length=3,
                 color=TEAM_COLORS[team], zorder=8, alpha=0.3)

    ax.arrow(df.x.mean(), df.y.mean(),
                df.endX.mean(), df.endY.mean(),
                width=3, head_width=4, head_length=3,
                color=TEAM_COLORS[team], zorder=8, alpha=1)