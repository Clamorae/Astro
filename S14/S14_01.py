import rebound
import os
import numpy as np

import subprocess
import matplotlib.figure as figure
import matplotlib.pyplot as plt
import astropy.time as time

import matplotlib.backends.backend_agg as agg

# ----------------------------- CREATE SIMULATION ---------------------------- #
sim = rebound.Simulation()

sim.add(m=2.063)
sim.add(m=1.018, a = 7.4957, e = 0.59142)

sim.save_to_file('Sirius.bin')

# ---------------------------- 3D OBJECT CREATION ---------------------------- #
def make_sphere(x_c, y_c, z_c, radius, colour):

    u = np.linspace(0, 2 * np.pi, 1000)
    v = np.linspace(0, np.pi, 1000)
    x = radius * np.outer(np.cos(u), np.sin(v))+ x_c
    y = radius * np.outer(np.sin(u), np.sin(v))+ y_c
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))+ z_c
    sphere = ax.plot_surface(x, y, z, color=colour, antialiased=False, shade=True, rcount=100, ccount=100)

    return(sphere)

# ---------------------------- ORBITAL INTEGRATION --------------------------- #
if not os.path.isfile("./S14/S14_graph000.png"):
    sim.move_to_com()
    part = sim.particles

    year = 2.0 * np.pi
    t_interval = 0.5
    n_output = 500
    dt = 0.01

    sim.integrator = 'ias15'
    sim.dt = dt


    t_epoch = time.Time('2001-02-22T00:00:00', scale='utc', format='isot')
    el0 = 90
    az0 = -90
    zoom0 = 1

    for i in range(n_output):

        t = t_interval * i
        t_yr = t_interval * i /(2.0 * np.pi)
        sim.integrate(t)

        star1_x = part[0].x
        star1_y = part[0].y
        star1_z = part[0].z
        star2_x = part[1].x
        star2_y = part[1].y
        star2_z = part[1].z

        file_fig = f"./S14/S14_graph{i:03d}.png"

        fig = figure.Figure(figsize=[15.36, 8.64,])
        fig.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0, wspace=0.0, hspace=0.0)
        canvas = agg.FigureCanvasAgg(fig)
        ax = fig.add_axes((0, 0, 1, 1), projection='3d')

        ax.set_xlabel('X [au]')
        ax.set_ylabel('Y [au]')
        ax.set_xlim(-25.0, +25.0)
        ax.set_ylim(-25.0, +25.0)
        ax.set_zlim(-25.0, +25.0)
        ax.set_aspect('equal')
        ax.grid()

        ax.plot(float(star1_x), float(star1_y), float(star1_z), linestyle='None', marker='o', markersize=10, color='red', label='Star 1')
        ax.plot(float(star2_x), float(star2_y), float(star2_z), linestyle='None', marker='o', markersize=5, color='blue', label='Star 2')

        #print(f"1x {star1_x}, 1y {star1_y}\n2x {star2_x}, 2y {star2_y}")
        ax.set_title(f"A binary system at {float(t_yr):6.2f} yr")
        ax.legend(loc='upper right')
        fig.savefig(file_fig, dpi=225)
        plt.close(fig)

# -------------------------- CREATE VIDEO FROM IMAGE ------------------------- #
command = "ffmpeg -framerate 30 -pattern_type glob -i './S14/*.png' ./S14/movie_sirius.mp4"
os.system(command)