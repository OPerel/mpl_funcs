import numpy as np
import random
import math
import matplotlib.pyplot as plt

# TODO: multiple axes: plotting single pie, annotation, legends, layout and style

plt.style.use('./Kqlmagic.mplstyle')

tabs = [{'Bothell': 964212, 'Yokohama': 168749, 'Baotou': 253928, 'Rottweil': 224921, 'Nantes': 194504, 'Peterborough': 327117, 'Sao Goncalo': 190879},
        {'Bothell': 967242, 'Yokohama': 265749, 'Baotou': 194568, 'Rottweil': 654254, 'Nantes': 300985, 'Peterborough': 187543, 'Sao Goncalo': 346432}
        ]

colors = [list(random.random() for _ in range(3)) for i in range(len(tabs[0].keys()))]

num_of_subplots = len(tabs)
fig, axes = plt.subplots(1, num_of_subplots)

plots = []
for i, tab in enumerate(tabs):
    plots.append(
        axes[i].pie(
            tab.values(),
            labels=tab.keys(),
            autopct='%1.1f%%',
            colors=colors
        )
    )

# for p in plots:
#     print(p)

# annotation template
annots = []
for ax in axes:
    annot = ax.annotate(
        '',
        xy=(0, 0),
        xytext=(0, 0),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', connectionstyle='angle, angleA=90, angleB=-10, rad=5')
    )

    annot.set_visible(False)
    annots.append(annot)
print(annots)

def update_annot(t, i, patch):
    theta1, theta2 = patch.theta1, patch.theta2
    center, r = patch.center, patch.r
    x = r * np.cos(math.pi / 180 * theta1 + center[0])
    y = np.sin(math.pi / 180 * theta1 + center[1])
    annot.xy = (x, y)
    if 0 < theta1 < 90:
        annot.set_x(x + 10)
        annot.set_y(y + 40)
    elif 90 < theta1 < 180:
        annot.set_x(x - 80)
        annot.set_y(y + 40)
    elif 180 < theta1 < 270:
        annot.set_x(x - 80)
        annot.set_y(y - 40)
    else:
        annot.set_x(x + 10)
        annot.set_y(y - 40)
    text = f'{list(tabs[t].keys())[i]}: {list(tabs[t].values())[i]}'
    annot.set_text(text)
    annot.set_bbox(
                dict(
                    boxstyle='round',
                    facecolor=colors[i],
                    lw=0,
                    alpha=0.8
                    )
                )

def hover(event):
    vis = annot.get_visible()
    if event.inaxes:
        for t, pie in enumerate(plots):
            for i, patch in enumerate(pie[0]):
                cont, ind = patch.contains(event)
                if cont:
                    update_annot(t, i, patch)
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                    return
    if vis:
        annot.set_visible(False)
        fig.canvas.draw_idle()

# figure and axes chart_properties
for ax in axes:
    title = 'Pie chart'
    xlabel = 'xaxis'
    ylabel = 'yaxis'
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.legend(
        fontsize='large',
        bbox_to_anchor=(0.95, 0.6),
        bbox_transform=fig.transFigure,
    )
    ax.set_aspect('equal')

fig.canvas.mpl_connect('motion_notify_event', hover)

plt.show()
