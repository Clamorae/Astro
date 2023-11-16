import astropy.coordinates as coord
import astropy.units as unit
import astropy.time as time
import astroquery.simbad

u_m = unit.m

centre_l = 0.0 * unit.degree
centre_b = 0.0 * unit.degree

t_str = "2023-10-28 21:00:00"
t_utc = time.Time (t_str , format="iso", scale="utc")

longitude = "121d11m12s"
latitude = "+24d58m12s"
height = 151.6 * u_m
observer = coord.EarthLocation(longitude, latitude, height)


query_result = astroquery.simbad.Simbad.query_object ("Antares")
ra_str = query_result["RA"][0]
dec_str = query_result["DEC"][0]
                       
antares = coord.SkyCoord(ra_str, dec_str , frame="icrs", unit=(unit.hourangle , unit.deg) )
centre = coord.SkyCoord(l=centre_l , b=centre_b , frame="galactic")
print(f"The angular distance is {centre.separation(antares)}")