'''matplotlib line chart'''
import random
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('./Kqlmagic.mplstyle')

# generate some data
tabs = [{i: random.random() * 100 for i in range(10)} for _ in range(10)]
xticks = np.arange(len(tabs[0].keys()))

fig, ax = plt.subplots()

# plot data
plots = []
colors = []
for i, tab in enumerate(tabs):
    color = list(random.random() for i in range(3))
    colors.append(color)
    plot, = ax.plot(
        xticks,
        list(tab.values()),
        c=color,
        label=i,
        alpha=0.7
    )
    plots.append(plot)

# interactive annotation
annot = ax.annotate(
    '',
    xy=(0, 0),
    xytext=(10, 20),
    textcoords='offset points',
    arrowprops=dict(arrowstyle='-[')
)

annotx = ax.annotate(
    '',
    xy =(0, 0),
    xycoords=('data', 'axes fraction'),
    xytext=(0, -20),
    textcoords='offset points',
    bbox=dict(boxstyle='round', fc='grey', lw=0),
    arrowprops=dict(arrowstyle='->')
)

annot.set_visible(False)
annotx.set_visible(False)

def update_annot(i, ind):
    x, y = plots[i].get_data()
    annot.xy = (x[ind['ind'][0]], y[ind['ind'][0]])
    text = f'{i}: {y[ind["ind"][0]]}'
    annot.set_text(text)
    annot.set_bbox(
        dict(
            boxstyle='round',
            facecolor=colors[i],
            lw=0,
            alpha=0.8
        )
    )

    annotx.xy = (x[ind['ind'][0]], 0)
    k = list(tabs[i].keys())
    textx = f'{k[x[ind["ind"][0]]]}'
    annotx.set_text(textx)

def hover(event):
    vis = annot.get_visible()
    if event.inaxes:
        for i, plot in enumerate(plots):
            cont, ind = plot.contains(event)
            if cont:
                update_annot(i, ind)
                annot.set_visible(True)
                annotx.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    annotx.set_visible(False)
                    fig.canvas.draw_idle()

# fig and ax properties
title = 'Line Chart'
xlabel = 'xaxis'
ylabel = 'yaxis'
xlabels = [key for key in tabs[0].keys()]

ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
ax.set_xticks(xticks)
ax.set_xticklabels(xlabels)

ax.legend(
    bbox_to_anchor=(0.99, 0.6),
    bbox_transform=fig.transFigure,
)

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()
