''' matplotlib horizontal bar chart with intercative annotation. '''

import random
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('./Kqlmagic.mplstyle')

tabs = [{'SOUTH CAROLINA': 1662, 'IDAHO': 10343, 'VIRGINIA': 9689, 'KANSAS': 3634, 'NEBRASKA': 5024, 'TEXAS': 5134},
        {'SOUTH CAROLINA': 8015, 'IDAHO': 57541, 'VIRGINIA': 54272, 'KANSAS': 20370, 'NEBRASKA': 29011, 'TEXAS': 29910},
        {'SOUTH CAROLINA': 15000, 'IDAHO': 40000, 'VIRGINIA': 40000, 'KANSAS': 25000, 'NEBRASKA': 20000, 'TEXAS': 25000}]

vals = len(tabs)
yticks = np.arange(len(tabs[0]))

fig, ax = plt.subplots()

plots = []
colors = []
for i, tab in enumerate(tabs):
    color = list(random.random() for _ in range(3))
    colors.append(color)
    plots.append(
        ax.barh(
            yticks - 0.8 / 2. + i / float(vals) * 0.8,
            list(tabs[i].values()),
            height=0.8 / float(vals),
            align='edge',
            color=color,
            label=i
            )
        )

# annotation template
annot = ax.annotate(
    '',
    xy=(0, 0),
    xytext=(20, 10),
    textcoords='offset points',
    arrowprops=dict(arrowstyle='->')
)

annot.set_visible(False)

def update_annot(i, bar):
    y = bar.get_x() + bar.get_width()
    x = bar.get_y() + bar.get_height()
    annot.xy = (y, x)
    text = f'{i}: {y}'
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
        for i, plot in enumerate(plots):
            for bar in plot:
                cont, _ = bar.contains(event)
                if cont:
                    update_annot(i, bar)
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                    return
    if vis:
        annot.set_visible(False)
        fig.canvas.draw_idle()

title = 'horizontal Bar Chart'
xlabel = 'xaxis'
ylabel = 'taxis'
ylabels = list(tabs[0].keys())

ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
ax.set_yticks(yticks)
ax.set_yticklabels(ylabels)
ax.legend(loc='best')

fig.canvas.mpl_connect('motion_notify_event', hover)

plt.show()
