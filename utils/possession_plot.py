#%%
from typing import Text
import pandas as pd
import matplotlib.pyplot as plt
from utils.metadata import *
from matplotlib.patches import Rectangle
import numpy as np
#from extract_data import *

def plot_possession(fig, ax, df_home_poss, df_away_poss, added_time: list):
    fig.set_facecolor(pitch_background_color)
    ax.patch.set_facecolor(pitch_background_color)
    
    x = df_home_poss['minute']
    
    y_home_poss = df_home_poss['rolling_percentage']
    y_away_poss = df_away_poss['rolling_percentage']

    # Plot added time
    added_time_box45 = Rectangle((45, 0), added_time[0], 100,
                               color='grey', alpha=0.2, hatch=3*'/', zorder=2)
    ax.add_artist(added_time_box45)
    ax.text((45+4), -5, s=f'+{added_time[0]}',
            fontsize=12, ha='center')

    added_time_box90 = Rectangle((90, 0), added_time[1], 100,
                               color='grey', alpha=0.2, hatch=3*'/', zorder=2)
    ax.add_artist(added_time_box90)
    ax.text((90+4), -5, s=f'+{added_time[1]}',
            fontsize=12, ha='center')
    
    
    # Plot lines
    ax.plot(x, y_home_poss,
        color=home_color, lw=5)

    ax.plot(x, y_away_poss,
        color=away_color, lw=5)

    # Shading around line
    ax.plot(x, y_home_poss,
        color=home_color, lw=15, alpha=0.3)
    ax.plot(x, y_away_poss,
        color=away_color, lw=15, alpha=0.3)

    ax.fill_between(x, y_home_poss, y_away_poss, step='post', 
                    where=(y_home_poss > y_away_poss), interpolate=True,
                    color=home_color, alpha=0.5)
    ax.fill_between(x, y_home_poss, y_away_poss, step='post', 
                    where=(y_home_poss <= y_away_poss), interpolate=True,
                    color=away_color, alpha=0.5)

    # Format axes
    ax.set_frame_on(False)
    ax.set_xticks([0, 15, 30, 45, 60, 75, 90])
    ax.set_yticks([])
    ax.tick_params(axis="both", which="both", length=0, colors=text_color, labelsize=14)

    ax.set_ylim(0, 100)

    # Set grid
    ax.grid(b=True, alpha=0.8, axis='x', linestyle=(0, (5, 10)), color='k')
    
    add_ax_title(ax, 'Ball Possession')

    return None

from scipy.interpolate import make_interp_spline, BSpline
def plot_momentum(fig, ax, df_home_poss, df_away_poss, home_goals, away_goals, added_time: list):
    fig.set_facecolor(pitch_background_color)
    ax.patch.set_facecolor(pitch_background_color)
    
    x = df_home_poss['minute']
    
    y_home_poss = df_home_poss['rolling_percentage']
    y_away_poss = df_away_poss['rolling_percentage']

    # Momentum difference
    y_momentum = y_home_poss - y_away_poss
    #make smooth
    x_new = np.linspace(x.min(), x.max(), 10000)  
    spl = make_interp_spline(x, y_momentum, k=3)
    y_smooth = spl(x_new)
       
    # Plot line
    #ax.plot(x, y_momentum,
    #    color=home_color, lw=5)

    # Shading around line
    #ax.plot(x, y_momentum,
    #    color=home_color, lw=15, alpha=0.3)
    ax.fill_between(x_new, y_smooth, 0, where=(y_smooth > 0),
                    facecolor=home_color, edgecolor='k', alpha=1, interpolate=True, zorder=10)
    
    ax.fill_between(x_new, y_smooth, 0, where=(y_smooth < 0),
                    facecolor=away_color, edgecolor='k', alpha=1, interpolate=True, zorder=10)

    # Format axes
    ax.set_frame_on(False)
    ax.set_xticks([0, 15, 30, 45, 60, 75, 90])
    ax.set_yticks([])
    ax.tick_params(axis="both", which="both", length=0, colors=text_color, labelsize=14)

    # Set grid
    ax.grid(b=True, alpha=0.8, axis='x', linestyle=(0, (5, 10)), color='k')
    #ax.grid(False)
    
    ymin, ymax = ax.get_ylim()
    
    # Plot added time
    added_time_box45 = Rectangle((45, ymin-10), added_time[0], 100,
                               color='grey', alpha=0.4, hatch=3*'/', zorder=-2)
    ax.add_artist(added_time_box45)
    fig.text((0.515), 0.111, s=f'+{added_time[0]}',
            fontsize=12, ha='center')

    added_time_box90 = Rectangle((90, ymin-10), added_time[1], 100,
                               color='grey', alpha=0.4, hatch=3*'/', zorder=-2)
    ax.add_artist(added_time_box90)
    fig.text((0.626), 0.111, s=f'+{added_time[1]}',
            fontsize=12, ha='center')
    
    
    # Add goals
    home_y = [ymax for _ in range(len(home_goals))]
    ax.scatter(x=home_goals, y=home_y, s=200, facecolor=home_color, edgecolor='k')
    away_y = [ymin for _ in range(len(away_goals))]
    ax.scatter(x=away_goals, y=away_y, s=200, facecolor=away_color, edgecolor='k')
    
    # Add lines for goals
    '''
    for i in range(len(home_goals)):
        intcp = np.interp(home_goals[i], x_new, y_smooth)
        ax.scatter(home_goals[i], intcp,
                   s=150, facecolor=home_color, zorder=15, edgecolor='k')
    for i in range(len(away_goals)):
        intcp = np.interp(away_goals[i], x_new, y_smooth)
        ax.scatter(away_goals[i], intcp,
                   s=150, facecolor=away_color, zorder=15, edgecolor='k')
    ''' 
    
    # Add title
    add_ax_title(ax, 'Momentum')

    return None



'''
df_home, df_away = load_data('2021', 'gw23')
df_home_poss, df_away_poss = get_possession_data(df_home, df_away)
home_poss, away_poss = calculate_possession(df_home_poss, df_away_poss)
added_time = get_added_time(df_home)

fig, ax = plt.subplots(figsize=(10,4))
plot_possession(fig, ax, df_home_poss, df_away_poss, added_time)
'''