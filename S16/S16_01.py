from astroquery.vizier import Vizier
import matplotlib.pyplot as plt
import astropy.coordinates as coord
import astropy.units as u


cluster_ra = 180.0  
cluster_dec = 0.0
cluster_radius = 0.1  

cluster_coords = coord.SkyCoord(ra=cluster_ra, dec=cluster_dec, unit=(u.deg, u.deg), frame='icrs')

vizier = Vizier(columns=["*", "+_r"])
result = vizier.query_region(cluster_coords, radius=cluster_radius * u.deg, catalog="II/246")

    
plt.figure(figsize=(15, 15))
ax = plt.axes()
ax.set_facecolor("black")

colors = ["lemonchiffon","aqua","lightcoral","lightsalmon","limegreen","slategrey","blue"]
col = 0
constellation = []

ra = result[0]['RAJ2000']
dec = result[0]['DEJ2000']
size = result[0]['Jmag']

for i in range(len(ra)):
    name = coord.get_constellation(coord.SkyCoord(ra[i],dec[i], unit = (u.rad,u.rad)))
    if name not in constellation:
        constellation.append(name)
    plt.plot(ra[i], dec[i], markersize =float(size[i])/2, linestyle='None', c=colors[constellation.index(name)], marker="*", alpha=0.5)
    plt.text(ra[i], dec[i],name,c=colors[constellation.index(name)], fontsize="small")

# with open("./S16/Lyr.txt","r") as f:
#     lines = f.readlines()
# lyr_x = []
# lyr_y = []
# for line in lines:
#     line = line.strip()
#     line = line.split()
#     lyr_x.append(line[0])
#     lyr_y.append(line[1])
# plt.plot(lyr_x, lyr_y, c=colors[constellation.index("Lyra")])

plt.title('Sky Map Chart')
ax.set_yticklabels([])
ax.set_xticklabels([])
plt.savefig("./S16/S16_01.png")
plt.show()
