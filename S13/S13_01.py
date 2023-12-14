import astroquery.simbad as simbad
import astropy.coordinates as coord
import astropy.units as units
import astroquery.skyview as skyview
import astropy
import matplotlib

query_result = simbad.Simbad.query_object("M31")

RA = query_result['RA']
Dec = query_result['DEC']

coordinates = coord.SkyCoord (RA[0], Dec[0], unit=(units.hourangle, units.deg))

list_image = skyview.SkyView.get_image_list (position=coordinates, survey="SDSSr")
print(list_image)
image = skyview.SkyView.get_images(position=coordinates, survey="SDSSr",pixels=1024)

astropy.io.fits.writeto("./S13/1.fits",image[0][0].data)

with astropy.io.fits.open ("./S13/1.fits") as hdu_list:
    header = hdu_list[0].header
    wcs = astropy.wcs.WCS (header)
    image = hdu_list[0].data
