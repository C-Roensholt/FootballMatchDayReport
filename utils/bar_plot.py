#%%
import pandas as pd
import numpy as np
from utils.extract_data import load_data, get_bar_plot_data
from utils.metadata import *
import matplotlib.pyplot as plt

def plot_bar(fig, ax, home_stats, away_stats):
    
    home_num_stats, home_per = zip(*home_stats)
    away_num_stats, away_per = zip(*away_stats)
    home_num_stats, home_per = list(home_num_stats), list(home_per)
    away_num_stats, away_per = list(away_num_stats), list(away_per)

    fig.set_facecolor(pitch_background_color)
    ax.patch.set_facecolor(pitch_background_color)

    bar_home = ax.barh(bar_stats, home_per, height=0.6,
                       alpha=1, facecolor=home_color, edgecolor='k', linewidth=2)
    bar_away = ax.barh(bar_stats, away_per, height=0.6,
                       alpha=1, facecolor=away_color, edgecolor='k', linewidth=2,
                       left=home_per)
    
    ax.set_frame_on(False)
    ax.axes.get_xaxis().set_visible(False)
    ax.tick_params(axis='y', colors='w', labelsize=14)
    # Add bar labels in middle
    for i, stat in enumerate(bar_stats):
        ax.text(0.5, i-0.5, s=f'{stat}', ha='center', va='center',
                fontsize=20, fontweight='bold')

    # Add home and away stats
    for i, home_stat in enumerate(home_num_stats):
        ax.text(0.05, i-0.5, s=f'{home_stat}', ha='center', va='center',
                fontsize=24, fontweight='bold')
    for i, away_stat in enumerate(away_num_stats):
        ax.text(0.95, i-0.5, s=f'{away_stat}', ha='center', va='center',
                fontsize=24, fontweight='bold')
        
    
    add_ax_title(ax, 'Match Stats')
    
    return None
"""
df_home, df_away = load_data('2021', 'gw23')
home_stats, away_stats = get_bar_plot_data(df_home, df_away)

fig, ax = plt.subplots(figsize=(12,8))

plot_bar(fig, ax, home_stats, away_stats)
"""