import os
import ssl
import numpy as np
import astropy.units as units
import astroquery.gaia as gaia
import matplotlib.figure as figure
import astroquery.simbad as simbad
import astropy.coordinates as coord
import astropy.io.votable as votable
import matplotlib.backends.backend_agg as agg

if os.path.isfile("./S11/t10.vot.gz") == False:
    ssl._create_default_https_context = ssl._create_unverified_context

    gaia.Gaia.MAIN_GAIA_TABLE ="gaiadr3.gaia_source"
    gaia.Gaia.ROW_LIMIT = -1

    target ="Trumpler 10"
    file_output ="./S11/t10.vot.gz"
    radius_arcmin = 30.0
    radius_deg = radius_arcmin / 60.0

    u_deg = units.deg
    u_ha = units.hourangle
    u_arcmin = units.arcmin

    result_simbad = simbad.Simbad.query_object(target)

    obj_ra = result_simbad["RA"][0]
    obj_dec = result_simbad["DEC"][0]

    coord = coord.SkyCoord(obj_ra, obj_dec, frame ="icrs", unit =(u_ha, u_deg))

    ra_deg = coord.ra.deg
    dec_deg = coord.dec.deg

    table = f"gaiadr3.gaia_source"
    field = f"*"
    point = f"POINT({ra_deg:8.4f} ,{dec_deg:8.4f})"
    circle = f"CIRCLE(ra, dec ,{radius_deg})"
    query = f"SELECT{field} from {table} WHERE 1= CONTAINS({point} ,{circle});"



    job = gaia.Gaia.launch_job_async(query, dump_to_file = True, output_format ="votable", output_file = file_output)
    result = job.get_results()
  
        

table = votable.parse_single_table("./S11/t10.vot.gz").to_table()

data_parallax = np.array(table ["parallax"])
data_g = np.array(table ["phot_g_mean_mag"])
data_br = np.array(table["bp_rp"])
colour = np.array(table["pseudocolour"])

distance = np.array([])

for parallax in data_parallax:
    if np.isnan(parallax) or parallax<=0:
        distance = np.append(distance,-1.0)
    else:
        distance = np.append(distance,1000/parallax)
    

data_g_abs = data_g + 5.0 * np.log10(distance/1000)+5

list_ms_colour = np.array([])
list_ms_absmag = np.array([])

for items,color_br in zip(data_g_abs,colour):
    try :
        colour_br = color_br
    except :
        colour_br = 999.999


    if ((colour_br < 100.0) and (items < 100.0)):
        list_ms_colour = np.append(list_ms_colour,colour_br)
        list_ms_absmag = np.append(list_ms_absmag, items)

data_ms_colour = np.array(list_ms_colour)
data_ms_absmag = np.array(list_ms_absmag)

fig = figure.Figure()
canvas = agg.FigureCanvasAgg(fig)
ax = fig.add_subplot(111)

ax.plot(data_br, data_g_abs, linestyle="None", marker ="o", markersize =3, color ="blue", zorder =0.2)
ax.plot(data_ms_colour, data_ms_absmag, linestyle="-", linewidth = 10, color ="orange", alpha =0.5, zorder =0.1)

# saving file
fig.savefig("./S11_01")