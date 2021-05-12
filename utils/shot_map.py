#%%
import matplotlib.pyplot as plt
from mplsoccer import VerticalPitch
from utils.metadata import *
#from extract_data import *

def plot_shot_map(fig, ax, goals, non_goals, team: str):
    pitch = VerticalPitch(pitch_type='opta', half=True, pitch_color=pitch_background_color, line_color=pitch_line_color,
                          linewidth=2, pad_top=0, pad_bottom=0)
    
    pitch.draw(tight_layout=True, ax=ax)
    
    fig.set_facecolor(pitch_background_color)
    ax.patch.set_facecolor(pitch_background_color)
    TEAM_COLORS = {'home': home_color, 'away': away_color}
    
    # Plot shots
    ax.scatter(non_goals['y']*100, non_goals['x']*100,
                    s=non_goals['xG']*1000, c='grey', edgecolor='k', alpha=0.8, zorder=10, label='Skud')
    ax.scatter(goals['y']*100, goals['x']*100,
                    s=goals['xG']*1000, c=TEAM_COLORS[team], edgecolor='k', alpha=1, zorder=10, label='Mål')

    add_ax_title(ax, 'Shots')
    
#home_goals, home_non_goals, away_goals, away_non_goals = load_understat('gw23')
#fig, ax = plt.subplots(figsize=(10,6))
#plot_shot_map(fig, ax, home_goals, home_non_goals, team='home')