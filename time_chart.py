''' matplotlib time chart '''
import datetime as dt
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

# generate data
tabs = [{dt.datetime(2018, 5, 1) + i * dt.timedelta(days=7): i * random.random() for i in range(10)} for _ in range(10)]

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
        marker='.',
        markersize=6,
        linestyle='-',
        linewidth=0.6,
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

# annotate on hover
annot = ax.annotate(
    '',
    xy=(0, 0),
    xytext=(40, 20),
    textcoords='offset points',
    arrowprops=dict(arrowstyle='-[', connectionstyle='arc3, rad=0.3')
)

annotx = ax.annotate(
    '',
    xy=(0, 0),
    xycoords=('data', 'axes fraction'),
    xytext=(-20, -40),
    textcoords='offset points',
    bbox=dict(boxstyle='round', fc='grey', lw=0),
    horizontalalignment='center',
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=0.3'),
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
    textx = mdates.num2date(x[ind['ind'][0]]).strftime('%H:%M \n %b %d, %Y')
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
                return
    if vis:
        annot.set_visible(False)
        annotx.set_visible(False)
        fig.canvas.draw_idle()

# fig and ax properties
ylabel = 'yaxis'
xlabel = 'xaxis'
title = 'title'

ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
ax.grid(linewidth=0.2)
ax.legend(
    loc='center right',
    bbox_to_anchor=(0.99, 0.6),
    bbox_transform=fig.transFigure,
    markerscale=0.7,
    fontsize='small',
    frameon=False
)

ax.set_frame_on(False)

fig.tight_layout(rect=(0, 0, 0.9, 0.99))
#     plt.subplot_tool()
fig.canvas.mpl_connect("motion_notify_event", hover)
plt.show()
