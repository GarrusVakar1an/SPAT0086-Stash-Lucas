from astropy.io import fits
from astropy.wcs import WCS
from astropy.nddata import Cutout2D
from astroquery.ipac.irsa import Irsa
from astropy.coordinates import SkyCoord
import numpy as np

# FIRST: CREATE an instance of a Skycoord object with the coordinates of the system you want to make a cutout of 

## How large do you want the image cutout to be?
im_cutout = 15 * u.arcsec

coords_cutout =  # FILL - Remember the command to create a SkyCoord object with the coordinates  
search_radius = 1.0 * u.arcsec
# Query Irsa 
# `'euclid_DpdMerBksMosaic'` -- This is the collection of interest for us in this notebook, it contains all the Q1 MER mosaic data. 
image_table = Irsa.query_sia(pos=(coord, search_radius), collection='euclid_DpdMerBksMosaic') 
# Select only science image 
science_images = image_table[image_table['dataproduct_subtype'] == 'science']
# Get the URL of the first image in the table - You may get ground based images but also EURCLID VIS and NISP image (Optical and NIR) 
# You can make cutouts of all the images, but this might be time consuming 
urls = science_images['access_url'] 
# Url for VIS band image only 
#urls_VIS = science_images[science_images['energy_bandpassname'] == 'VIS']['access_url']

# Instead of downloading the full field (> 1 Gb) we will make image cutout on the fly 
 ## Use fsspec to interact with the fits file without downloading the full file
hdu = fits.open(url, use_fsspec=True)
print(f"Opened {url}")

## Store the header
header = hdu[0].header

## Read in the cutout of the image that you want
cutout_data = Cutout2D(hdu[0].section, position=coords_cutout, size=im_cutout, wcs=WCS(hdu[0].header))

## Close the file
# hdu.close()

## Define a new fits file based on this smaller cutout, with accurate WCS based on the cutout size
new_hdu = fits.PrimaryHDU(data=cutout_data.data, header=header)
new_hdu.header.update(cutout_data.wcs.to_header())
