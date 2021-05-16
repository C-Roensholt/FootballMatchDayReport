import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
from utils.metadata import *

def plot_heatmap(fig, ax, actions, team: str, heatmap_type: str):
    TEAM_COLORS = {'home': home_color, 'away': away_color}
    TYPE = {'defensive': 'Defensive Heatmap', 'offensive': 'Offensive Heatmap'}

    # Create heatmap
    cmap = colors.LinearSegmentedColormap.from_list("", [pitch_background_color, TEAM_COLORS[team]])
    
    heatmap_1 = sns.kdeplot(x='x', y='y', data=actions, ax=ax, 
                     cmap=cmap, fill=True, bw_method=0.3, alpha=1, levels=10)

    if team == 'away':
        ax.invert_xaxis()
        #ax.invert_yaxis()

    
    add_ax_title(ax, TYPE[heatmap_type])
    
    add_arrow(ax, team)

