import numpy as np
import astropy.units as units
import astropy.coordinates as coord
import matplotlib.figure as fig
import matplotlib.backends.backend_agg as back

u_ha = units.hourangle
u_deg = units.deg

data_ra = np.array([])
data_dec = np.array([])
data_l = np.array([])
data_b = np.array([])

with open("./Astro/S09/dataE1.txt","r") as f:
    lines = f.readlines()

for line in lines:
    splitted = line.split()
    ha = float(splitted[-2])
    deg = float(splitted[-1])

    coordinate = coord.SkyCoord(ha,deg,unit=(u_ha,u_deg))

    ra_rad = coordinate.ra.radian
    dec_rad = coordinate.dec.radian

    l_rad = coordinate.galactic.l.radian
    b_rad = coordinate.galactic.b.radian

    if ra_rad > np.pi:
        ra_rad -= 2.0 * np.pi
    if l_rad > np.pi:
        l_rad -= 2.0 * np.pi

    data_ra = np.append(data_ra, ra_rad)
    data_dec = np.append(data_dec, dec_rad)
    data_l = np.append(data_l, l_rad)
    data_b = np.append(data_b, b_rad)
    
gal_lon = np.linspace(0.001 , 359.999 , 1000) * u_deg
gal_lat = np.zeros(1000) * u_deg
gal_coord = coord.Galactic(l = gal_lon, b = gal_lat)
gal_ra = gal_coord.transform_to(coord.ICRS).ra.wrap_at(180.0 * u_deg).radian
gal_dec = gal_coord.transform_to(coord.ICRS).dec.radian

fig = fig.Figure()
canvas = back.FigureCanvasAgg(fig)
ax = fig.add_subplot(111, projection = "aitoff")

ax.grid()

ax.plot(gal_ra, gal_dec, linestyle= "None" ,marker = "o", color = "silver", markersize=5, alpha =0.1)
ax.scatter(data_ra, data_dec, marker = "o", c = "blue", alpha =0.3)

fig.savefig("Astro/S09/E1.png")