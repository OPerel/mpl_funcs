''' Matplotlib scatter chart '''
import random
import matplotlib.pyplot as plt

from annotate import Annotation

plt.style.use('./Kqlmagic.mplstyle')

# data
tabs = [{random.random() * 10: random.random() * 100 for _ in range(20)} for _ in range(10)]

# random.seed(107)

fig, ax = plt.subplots()

# plot data
labels = []
plots = []
colors = []
for i, tab in enumerate(tabs):
    color = list(random.random() for i in range(3))
    colors.append(color)
    labels.append(i)
    s = [v * 15 for v in tab.values()]
    plots.append(
        ax.scatter(
            list(tab.keys()),
            list(tab.values()),
            s=s,
            c=[color],
            linewidths=0.5,
            alpha=0.6,
            edgecolor='black'
            )
        )

# figure and axes properties
title = 'title'
ylabel = 'yaxis'
xlabel = 'xaxis'

ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
ax.legend(
    labels=labels,
    bbox_to_anchor=(0.95, 0.5),
    bbox_transform=fig.transFigure
)

Annotation(fig, ax, plots, tabs, colors).annotate_lines()

plt.show()
