import numpy as np
from utils.metadata import *

def plot_cluster(fig, ax, df, team):
    
    TEAM_COLORS = {'home': home_color, 'away': away_color}
    n_top_clusters_to_plot = 5
    
    clusters_to_plot = df['cluster'].value_counts().index[:n_top_clusters_to_plot]
    df.reset_index(drop=True, inplace=True)
    for i in range(len(clusters_to_plot)):
        ax.annotate('', xy=(df['x'][i], df['y'][i]),
                 xytext=(df['endX'][i], df['endY'][i]),
                 arrowprops={'width': 1, 'headwidth': 8, 'headlength': 8,
                'color': TEAM_COLORS[team], 'zorder': 8, 'alpha': 0.3})

    ax.annotate('', xy=(df.x.mean(), df.y.mean()),
                xytext=(df.endX.mean(), df.endY.mean()),
                arrowprops={'width': 3, 'headwidth': 4, 'headlength': 3,
                'color': TEAM_COLORS[team], 'zorder': 8, 'alpha': 1})