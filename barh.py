''' matplotlib horizontal bar chart with intercative annotation. '''

import random
import matplotlib.pyplot as plt
import numpy as np

from annotate import Annotation

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


title = 'horizontal Bar Chart'
xlabel = 'xaxis'
ylabel = 'taxis'
ylabels = list(tabs[0].keys())

ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
ax.set_yticks(yticks)
ax.set_yticklabels(ylabels)
ax.legend(loc='best')

Annotation(fig, ax, plots, colors).annotate()

plt.show()
