import matplotlib.pyplot as plt

class Annotation():
    def __init__(self, figure, axes, plots, colors):
        self.fig = figure
        self.ax = axes
        self.plots = plots
        self.colors = colors

    def annotate(self):
        # annotation template
        annot = self.ax.annotate(
            "",
            xy=(0, 0),
            xytext=(15, 20),
            textcoords="offset points",
            arrowprops=dict(arrowstyle='->')
        )

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
            # vis = annot.get_visible()
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
                        else:
                            annot.set_visible(False)
                            self.fig.canvas.draw_idle()

        self.fig.canvas.mpl_connect('motion_notify_event', hover)
        return self
