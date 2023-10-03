import numpy as np
import matplotlib.backends.backend_agg
import matplotlib.figure as fig
import matplotlib.animation as animation

#y = x tan θ − gx2/2v2 cos2 θ
theta = np.radians(30)
g = 9.81
v = 30
total_time = (2 * v * np.sin(theta)) / g

nb_frame = 60
frames = []
figure = fig.Figure()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg(figure)
ax = figure.add_subplot(111)

for i in range(nb_frame):
    ax.set_xlim(0,100)
    ax.set_ylim(0,30)

    t = (i / (nb_frame - 1)) * total_time

    x = v * t * np.cos(theta)
    y = v * t * np.sin(theta) - (0.5 * g * t**2)

    point, = ax.plot(x,y,"bo")#i, i*np.tan(theta) - g*i**2/2*v**2*np.cos(theta)**2,"bo")
    ax.set_aspect("equal")
    frames.append([point])

anim = animation.ArtistAnimation(figure,frames,interval = 50)
anim.save("3.mp4",dpi = 225)

