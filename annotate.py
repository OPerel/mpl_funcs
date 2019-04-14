import matplotlib
import matplotlib.dates as mdates
import datetime as dt

class Annotation():
    def __init__(self, figure, axes, plots, data, colors):
        self.fig = figure
        self.ax = axes
        self.plots = plots
        self.data = data
        self.colors = colors

    def annotation_temp(self):
        # annotation template
        ann = self.ax.annotate(
            "",
            xy=(0, 0),
            xytext=(15, 20),
            textcoords="offset points",
            arrowprops=dict(arrowstyle='->')
        )

        return ann

    def xaxis_annotation_temp(self):
        ann = self.ax.annotate(
            '',
            xy =(0, 0),
            xycoords=('data', 'axes fraction'),
            xytext=(0, -60),
            textcoords='offset points',
            bbox=dict(boxstyle='round', fc='grey', lw=0),
            horizontalalignment='center',
            arrowprops=dict(arrowstyle='->')
        )

        return ann

    def annotate_bars(self):
        # annotate bar charts
        annot = self.annotation_temp()
        annot.set_visible(False)

        # update annotation with bar data
        def update_annot(i, bar):
            if self.plots[0][0].properties()['y'] == 0:
                x = bar.get_x() + bar.get_width() / 2.
                y = bar.get_y() + bar.get_height()
                annot.xy = (x, y)
            else:
                y = bar.get_x() + bar.get_width()
                x = bar.get_y() + bar.get_height()
                annot.xy = (y, x)
            text = f'{i}: {y}'
            annot.set_text(text)
            annot.set_bbox(
                dict(
                    boxstyle='round',
                    lw=0,
                    color=self.colors[i],
                    alpha=0.8
                    )
                )

        # activate annotation on hover
        def hover(event):
            vis = annot.get_visible()
            if event.inaxes:
                for i, plot in enumerate(self.plots):
                    for bar in plot:
                        cont, _ = bar.contains(event)
                        if cont:
                            # col = [plot[j] for plot in plots]
                            # col = list(zip(*plots))[j]
                            update_annot(i, bar)
                            annot.set_visible(True)
                            self.fig.canvas.draw_idle()
                            return
            if vis:
                annot.set_visible(False)
                self.fig.canvas.draw_idle()

        self.fig.canvas.mpl_connect('motion_notify_event', hover)
        return self

    def annotate_lines(self):
        ''' annotate line charts '''
        annot = self.annotation_temp()
        annotx = self.xaxis_annotation_temp()
        annot.set_visible(False)
        annotx.set_visible(False)

        # update annotation with point data
        def update_annot(i, ind):
            if isinstance(self.plots[i], matplotlib.collections.PathCollection):
                pos = self.plots[i].get_offsets()[ind["ind"][0]]
                annot.xy = pos
                text = f'{i}: {str(pos[1])}'
            else:
                x, y = self.plots[i].get_data()
                annot.xy = (x[ind['ind'][0]], y[ind['ind'][0]])
                text = f'{i}: {y[ind["ind"][0]]}'
            annot.set_text(text)
            annot.set_bbox(
                dict(
                    boxstyle='round',
                    facecolor=self.colors[i],
                    lw=0,
                    alpha=0.8
                )
            )

            # if ax.plot_date
            if isinstance(list(self.data[i].keys())[0], dt.datetime):
                annotx.xy = (x[ind['ind'][0]], 0)
                textx = mdates.num2date(x[ind['ind'][0]]).strftime('%H:%M \n %b %d, %Y')
            # if ax.scatter
            elif isinstance(self.plots[i], matplotlib.collections.PathCollection):
                annotx.xy = (pos[0], 0)
                textx = pos[0]
                annotx.set_text(textx)
            # if ax.plot
            else:
                annotx.xy = (x[ind['ind'][0]], 0)
                k = list(self.data[i].keys())
                textx = f'{k[x[ind["ind"][0]]]}'
            annotx.set_text(textx)

        def hover(event):
            vis = annot.get_visible()
            if event.inaxes:
                for i, plot in enumerate(self.plots):
                    cont, ind = plot.contains(event)
                    if cont:
                        update_annot(i, ind)
                        annot.set_visible(True)
                        annotx.set_visible(True)
                        self.fig.canvas.draw_idle()
                        return
            if vis:
                annot.set_visible(False)
                annotx.set_visible(False)
                self.fig.canvas.draw_idle()

        self.fig.canvas.mpl_connect('motion_notify_event', hover)
        return self
