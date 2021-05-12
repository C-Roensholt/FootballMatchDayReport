import matplotlib.pyplot as plt

# Colors
pitch_background_color = 'w'
text_color = '#000000'
pitch_line_color = '#000000'

home_color = '#1565c0'
away_color = '#c62828'

bar_stats = ['Mål', 'Skud', 'Skud på mål', 'Afleveringer', 'Afleveringer', 'Afleveringer']

def add_ax_title(ax, title):
    # Add title
    ax_title = ax.set_title(
                title,
                color=text_color,
                alpha=0.75,
                weight=600,
                fontsize=12,
                pad=8,
                zorder=-2,
                bbox=dict(
                    facecolor=pitch_background_color,
                    edgecolor=pitch_line_color,
                    linewidth=2,
                    alpha=1,
                    boxstyle='Square, pad=0.45',
                    zorder=1
                ))
    return ax_title
