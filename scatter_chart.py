''' Matplotlib scatter chart '''
import random
import matplotlib.pyplot as plt

from annotate import Annotation

plt.style.use('./Kqlmagic.mplstyle')

# data
tabs = [{random.random() * 10: random.random() * 100 for _ in range(20)} for _ in range(10)]

random.seed(107)

fig, ax = plt.subplots(figsize=(9, 5))

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

# # annotation template
# annot = ax.annotate(
#     '',
#     xy=(0, 0),
#     xytext=(20, 20),
#     textcoords='offset points',
#     arrowprops=dict(arrowstyle='-[')
# )
#
# annotx = ax.annotate(
#     '',
#     xy=(0, 0),
#     xycoords=('data', 'axes fraction'),
#     xytext=(0, -35),
#     textcoords='offset points',
#     bbox=dict(boxstyle='round', fc='grey', lw=0),
#     arrowprops=dict(arrowstyle='->')
# )
#
# annot.set_visible(False)
# annotx.set_visible(False)
#
# # update annotation with point data
# def update_annot(i, ind):
#     pos = plots[i].get_offsets()[ind["ind"][0]]
#     annot.xy = pos
#     text = f'{i}: {str(pos[1])}'
#     annot.set_text(text)
#     annot.set_bbox(
#         dict(
#             boxstyle='round',
#             facecolor=colors[i],
#             lw=0,
#             alpha=0.8
#         )
#     )
#
#     annotx.xy = (pos[0], 0)
#     textx = pos[0]
#     annotx.set_text(textx)
#
# # activate on hover
# def hover(event):
#     vis = annot.get_visible()
#     if event.inaxes:
#         for i, plot in enumerate(plots):
#             cont, ind = plot.contains(event)
#             if cont:
#                 update_annot(i, ind)
#                 annot.set_visible(True)
#                 annotx.set_visible(True)
#                 fig.canvas.draw_idle()
#             else:
#                 if vis:
#                     annot.set_visible(False)
#                     annotx.set_visible(False)
#                     fig.canvas.draw_idle()

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
# print(type(Annotation(fig, ax, plots, tabs, colors).plots[0]))
Annotation(fig, ax, plots, tabs, colors).annotate_lines()
# fig.canvas.mpl_connect('motion_notify_event', hover)

plt.show()
