import matplotlib.backends.backend_agg as agg
import photutils.background as background
import astroquery.simbad as simbad
import astropy.coordinates as coord
import astropy.units as units
import astroquery.skyview as skyview
import astropy.wcs as wcs
import matplotlib.backends.backend_agg as agg
import matplotlib.figure as figure
import astropy.stats as stats
import astropy.table as table
import numpy as np
import astropy
import photutils
import astropy
import os
import matplotlib
import astroalign

# ---------------------- RETRIEVE AND DOWLOAD STAR DATA ---------------------- #
if not os.path.isfile("./S13/optical.fits") or not os.path.isfile("./S13/IR.fits"):
    query_result = simbad.Simbad.query_object("Sirius")

    RA = query_result['RA']
    Dec = query_result['DEC']

    coordinates = coord.SkyCoord(RA[0], Dec[0], unit=(units.hour, units.deg))
    image = skyview.SkyView.get_images(position=coordinates, survey="2MASS-J",pixels=1024)
    astropy.io.fits.writeto("./S13/optical.fits",image[0][0].data,overwrite=True)

    ir_ra_decimal = coordinates.ra.deg + 1 /60
    ir_dec_decimal = coordinates.dec.deg + 2 /60

    ir_coordinates = coord.SkyCoord(ir_ra_decimal,ir_dec_decimal, unit=(units.deg, units.deg))
    ir_image = skyview.SkyView.get_images(position=ir_coordinates, survey = "2MASS-J", pixels=1024)
    astropy.io.fits.writeto("./S13/IR.fits",ir_image[0][0].data,overwrite=True)

# ---------------------- CREATE AND PRINT OPTICAL IMAGE ---------------------- #
    with astropy.io.fits.open("./S13/optical.fits") as hdu_list:
        header = hdu_list[0].header
        wcs_head= wcs.WCS(header)
        image = hdu_list[0].data

    fig= matplotlib.figure.Figure()
    canvas = agg.FigureCanvasAgg(fig)
    ax = fig.add_subplot(111, projection=wcs_head)

    norm = astropy.visualization.mpl_normalize.ImageNormalize( stretch=astropy.visualization.HistEqStretch(image) )
    im = ax.imshow(image, origin='lower', cmap="grey", norm=norm)
    fig.savefig("./S13/optical.png", dpi=150)
    fig.clf()

# ------------------------- CREATE AND PRINT IR IMAGE ------------------------ #
    with astropy.io.fits.open("./S13/IR.fits") as hdu_list:
        header = hdu_list[0].header
        wcs_head= wcs.WCS(header)
        image = hdu_list[0].data

    canvas = agg.FigureCanvasAgg(fig)
    ax = fig.add_subplot(111, projection=wcs_head)

    norm = astropy.visualization.mpl_normalize.ImageNormalize( stretch=astropy.visualization.HistEqStretch(image) )
    im = ax.imshow(image, origin='lower', cmap="grey", norm=norm)
    fig.savefig("./S13/IR.png", dpi=150)

# ---------------------------- CATALOGUE CREATION ---------------------------- #
def catalogue_creation(input):
    sigma_sky = 3.0
    maxiters = 10
    box_size = 50
    filter_size = 3
    thresh = 2
    kernel = 3.0
    array_size = 5
    nb_pixel = 10

    with astropy.io.fits.open("./S13/"+input+".fits") as hdu:
        header = hdu[0].header
        image = hdu[0].data
        if(header['NAXIS'] == 0):
            header = hdu[1].header
            image = hdu[1].data
    sigma_clip = stats.SigmaClip(sigma=sigma_sky, maxiters=maxiters)
    skybg_estimator = background.SExtractorBackground()

    image_skybg = background.Background2D(image, box_size=(box_size, box_size), filter_size=(filter_size, filter_size), sigma_clip=sigma_clip, bkg_estimator=skybg_estimator)
    image_skysub = image - image_skybg.background
    detection_threshold = thresh * image_skybg.background_rms_median
    convolution_kernel = photutils.segmentation.make_2dgaussian_kernel(fwhm=kernel, size=array_size)
    image_convolved = astropy.convolution.convolve(image_skysub, convolution_kernel)
    image_segmented = photutils.segmentation.detect_sources(image_convolved, detection_threshold, npixels=nb_pixel)
    catalogue = photutils.segmentation.SourceCatalog(data=image_skysub, segment_img=image_segmented, convolved_data=image_convolved)
    table_source = catalogue.to_table()
    astropy.io.ascii.write(table_source, "./S13/"+input+".cat", format='commented_header')

if not os.path.isfile("./S13/optical.cat") or not os.path.isfile("./S13/IR.cat"):
    catalogue_creation("optical")
    catalogue_creation("IR")

# -------------------------- LOOKING FOR COMMON STAR ------------------------- #
table1 = table.Table.read("./S13/optical.cat",format='ascii.commented_header')
table2 = table.Table.read("./S13/IR.cat",format='ascii.commented_header')

list_source1_x = list (table1['xcentroid'])
list_source1_y = list (table1['ycentroid'])
list_source2_x = list (table2['xcentroid'])
list_source2_y = list (table2['ycentroid']) 
position_1= np.transpose ( (list_source1_x, list_source1_y) )
position_2= np.transpose ( (list_source2_x, list_source2_y) )

transf, (list_matched_2, list_matched_1) = astroalign.find_transform (position_2, position_1)
list_matched_2_aligned = astroalign.matrix_transform (list_matched_2, transf.params)

# ------------------------------ STAR ALIGNEMENT ----------------------------- #
# --------- THIS PART IS COMING FROM THE COURSE SINCE IN COULDNT TEST -------- #

(header1, image1) = astropy.read_fits("./S13/optical.fits")
(header2, image2) = astropy.read_fits("./S13/IR.fits")

image1 = image1.byteswap ().newbyteorder ()
image2 = image2.byteswap ().newbyteorder ()


st = coord.skimage.transform.SimilarityTransform (scale=transf.scale, rotation=transf.rotation, translation=transf.translation)
image2_aligned = coord.skimage.transform.warp (image2, st.inverse)

markers = ['o', 'v', '^', 's', 'p', 'h', '8']
colours = ['maroon', 'red', 'coral', 'bisque', 'orange', 'wheat', 'yellow', 'green', 'lime', 'aqua', 'skyblue', 'blue', 'indigo', 'violet', 'pink']

fig = figure.Figure ()
agg.FigureCanvasAgg (fig)
ax1 = fig.add_subplot (121)
ax2 = fig.add_subplot (122)

norm1 = astropy.visualization.mpl_normalize.ImageNormalize ( stretch=astropy.visualization.HistEqStretch (image1) )
im1 = ax1.imshow (image1, origin='lower', cmap='bone', norm=norm1)
for i in range ( len (list_matched_1) ):
    i_marker = i % len (markers)
    i_colour = i % len (colours)
    ax1.plot (list_matched_1[i][0], list_matched_1[i][1], marker=markers[i_marker], color=colours[i_colour], markersize=8, fillstyle='none')
ax1.set_title ('First Image')


norm2 = astropy.visualization.mpl_normalize.ImageNormalize ( stretch=astropy.visualization.HistEqStretch (image2_aligned) )
im2 = ax2.imshow (image2_aligned, origin='lower', cmap='bone', norm=norm2)
for i in range ( len (list_matched_2_aligned) ):
    i_marker = i % len (markers)
    i_colour = i % len (colours)
    ax2.plot (list_matched_2_aligned[i][0], list_matched_2_aligned[i][1], marker=markers[i_marker], color=colours[i_colour], markersize=8, fillstyle='none')
ax2.set_title ('Second Image')
fig.tight_layout ()
fig.savefig ("./S13/final.png", dpi=150)