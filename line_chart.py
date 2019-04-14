'''matplotlib line chart'''
import random
import numpy as np
import matplotlib.pyplot as plt

from annotate import Annotation

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

Annotation(fig, ax, plots, tabs, colors).annotate_lines()

plt.show()
