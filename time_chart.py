''' matplotlib time chart '''
import datetime as dt
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

from annotate import Annotation

plt.style.use('./Kqlmagic.mplstyle')

# generate data
tabs = [{dt.datetime(2018, 5, 1) + i * dt.timedelta(hours=8): i * random.random() for i in range(10)} for _ in range(10)]
fig, ax = plt.subplots(figsize=(9, 5))

# plot data
plots = []
colors = []
for i, tab in enumerate(tabs):
    color = list(random.random() for i in range(3))
    colors.append(color)
    date = mdates.date2num(list(tab.keys()))
    plot, = ax.plot_date(
        date,
        list(tab.values()),
        linestyle='-',
        c=color,
        label=i
    )
    plots.append(plot)

# scale dates on x axis, locate ticks and format labels
def format_dates(x, pos):
    xticks = [mdates.num2date(date) for date in ax.get_xticks()]
    if pos == 0:
        if xticks[0].day != xticks[1].day:
            fmt = '%b %d \n %Y'
        else:
            fmt = '%H:%M \n %b %d, %Y'
    else:
        if xticks[pos - 1].year != xticks[pos].year:
            fmt = '%b %d \n %Y'
        elif xticks[pos - 1].month != xticks[pos].month:
            fmt = '%b %d'
        elif xticks[pos - 1].day != xticks[pos].day:
            if xticks[pos - 2].day != xticks[pos - 1].day:
                fmt = '%b %d'
            else:
                fmt = '%H:%M \n %b %d'
        else:
            fmt = '%H:%M'

    return xticks[pos].strftime(fmt)

locator = mdates.AutoDateLocator(interval_multiples=False)
ax.xaxis.set_major_locator(locator)
formatter = FuncFormatter(format_dates)
ax.xaxis.set_major_formatter(formatter)

# fig and ax properties
title = 'Time Chart'
ylabel = 'yaxis'
xlabel = 'xaxis'

ax.set(title=title, xlabel=xlabel, ylabel=ylabel)

ax.legend(
    bbox_to_anchor=(0.99, 0.6),
    bbox_transform=fig.transFigure,
)

Annotation(fig, ax, plots, tabs, colors).annotate_lines()

plt.show()
