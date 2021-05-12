#%%
import pandas as pd
from mplsoccer import PyPizza
from utils.extract_data import load_data, get_radar_data
from utils.metadata import *
import matplotlib.pyplot as plt
from matplotlib import colors
from adjustText import adjust_text

def plot_radar(fig, ax, pvals: list, team):
    TEAM_COLORS = {'home': home_color, 'away': away_color}
    #TEAM_AX = {'home': 15, 'away': 16}
    pvals = [int(val) for val in pvals]
    cmap = colors.LinearSegmentedColormap.from_list("", ["white",'red'])

    
    fig.set_facecolor(pitch_background_color)
    ax.patch.set_facecolor(pitch_background_color)
    #add_ax_title(ax, 'Playing Style')
    
    if team=='home':
        ax = fig.add_subplot(4, 6, 15, projection='polar')
    if team=='away':
        ax = fig.add_subplot(4, 6, 16, projection='polar')
    
    
    # Set colors
    slice_colors = [TEAM_COLORS[team]]*8
    #slice_colors = cmap([0.6, 0.7, 0.8, 0.9, 1])*8
    text_colors = ['k']*8
    bg_colors = ['w']*8

    params = ['Kant spil', 'Dybt spil', 'Lange bolde', 'Kontra',
              'Indlæg', 'Danger Zone', 'Dybt forsvar', 'Højt pres']
    
    # instantiate PyPizza class
    baker = PyPizza(
        params=params,                  # list of parameters
        background_color='w',     # background color
        straight_line_color="#000000",  # color for straight lines
        straight_line_lw=3,             # linewidth for straight lines
        last_circle_color="#000000",    # color for last line
        last_circle_lw=5,               # linewidth of last circle
        other_circle_lw=1,              # linewidth for other circles
        other_circle_color='#000000',
        other_circle_ls=(0, (5, 10)),
        inner_circle_size=20            # size of inner circle
    )

    # plot pizza
    baker.make_pizza(
        pvals,                           # list of values
        figsize=(8, 8.5),                # adjust the figsize according to your need
        color_blank_space=bg_colors,     # use the same color to fill blank space
        slice_colors=slice_colors,       # color for individual slices
        value_colors=['w']*8,        # color for the value-text
        value_bck_colors=slice_colors,   # color for the blank spaces
        blank_alpha=0.4,                 # alpha for blank-space colors
        ax=ax,
        
        kwargs_slices=dict(
        edgecolor='k', zorder=0, linewidth=3, color=slice_colors
        ),                               # values to be used when plotting slices
        kwargs_params=dict(
            color="k", fontsize=11, va="center", fontweight='bold'
        ),                               # values to be used when adding parameter labels
        kwargs_values=dict(
            color="k", fontsize=11, zorder=3, fontweight='bold',
            bbox=dict(
                edgecolor="#000000", facecolor="w",
                boxstyle="round,pad=0.4", lw=2
            )
        )                                # values to be used when adding parameter-values labels
    )
    # Adjust text to avoid overlap

            
    value_texts = baker.get_value_texts()
    texts_adjusted = [txt for txt in value_texts if int(txt.get_text()) > 80]
    
    adj_val = 20
    
    for temp_text in texts_adjusted:
        temp_text.set_position((
        temp_text.get_position()[0], temp_text.get_position()[1] - adj_val
        ))

    
    
    
"""
fig = plt.figure()
ax = fig.add_subplot(projection='polar')

df_home, df_away = load_data('2021', 'gw23')
home_pvals, away_pvals = get_radar_data(df_home, df_away)
plot_radar(fig, ax, away_pvals, team='away')
"""