# ---------------------- RETRIEVE AND DOWLOAD STAR DATA ---------------------- #
if not os.path.isfile("./S13/optical.fits") or not os.path.isfile("./S13/IR.fits"):
    query_result = simbad.Simbad.query_object("M31")

    RA = query_result['RA']
    Dec = query_result['DEC']

    coordinates = coord.SkyCoord(RA[0], Dec[0], unit=(units.deg, units.deg))
    image = skyview.SkyView.get_images(position=coordinates, survey="SDSSr",pixels=1024)
    astropy.io.fits.writeto("./S13/optical.fits",image[0][0].data,overwrite=True)

    ir_ra_decimal = coordinates.ra.deg + 15 /60
    ir_dec_decimal = coordinates.dec.deg + 14 /60

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