import random
import matplotlib.pyplot as plt
import numpy as np

tabs = [{'SOUTH CAROLINA': 1662, 'IDAHO': 10343, 'VIRGINIA': 9689, 'KANSAS': 3634, 'NEBRASKA': 5024, 'TEXAS': 5134},
        {'SOUTH CAROLINA': 8015, 'IDAHO': 57541, 'VIRGINIA': 54272, 'KANSAS': 20370, 'NEBRASKA': 29011, 'TEXAS': 29910},
        {'SOUTH CAROLINA': 15000, 'IDAHO': 40000, 'VIRGINIA': 40000, 'KANSAS': 25000, 'NEBRASKA': 20000, 'TEXAS': 25000}]

# random.seed(112)

vals = len(tabs)
xticks = np.arange(len(tabs[0]))
xlabels = list(tabs[0].keys())

fig, ax = plt.subplots(figsize=(9, 5))

plots = []
colors = []
for i, tab in enumerate(tabs):
    color = list(random.random() for i in range(vals))
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

# annotation template
annots = []
for i, tab in enumerate(tabs):
    annot = ax.annotate(
        "",
        xy=(0, 0),
        xytext=(15, 20),
        textcoords="offset points",
        arrowprops=dict(arrowstyle='->')
    )

    annot.set_visible(False)
    annots.append(annot)

# update annotation with bar data
def update_annot(i, bar):
    x = bar.get_x() + bar.get_width() / 2.
    y = bar.get_y() + bar.get_height()
    annot.xy = (x, y)
    text = f'{i}: {y}'
    annot.set_text(text)
    annot.set_bbox(
        dict(
            boxstyle='round',
            lw=0,
            color=colors[i],
            alpha=0.8
            )
        )

# activate annotation on hover
def hover(event):
    # vis = annot.get_visible()
    if event.inaxes:
        for i, plot in enumerate(plots):
            for bar in plot:
                cont, _ = bar.contains(event)
                if cont:
                    # col = [plot[j] for plot in plots]
                    # col = list(zip(*plots))[j]
                    update_annot(i, bar)
                    annot.set_visible(True)
                    fig.canvas.draw_idle()
                    return
                else:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()

ax.set(title='title', xlabel='xlabel', ylabel='ylabel')
ax.set_xticks(xticks)
ax.set_xticklabels(xlabels, rotation=45)
ax.legend()
ax.grid(axis='y', linewidth=0.2)
fig.tight_layout(rect=(0, 0, 0.9, 0.9))

fig.canvas.mpl_connect("motion_notify_event", hover)
# print(list(zip(*plots)), '\n')
# for i in zip(*plots):
#     print(i)
plt.show()
