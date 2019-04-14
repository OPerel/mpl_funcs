''' matplotlib bar chart with intercative annotation. '''

import random
import matplotlib.pyplot as plt
import numpy as np

from annotate import Annotation

plt.style.use('./Kqlmagic.mplstyle')

# sample data
tabs = [{'SOUTH CAROLINA': 1662, 'IDAHO': 10343, 'VIRGINIA': 9689, 'KANSAS': 3634, 'NEBRASKA': 5024, 'TEXAS': 5134},
        {'SOUTH CAROLINA': 8015, 'IDAHO': 57541, 'VIRGINIA': 54272, 'KANSAS': 20370, 'NEBRASKA': 29011, 'TEXAS': 29910},
        {'SOUTH CAROLINA': 15000, 'IDAHO': 40000, 'VIRGINIA': 40000, 'KANSAS': 25000, 'NEBRASKA': 20000, 'TEXAS': 25000}]

# random.seed(2001) # uncomment to fix color palette

vals = len(tabs)
xticks = np.arange(len(tabs[0]))
xlabels = list(tabs[0].keys())

fig, ax = plt.subplots()

# plot data
plots = []
colors = []
for i, tab in enumerate(tabs):
    color = list(random.random() for i in range(3))
    colors.append(color)
    plots.append(
        ax.bar(
            xticks - 0.7 / 2. + i / float(vals) * 0.7,
            list(tab.values()),
            width=0.7 / float(vals),
            align='edge',
            color=color,
            label=i
            )
        )

ax.set(title='title', xlabel='xlabel', ylabel='ylabel')
ax.set_xticks(xticks)
ax.set_xticklabels(xlabels, rotation=45)
ax.legend(loc='best')

Annotation(fig, ax, plots, tabs, colors).annotate_bars()

plt.show()
