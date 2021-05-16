from utils.metadata import *

def plot_average_positions(fig, ax, avg_locations, team):

    TEAM_COLORS = {'home': home_color, 'away': away_color}
    TEAM_ANNO = {'home': [-0.1, -1.2], 'away': [0.1, 1.2]}
    
    for i in range(len(avg_locations)):
        nodes = ax.scatter(avg_locations.x.iloc[i], avg_locations.y.iloc[i],
                        s=450, color=TEAM_COLORS[team], edgecolors='k', 
                        linewidth=1.5, alpha=1, zorder=10)
        text = ax.annotate(int(avg_locations.index[i]), xy = (avg_locations.x.iloc[i]+TEAM_ANNO[team][0], avg_locations.y.iloc[i]+TEAM_ANNO[team][1]), 
                            ha='center', color='w', fontsize=10, fontweight='semibold', zorder=11)

    if team == 'away':
        ax.invert_xaxis()
        ax.invert_yaxis()

    add_ax_title(ax, 'Average Positions')
    
    add_arrow(ax, team)