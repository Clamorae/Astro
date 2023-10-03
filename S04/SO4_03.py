import numpy as np
import matplotlib.backends.backend_agg
import matplotlib.figure as fig

figure =fig.Figure()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg(figure)
ax = figure.add_subplot(111)
