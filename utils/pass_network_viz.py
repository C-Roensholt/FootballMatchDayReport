#%%
from utils.metadata import *
from utils.extract_data import get_pass_network_data, load_data
import pandas as pd
import matplotlib.pyplot as plt
from highlight_text import ax_text, fig_text
from mplsoccer.pitch import Pitch, VerticalPitch
import numpy as np
import math

df_home, df_away = load_data('2021', 'gw23')
home_avg_locations, home_pass_between, away_avg_locations, away_pass_between = get_pass_network_data(df_home, df_away)

home_avg_locations
home_pass_between
#%%
opacity = 0.4
width = 0.8
zorder = 10

def draw_arrow_with_shrink(ax, x, y, end_x, end_y, lw, line_color, alpha, dist_delta=4):
    dist = math.hypot(end_x - x, end_y - y)
    angle = math.atan2(end_y - y, end_x - x)
    upd_end_x = x + (dist - dist_delta) * math.cos(angle)
    upd_end_y = y + (dist - dist_delta) * math.sin(angle)
    upd_x = end_x - (dist - dist_delta * 1.2) * math.cos(angle)
    upd_y = end_y - (dist - dist_delta * 1.2) * math.sin(angle)
    ax.annotate('', xy=(upd_end_x, upd_end_y), xytext=(upd_x, upd_y), zorder=1,
                arrowprops=dict(width=width, color=line_color, alpha=0.8,
                                headwidth=3*1.3*width,
                                headlength=1.5*1.3*(3*1.3*width)))
    

def plot_pass_network(fig, ax, avg_locations, pass_between, team='home'):
    """
    Input:
        team: 'home' or 'away'
    Returns:
        fig, ax: Matplotlib fig and ax
    """
    # To-do: Create color map of the node labels
    #LABEL_COLOR = TEMPLATE_COLOR = col_dict[position]
    #cmap = colors.LinearSegmentedColormap.from_list("", ["white",col_dict[position]])

    fig.set_facecolor(pitch_background_color)
    ax.patch.set_facecolor(pitch_background_color)
    

    #add title and description
    #fig_text(x = 0.03, y = 1.02,
    #        s = 'Liverpool vs Newcastle',
    #        color = 'white', ha='left', highlight_colors = ['white'], fontsize=34, fontweight='bold')
    
    #plot pass arrows
    for i in range(len(pass_between)):
        draw_arrow_with_shrink(ax=ax, x=pass_between.x[i], y=pass_between.y[i],
                               end_x=pass_between.x_end[i], end_y=pass_between.y_end[i],
                               lw=0.005, line_color=pitch_line_color, 
                               alpha=pass_between['pass_count'][i]*0.1, dist_delta=5.5)

    if team == 'home':
        nodes = ax.scatter(avg_locations.x, avg_locations.y,
                        s=450, color=home_color, edgecolors='k', 
                        linewidth=1.5, alpha=1, zorder=3)
        text = [ax.annotate(int(txt), xy = (avg_locations['x'].iloc[i]-0.1, avg_locations['y'].iloc[i]-1.2), 
                            ha='center', color='w', fontsize=10, fontweight='semibold') 
                for i, txt in enumerate(avg_locations.index)]

    if team == 'away':
        nodes = ax.scatter(avg_locations.x, avg_locations.y,
                           s=450, color=away_color, edgecolors='k', 
                           linewidth=1.5, alpha=1, zorder=3)
        text = [ax.annotate(int(txt), xy = (avg_locations['x'].iloc[i]+0.1, avg_locations['y'].iloc[i]+1.2), 
                    ha='center', color='w', fontsize=10, fontweight='semibold') 
        for i, txt in enumerate(avg_locations.index)]
        ax.invert_xaxis()
        ax.invert_yaxis()

    
    return None

def plot_pass_network_1(fig, ax, avg_locations, pass_between, team='home'):
    """
    Input:
        team: 'home' or 'away'
    Returns:
        fig, ax: Matplotlib fig and ax
    """
    # To-do: Create color map of the node labels
    #LABEL_COLOR = TEMPLATE_COLOR = col_dict[position]
    #cmap = colors.LinearSegmentedColormap.from_list("", ["white",col_dict[position]])

    fig.set_facecolor(pitch_background_color)
    ax.patch.set_facecolor(pitch_background_color)

    arrow_shift = 2 ##Units by which the arrow moves from its original position
    shrink_val = 10 ##Units by which the arrow is shortened from the end_points


    #add title and description
    #fig_text(x = 0.03, y = 1.02,
    #        s = 'Liverpool vs Newcastle',
    #        color = 'white', ha='left', highlight_colors = ['white'], fontsize=34, fontweight='bold')
    
    for i in range(len(pass_between)):
        link = pass_between['pass_count'][3] ## for the arrow-width and the alpha 
        
        alpha = link
        if alpha > 1:
            alpha=0.8
        
        if abs(pass_between.iloc[i].x_end - pass_between.iloc[i].x) > abs(pass_between.iloc[i].y_end - pass_between.iloc[i].y):

            if pass_between.iloc[i].passer > pass_between.iloc[i].recipient:
                ax.annotate("", xy=(pass_between.iloc[i].x_end, pass_between.iloc[i].y_end + arrow_shift), xytext=(pass_between.iloc[i].x, pass_between.iloc[i].y + arrow_shift),
                                arrowprops=dict(arrowstyle="-|>", color="0.25", shrinkA=shrink_val, shrinkB=shrink_val, lw=link*0.2, alpha=alpha))
                
            elif pass_between.iloc[i].passer < pass_between.iloc[i].recipient:
                ax.annotate("", xy=(pass_between.iloc[i].x_end, pass_between.iloc[i].y_end - arrow_shift), xytext=(pass_between.iloc[i].x, pass_between.iloc[i].y - arrow_shift),
                                arrowprops=dict(arrowstyle="-|>", color="0.25", shrinkA=shrink_val, shrinkB=shrink_val, lw=link*0.2, alpha=alpha))

        elif abs(pass_between.iloc[i].x_end - pass_between.iloc[i].x) <= abs(pass_between.iloc[i].y_end - pass_between.iloc[i].y):

            if pass_between.iloc[i].passer > pass_between.iloc[i].recipient:
                ax.annotate("", xy=(pass_between.iloc[i].x_end, pass_between.iloc[i].y_end + arrow_shift), xytext=(pass_between.iloc[i].x, pass_between.iloc[i].y + arrow_shift),
                                arrowprops=dict(arrowstyle="-|>", color="0.25", shrinkA=shrink_val, shrinkB=shrink_val, lw=link*0.2, alpha=alpha))
                
            elif pass_between.iloc[i].passer < pass_between.iloc[i].recipient:
                ax.annotate("", xy=(pass_between.iloc[i].x_end, pass_between.iloc[i].y_end - arrow_shift), xytext=(pass_between.iloc[i].x, pass_between.iloc[i].y - arrow_shift),
                                arrowprops=dict(arrowstyle="-|>", color="0.25", shrinkA=shrink_val, shrinkB=shrink_val, lw=link*0.2, alpha=alpha))

    if team == 'home':
        nodes = ax.scatter(avg_locations.x, avg_locations.y,
                        s=350, color=home_color, edgecolors='k', 
                        linewidth=1.5, alpha=1, zorder=10)
        text = [ax.annotate(int(txt), xy = (avg_locations['x'].iloc[i]-0.1, avg_locations['y'].iloc[i]-1.2), 
                            ha='center', color='w', fontsize=8, fontweight='semibold', zorder=11) 
                for i, txt in enumerate(avg_locations.index)]

    if team == 'away':
        nodes = ax.scatter(avg_locations.x, avg_locations.y,
                           s=350, color=away_color, edgecolors='k', 
                           linewidth=1.5, alpha=1, zorder=10)
        text = [ax.annotate(int(txt), xy = (avg_locations['x'].iloc[i]+0.1, avg_locations['y'].iloc[i]+1.2), 
                    ha='center', color='w', fontsize=8, fontweight='semibold', zorder=11) 
        for i, txt in enumerate(avg_locations.index)]
        ax.invert_xaxis()
        ax.invert_yaxis()

    add_ax_title(ax, 'Passing Network')
    
    add_arrow(ax, team)
    
    return None

#fig, ax = plt.subplots(figsize=(10,8))
#plot_pass_network_1(fig, ax, home_avg_locations, home_pass_between)