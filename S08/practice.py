import matplotlib.figure as fug
import matplotlib.backends.backend_agg as back

with open("./Astro/S08/pdata.txt","r") as f:
    lines = f.readlines()

wavelength = []
flux = []
reference = []
err = []

test = False
for line in lines:
    if line != "\n":
        splitted = line.split()
        try:
            wavelength.append(float(splitted[0]))
        except:
            continue
        flux.append(float(splitted[1]))
        err.append(float(splitted[3]))
        try:
            reference.append(float(splitted[4]))
        except:
            wavelength = wavelength[:-1]
            flux = flux[:-1]
            err = err[:-1]

fig = fug.Figure ()
canvas = back.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)
ax.set_xlabel ("Wavelength [$\mu$m]")
ax.set_ylabel ("Flux [Jy]")
ax.errorbar (wavelength , flux , yerr= err , \
linestyle="None", marker="o", markersize=5, color="red", \
ecolor="black", elinewidth=2, capsize=5, \
label="HD61005")
ax.set_xscale ("log")
ax.set_yscale ("log")
ax.legend ()
fig.savefig("./Astro/S08/fig.png")