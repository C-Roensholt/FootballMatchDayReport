import numpy as np
from utils.metadata import *
from matplotlib import colors
import matplotlib.patheffects as path_effects
import seaborn as sns
import matplotlib.pyplot as plt
#from extract_data import *

def plot_juego(fig, ax, pitch, df, team):
    
    TEAM_COLORS = {'home': home_color, 'away': away_color}

    # Create heatmap
    cmap = colors.LinearSegmentedColormap.from_list("", [pitch_background_color, TEAM_COLORS[team]])
    path_eff = [path_effects.Stroke(linewidth=1.5, foreground='black'),
                path_effects.Normal()]
    
    bin_statistic = pitch.bin_statistic_positional(df.x, df.y, statistic='count',
                                                   positional='full', normalize=True)
    pitch.heatmap_positional(bin_statistic, ax=ax, cmap=cmap, edgecolors='#22312b')
    
    #pitch.scatter(df.x, df.y, c='white', s=2, ax=ax)
    ax.scatter(df.x, df.y, 
                s=20, color='k', alpha=0.8, zorder=10)
    #ax.scatter(df.x, df.y, 
    #            s=150, color='w', alpha=0.2, marker='h', zorder=4)
 
    
    labels = pitch.label_heatmap(bin_statistic, color='#f4edf0', fontsize=18,
                                 ax=ax, ha='center', va='center', path_effects=path_eff,
                                 str_format='{:.0%}', exclude_zeros=True, zorder=15)
    
    if team == 'away':
        ax.invert_xaxis()
        #ax.invert_yaxis()
        
    add_arrow(ax, team)
    
    # Add title
    add_ax_title(ax, 'Shot Assist Locations')

    return None
 
    