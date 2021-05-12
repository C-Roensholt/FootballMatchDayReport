#%%
import matplotlib.pyplot as plt
from mplsoccer import VerticalPitch, pitch
from utils.metadata import *
#from extract_data import *

def plot_key_passes(fig, ax, key_passes, team: str):
    pitch = VerticalPitch(pitch_type='opta', half=True, pitch_color=pitch_background_color, line_color=pitch_line_color,
                          linewidth=2, pad_top=0, pad_bottom=0)
    
    pitch.draw(tight_layout=True, ax=ax)
    
    fig.set_facecolor(pitch_background_color)
    ax.patch.set_facecolor(pitch_background_color)
    TEAM_COLORS = {'home': home_color, 'away': away_color}
    
    # Plot shots
    pitch.arrows(key_passes.x, key_passes.y,
                  key_passes.endX, key_passes.endY,
                  width=3, headwidth=4, headaxislength=3,
                  color=TEAM_COLORS[team], ax=ax, zorder=8)
    #plot circle at start of pass into box
    ax.scatter(key_passes.y, key_passes.x,
               s=100, color=TEAM_COLORS[team], facecolor=pitch_background_color,
               edgecolor=TEAM_COLORS[team], lw=2, zorder=10)

    
    
    add_ax_title(ax, 'Key Passes')
