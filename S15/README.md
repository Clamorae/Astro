V/137D        Extended Hipparcos Compilation (XHIP)          (Anderson+, 2012)
================================================================================
XHIP: An Extended Hipparcos Compilation
     Anderson E., Francis C.
    <Astron. Letters 38 (2012)>
   =2012AstL...38..331A  (http://arxiv.org/abs/1108.4971)
   =2012PAZh...38..374A
   =2012yCat.5137....0A
================================================================================
ADC_Keywords: Stars, bright ; Combined data ; Cross identifications ;
              Positional data ; Parallaxes, trigonometric ; Proper motions ;
              Stars, distances ; Spectral types ; Radial velocities ;
              Abundances, [Fe/H] ; Stars, ages ; Space velocities ;
              Milky Way; Clusters, open; Associations, stellar;
              Photometry, UBVRI ; Photometry, infrared
Keywords: astrometry;  spectrography ; radial velocities ;
          spectral classifications ; iron abundances ; photometry ;
          solar neighbourhood ; kinematics ; open clusters;
          stellar associations; exoplanets ; photometry

Description:
    The  Extended  Hipparcos  Compilation (XHIP) cross-references  the New
    Hipparcos  Reduction  (HIP2, Cat. I/311)  with  relatable  data from a
    broad survey of presently available sources.  The resulting collection
    uniquely  assigns  116,096  spectral  classifications,   46,392 radial
    velocities,  and  19,097 iron  abundances  [Fe/H]  to Hipparcos stars.
    Stellar classifications  from  SIMBAD and  indications of multiplicity
    from  either   CCDM (Cat. I/274)  or  WDS (Cat. B/wds)  are  provided.
    Parameters for solar encounters and Galactic orbits are calculated for
    a  subset   of  stars   that  can  be  made   kinematically  complete.
    Memberships in  open clusters and  stellar associations  are assigned.
    We also provide stellar ages from  The Geneva-Copenhagen survey of the
    Solar neighbourhood III  (Cat. V/130),  identifications  of  exoplanet
    host stars,  and supplemental photometry from  2MASS (Cat. II/246) and
    SIMBAD.


File Summary:
--------------------------------------------------------------------------------
 FileName  Lrecl  Records  Explanations
--------------------------------------------------------------------------------
ReadMe        80        .  This file
main.dat     417   117955  Astrometry, spectrography, space motions, exoplanets
photo.dat    235   117955  Photometry
biblio.dat   376   117955  References
refs.dat      23      674  Reference key for r_RV & r_[Fe/H]
groups.dat   318       87  Statistics on open clusters and stellar associations
--------------------------------------------------------------------------------

See also:
          I/239 : The Hipparcos and Tycho Catalogues
          I/274 : Catalog of Components of Double & Multiple stars
          I/311 : Hipparcos, the New Reduction
         II/246 : 2MASS All-Sky Catalog of Point Sources
        III/252 : Pulkovo radial velocities for 35,493 HIP stars
          V/130 : Geneva-Copenhagen Survey of Solar neighbourhood III
           B/mk : Catalogue of Stellar Spectral Classifications
          B/ocl : Optically visible open clusters and Candidates
       B/pastel : The PASTEL catalogue of stellar atmospheric parameters
          B/wds : The Washington Visual Double Star Catalog
  J/A+A/477/165 : Tidal radii and masses of open clusters


Byte-by-byte Description of file: main.dat
--------------------------------------------------------------------------------
   Bytes Format  Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  6  I6     ---     HIP       Hipparcos identifier
   8- 13  A6     ---     Comp      Component(s) (1)
  15- 55  A41    ---     Classes   SIMBAD classifications (comma separated) (2)
      57  I1     ---     Gr        ? Cluster or Association membership(s) (3)
  59- 70  F12.8  deg     RAdeg     Right ascension (ICRS, Epoch=J1991.25)
  72- 83  F12.8  deg     DEdeg     Declination (ICRS, Epoch=J1991.25)
  85- 90  F6.2   mas     Plx       Trigonometric parallax
  92- 99  F8.2   mas/yr  pmRA      Proper motion in RA*cos(DEdeg)
 101-108  F8.2   mas/yr  pmDE      Proper motion in Declination
 110-115  F6.2   mas   e_RAdeg     Standard error on RA*cos(DEdeg)
 117-122  F6.2   mas   e_DEdeg     Standard error on DE
 124-128  F5.2   mas   e_Plx       Standard error on Plx
 130-135  F6.2 mas/yr  e_pmRA      Standard error on pmRA
 137-141  F5.2 mas/yr  e_pmDE      Standard error on pmDE
     143  I1     ---   r_HIP       [1/2] Reference for Hipparcos astrometry (4)
     145  I1     ---   r_pm        [1/3] Reference for proper motion (5)
 147-158  F12.8  deg     GLon      Galactic longitude (6)
 160-171  F12.8  deg     GLat      Galactic latitude (6)
 173-179  F7.2   pc      Dist      ? Heliocentric distance (7)
 181-184  F4.1   %     e_Dist      ? Distance error expressed as percentage (8)
 186-193  F8.2   mas/yr  pmGLon    Proper motion in GLon*cos(GLat)
 195-202  F8.2   mas/yr  pmGLat    Proper motion in GLat
 204-209  F6.1   pc      X         ? Heliocentric distance towards Gal. center
 211-217  F7.1   pc      Y         ? Heliocentric distance towards Gal. rotation
 219-224  F6.1   pc      Z         ? Heliocentric distance towards N. Gal. Pole
 226-229  I4     pc      RGal      ? Galactocentric distance (9)
 231-235  F5.1   km/s    vT        ? Transverse velocity
 237-262  A26    ---     SpType    Spectral type (MK, HD, or other)
 264-266  I3     ---     Tc        ]0/140[? Temperature class codified (10)
     268  I1     ---     Lc        [1/6]? Luminosity class codified (11)
 270-276  F7.2   km/s    RV        ? Radial velocity
 278-283  F6.2   km/s  e_RV        ? Standard error on RV (12)
     285  A1     ---   q_RV        [ABCD] Quality flag on RV (13)
 287-291  F5.2  [Sun]    [Fe/H]    ? Iron abundance
 293-296  F4.2  [Sun]  e_[Fe/H]    ? Standard error on [Fe/H] (14)
     298  A1     ---   q_[Fe/H]    [ABC] Quality flag on [Fe/H] (15)
 300-303  F4.1   Gyr     age       ? Age, in billions of years
 305-308  F4.1   Gyr   b_age       ? Lower confidence limit on age
 310-313  F4.1   Gyr   B_age       ? Upper confidence limit on age
 315-320  F6.1   km/s    U         ? Heliocentric velocity towards Gal. center
 322-327  F6.1   km/s    V         ? Heliocentric velocity towards Gal. rotation
 329-334  F6.1   km/s    W         ? Heliocentric velocity towards N. Gal. Pole
 336-340  F5.1   km/s    UVW       ? Total heliocentric velocity
 342-348  F7.2   pc      Dmin      ? Minimum distance at solar encounter (16)
 350-354  I5     kyr     Tmin      ? Timing of Dmin, in thousands of years (17)
 356-361  F6.4   ---     e         ? Total orbital eccentricity (18)
 363-368  F6.1   deg     phi       [-180/180]? Pericenter position angle (18)
 370-376  I7     pc      a         ? Semi-major axis of orbit (18)
 378-382  I5     pc      b         ? Semi-minor axis of orbit (18)
 384-390  I7     pc      c         ? Focus-to-center distance of orbit (18)
 392-396  I5     deg     L         ? Semilatus rectum of orbit (18)
 398-401  I4     pc      Rmin      ? Orbital radius at pericenter (18)
 403-409  I7     pc      Rmax      ? Orbital radius at apocenter (18)
     411  I1     ---     Npl       ? Number of exoplanets (known in April 2012)
 413-417  A5     ---     Mpl       Exoplanet discovery method(s) (19)
--------------------------------------------------------------------------------

Note (1): from CCDM (Cat. I/274) or WDS (Cat. B/wds)

Note (2): object types, see
     http://simbad.u-strasbg.fr/simbad/sim-display?data=otypes

Note (3): Group IDs are in biblio.dat (GrpName)
     see also: groups.dat and Cat. B/Ocl

Note (4): flag indicates astrometry source:
     1 = HIP (Cat. I/239) for 3,504 problematic cases in HIP2
     2 = HIP2 (Cat. I/311) for all remaining cases

Note (5): flag indicates the following:
     1 = From HIP2 (Cat. I/311)
     2 = From Tycho-2 (Cat. I/259)
     3 = HIP2 & Tycho-2 combined for improved error bounds

Note (6): transformation from ICRS defined by:
     NGP RAdeg = 192.85948,
     NGP DEdeg = +27.12825,
     GLon of ascending node @ celestial equator = 32.93192 deg

Note (7): null where parallax errors <20%
     Dist = 1000/Plx * (1+1.2*(e_Plx/Plx)^2^)

Note (8): null where Dist is fitted to cluster

Note (9): adopts Sgr A* (X,Y,Z) as (7400,-7.2,-6.0) pc

Note (10): Temperature classes are:
      O=10 B=20 A=30 F=40 G=50 K=60 M=70
      L=80 T=90 S=100 C=110 R=120 N=130
      Subclasses 0-9 are additionally summed.

Note (11): I=1 II=2 III=3 IV=4 V=5 VI=6

Note (12): 999 = error not available though RV is available

Note (13): quality flag means:
       A = Most likely to be within stated error bounds
       B = May have small systematic errors
       C = May have larger systematic errors
       D = No error available or other serious problems

Note (14): 9.99 = error not available though [Fe/H] is available

Note (15): quality flag means:
       A = Calibrated
       B = Calibrated, but no error bounds assigned
       C = Uncalibrated and no error bounds assigned

Note (16): based on linear approximation to space motion

Note (17): Past times are negative; future times positive

Note (18): LSR (U,V,W) = (14.1,14.6,6.9) km/s are
      adopted.  Note (9) above with regard to Rgal also applies.

Note (19): method is codified:
     RA = "radial velocity or astrometric methods"
     I  = "imaging"
     T  = "timing"
     X  = "transit"

--------------------------------------------------------------------------------

Byte-by-byte Description of file: photo.dat
--------------------------------------------------------------------------------
   Bytes Format  Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  6  I6     pc      HIP       Hipparcos identifier
   8- 14  F7.4   mag     Hpmag     Median magnitude in Hipparcos system
  16- 21  F6.4   mag   e_Hpmag     Standard error on Hpmag
      23  A1     ---   m_Hpmag     [A-Z*-] Reference flag for Hpmag (20)
  25- 29  F5.2   mag     Hpmax     ? Hpmag at maximum (5th percentile)
  31- 35  F5.2   mag     Hpmin     ? Hpmag at minimum (95th percentile)
  37- 42  F6.2   d       Per       ? Variability period
      44  A1     mag     Hvar      [CDMPRU] Variability type (21)
  46- 51  F6.3   mag     Umag      ? Apparent magnitude in Johnson U
  53- 58  F6.3   mag     Bmag      ? Apparent magnitude in Johnson B
  60- 64  F5.2   mag     Vmag      Apparent magnitude in Johnson V
  66- 70  F5.2   mag     Rmag      ? Apparent magnitude in R
  72- 77  F6.3   mag     Imag      ? Apparent magnitude in I
  79- 84  F6.3   mag     Jmag      ? J selected default magnitude (22)
  86- 91  F6.3   mag     Hmag      ? H selected default magnitude (22)
  93- 98  F6.3   mag     Kmag      ? K selected default magnitude (22)
 100-104  F5.3   mag   e_Jmag      ? J total magnitude uncertainty (22)
 106-110  F5.3   mag   e_Hmag      ? H total magnitude uncertainty (22)
 112-116  F5.3   mag   e_Kmag      ? K total magnitude uncertainty (22)
 118-134  A17    ---     2MASS     2MASS source designation (22)
 136-138  A3     ---     q2M       JHK photometric quality flag (22)
 140-145  F6.3   mag     B-V       ? Johnson B-V color index
 147-151  F5.2   mag     V-I       ? Color index in Cousins' system
 153-157  F5.3   mag   e_B-V       ? Standard error on B-V
 159-162  F4.2   mag   e_V-I       ? Standard error on V-I
 164-169  F6.3   mag     HpMag     ? Absolute Magnitude of Hpmag (23)
 171-176  F6.3   mag     UMag      ? Absolute Magnitude in Johnson U (23)
 178-182  F5.2   mag     BMag      ? Absolute Magnitude in Johnson B (23)
 184-188  F5.2   mag     VMag      ? Absolute Magnitude in Johnson V (23)
 190-194  F5.2   mag     RMag      ? Absolute Magnitude in R (23)
 196-200  F5.2   mag     IMag      ? Absolute Magnitude in I (23)
 202-206  F5.2   mag     JMag      ? Absolute Magnitude J (23)
 208-212  F5.2   mag     HMag      ? Absolute Magnitude H (23)
 214-219  F6.2   mag     KMag      ? Absolute Magnitude K (23)
 221-229  F9.2   Lsun    Lum       ? Stellar luminosity (23)
 231-235  F5.2   mag     magmin    ? Apparent magnitude V at Tmin (main.dat)
--------------------------------------------------------------------------------
Note (20): this flag indicates for double or multiple entries:
     A to Z = the letter indicates the specified component measured
     * = combined Hpmag of a double system, corrected for attenuation
     - = combined Hpmag of a multiple system, not corrected for attenuation

Note (21): Hipparcos-defined type of variability
 blank = entry could not be classified as variable or constant
     C = no variability detected ("constant")
     D = duplicity-induced variability
     M = possibly micro-variable (amplitude < 0.03mag)
     P = periodic variable
     R = V-I colour index was revised due to variability analysis
     U = unsolved variable which does not fall in the other categories

Note (22): See Cat. II/246

Note (23): does not factor absorption
      by the interstellar medium; may also contain integrated components.

--------------------------------------------------------------------------------

Byte-by-byte Description of file: biblio.dat
--------------------------------------------------------------------------------
   Bytes Format  Units   Label     Explanations
--------------------------------------------------------------------------------
   1-  6  I6     ---     HIP       Hipparcos identifier
   8- 13  I6     ---     HD        ? Henry Draper catalog identifier
  15- 17  A3     ---     Cst       Constellation membership
  19- 22  I4     ---     Atlas     Millennium Star Atlas page number
  24- 33  A10    ---     Coords    RA, DE in compact format; n = + ; s = -
  35- 82  A48    ---     Name      Star name(s)
  84-189  A106   ---     GrpName   Cluster or Association name(s)
 191-206  A16    ---     CompID    Reference for Comp (main.dat)
 208-232  A25    ---     rSpType   Reference for SpType (main.dat) (24)
 234-248  A15    ---   r_RV        Reference for RV (main.dat)
 250-376  A127   ---   r_[Fe/H]    Reference(s) for [Fe/H] (main.dat)
--------------------------------------------------------------------------------
Note (24): BibCodes "1993BICDS..43....5T" & "2003AJ....125..359W" are
     augmented (after a colon :) with the content of the r_Sp or r_SpType
     columns from those sources respectively.
--------------------------------------------------------------------------------

Byte-by-byte Description of file: refs.dat
--------------------------------------------------------------------------------
   Bytes Format  Units   Label    Explanations
--------------------------------------------------------------------------------
   1-  3  I3     ---     KeyCode  [1,703] 3-digit shorthand code (25)
   5- 23  A19    ---     BibCode  Corresponding 19-digit bibliographic code (26)
--------------------------------------------------------------------------------

Note (25): Range of key code:
  * [001-176]: Calibrated [Fe/H] sources
  * [201-495]: Uncalibrated [Fe/H] sources
  * [501-703]: Radial velocity sources

Note (26): Radial velocities obtained through SIMBAD having no source
     reference are indicated with the pseudo-code "2010.........SIMBAD"

--------------------------------------------------------------------------------

Byte-by-byte Description of file: groups.dat
--------------------------------------------------------------------------------
   Bytes Format  Units   Label    Explanations
--------------------------------------------------------------------------------
   1- 21  A21    ---     GrpName  Group name
  23- 43  A21    ---     AltName  Alternative group name
  45- 47  I3     ---     N        Number of Hiipparcos candidate stars
  49- 52  F4.1   ---     n        [3.5/16] Separation parameter (27)
  54- 66  A13    ---     Stream   Kinematic group (28)
  68- 73  F6.2   deg     RAdeg    Group mean right ascension (ICRS)
  75- 80  F6.2   deg     DEdeg    Group mean declination (ICRS)
  82- 87  F6.1   pc      Dist     Group mean parallax distance
  89- 94  F6.1 mas/yr    pmRA     Group mean proper motion in RA*cos(DEdeg)
  96-101  F6.1 mas/yr    pmDE     Mean proper motion in declination
 103-107  F5.1   km/s    RV       Group mean radial velocity
 109-114  F6.2   deg   s_RAdeg    Group width on RA*cos(DEdeg) (1-{sigma})
 116-121  F6.2   deg   s_DEdeg    Group width on DE (1-{sigma})
 123-128  F6.1   pc    s_Dist     Group width on Dist (1-{sigma})
 130-134  F5.1 mas/yr  s_pmRA     Group width on pmRA (1-{sigma})
 136-140  F5.1 mas/yr  s_pmDE     Group width on pmDE (1-{sigma})
 142-145  F4.1   km/s  s_RV       Group width on radial velocity
 147-151  F5.2   deg   e_RAdeg    Standard error on RA*cos(DEdeg)
 153-157  F5.2   deg   e_DEdeg    Standard error on DE
 159-164  F6.1   pc    e_Dist     Standard error on Dist
 166-169  F4.1 mas/yr  e_pmRA     Standard error on pmRA
 171-174  F4.1 mas/yr  e_pmDE     Standard error on pmDE
 176-179  F4.1   km/s  e_RV       Standard error on radial velocity
 181-185  F5.1   pc      rad      Physical radius (1-{sigma})
 187-191  F5.1   deg     arad     Angular radius (1-{sigma})
 193-198  F6.1   pc      X        Heliocentric distance towards Gal. center
 200-205  F6.1   pc      Y        Heliocentric distance towards Gal. rotation
 207-212  F6.1   pc      Z        Heliocentric distance towards N. Gal. Pole
 214-218  F5.1   km/s    U        Heliocentric velocity towards Gal. center
 220-224  F5.1   km/s    V        Heliocentric velocity towards Gal. rotation
 226-230  F5.1   km/s    W        Heliocentric velocity towards N. Gal. Pole
 232-236  F5.1   pc    s_X        Group width on X (1-{sigma})
 238-242  F5.1   pc    s_Y        Group width on Y (1-{sigma})
 244-248  F5.1   pc    s_Z        Group width on Z (1-{sigma})
 250-253  F4.1   km/s  s_U        Group width on U (1-{sigma})
 255-258  F4.1   km/s  s_V        Group width on V (1-{sigma})
 260-263  F4.1   km/s  s_W        Group width on W (1-{sigma})
 265-269  F5.1   pc    e_X        Standard error on X
 271-275  F5.1   pc    e_Y        Standard error on Y
 277-281  F5.1   pc    e_Z        Standard error on Z
 283-285  F3.1   km/s  e_U        Standard error on U
 287-289  F3.1   km/s  e_V        Standard error on V
 291-293  F3.1   km/s  e_W        Standard error on W
 295-299  F5.2   [Sun]   [Fe/H]   ? Iron abundance
 301-304  F4.2   [Sun] e_[Fe/H]   ? Standard error on [Fe/H]
 306-308  I3     ---   n_[Fe/H]   ? Number of Hipparcos member stars with [Fe/H]
 310-313  F4.2   mag     E(B-V)1  ? Color excess in B-V, CDS Cat. B/ocl
 315-318  F4.2   mag     E(B-V)2  ? Color excess in B-V, CDS Cat. J/A+A/477/165
--------------------------------------------------------------------------------
Note (27): the separation parameter n is a measure of the concentration of
     a cluster, and of its separation from the surrounding star field (low
     values show poor dynamical separation from surrounding stars). A value
     of 5 is usual for a cluster, while 3.5 is typical for an
     association.

Note (28): see 2012MNRAS.422.1283F (arXiv:1202.1375)
--------------------------------------------------------------------------------

History:
  * 17-Aug-2011: First (original) version

  * 01-Feb-2012: Version 'A' (from the author)
           with the following modifications:
    -- main.dat: 'Planets' and 'Methods' columns brought up to date.
    -- biblio.dat: added 'HD' column (by request);
       'GrpName' column had a few minor changes
    -- groups.dat : renamed column 'n' to 'N', and made new column 'n' for
       'separation parameter'

  * 15-Mar-2012: Version 'B' (from the author)
           with the following modifications:
    -- main.dat: Corrected e_plx values where r_HIP=1
    -- groups.dat: added 14 new columns: AltName, Stream, & Group width cols

  * 30-Apr-2012: Version 'C' (from the author)
           with the following modifications:
    -- main.dat: corrected 22 entries in column 'Lc' where SpType contains "VI"
    -- main.dat: columns "Npl" and "Mpl" brought up to date.

  * 28-Jan-2013: Version 'D' (from the author)
           with the following modifications:
    -- main.dat: revised/corrected 623 entries in columns 'RV' and/or 'e_RV'
                 where 'r_RV' in biblio.dat contains "577"
    -- main.dat: revised columns pertaining to Note(18) to reflect revised
                 estimate of LSR (U,V) from (14.0,14.5) to (14.1,14.6)
    -- main.dat: columns "Npl" and "Mpl" brought up to date.
    -- main.dat: corrected SpType for HIP 32067
    -- biblio.dat: revised r_SpType for HIP 32067

================================================================================
(End)   Erik Anderson [astrostudio.org], Francois Ochsenbein [CDS]   28-Jan-2013