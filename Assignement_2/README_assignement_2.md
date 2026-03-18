The catalog q1_MER_morph_EDFN_w_score_4students.fits.gz located in https://dox.uliege.be/index.php/s/mqdX4hxLkZ62wUL is the parent catalog of objects where the lensed candidates have been identified using different "lens search engines".

Your task:

Understand what information is in that catalog.

- How many objects are present in that catalog?
- How many columns does it contain? Are they all filled with values?
- Do all columns contain sensible information for machine learning classification tasks? 
- Some lenses from `q1_lens_search_EDFN_4students.csv` are in that table. Which ones? Is it a problem?
- What are the lens engine scores for the lenses? Plot their distribution.
- Are all engines equivalent? Is there a methodology you can use to compare the performances of the different engines (you might have to wait the end of the ML lectures to answer that question). 

**Descritpion of the columns**

The columns of that catalog combines columns from the so called Euclid "MER" catalogue (http://st-dm.pages.euclid-sgs.uk/data-product-doc/dm10/merdpd/merphotometrycookbook.html#total-fluxes) that typically makes the object detection and reports the object photometry; from the "MORPHOLOGICAL" catalog (http://st-dm.pages.euclid-sgs.uk/data-product-doc/dm10/merdpd/mermorphologycookbook.html) and some columns corresponding to the scores of the lens search engines (lens_score_a -> f). Some additional columns contain object identifer and ID of the the image from which the detection is perfromed (tile_index).

The photometric data contained in those table correspond to data obtained in 4 bands: VIS (optical), Y-J-H (Near-infred). There is an additional "joined NIR" photometry  

Brief description of the main columns:

'basic_download_data_oid',    Some sort of data identified (irrelevant)
 'RA',			      Right ascention of hte object
 'DEC',			      Declination of the object
 'object_id',		      Object identifier
 'id_str',		      Alternative object identifier
 'tile_index',		      Tile index

MER Photometry information: 
 'flux_vis_1fwhm_aper',	            Aperture photometry - 1FWHM - VIS BAND
 'flux_vis_2fwhm_aper',	    	    Aperture photometry - 2FWHM - VIS BAND
 'flux_vis_3fwhm_aper',     	    Aperture photometry - 3FWHM - VIS BAND
 'flux_vis_4fwhm_aper',	    	    Aperture photometry - 4FWHM - VIS BAND
 'flux_y_1fwhm_aper',	    	    Aperture photometry - 1FWHM - NIR Y BAND
 'flux_y_4fwhm_aper',	    	    Aperture photometry - 4FWHM - NIR Y BAND
 'flux_j_1fwhm_aper',	    	    Aperture photometry - 1FWHM - NIR J BAND
 'flux_j_4fwhm_aper',	    	    Aperture photometry - 4FWHM - NIR J BAND
 'flux_h_1fwhm_aper',	    	    Aperture photometry - 1FWHM - NIR H BAND
 'flux_h_4fwhm_aper',	    	    Aperture photometry - 4FWHM - NIR H BAND
 'flux_nir_stack_1fwhm_aper',	    Aperture photometry - 1FWHM - NIR BAND
 'flux_nir_stack_2fwhm_aper',	    Aperture photometry - 2FWHM - NIR BAND
 'flux_nir_stack_3fwhm_aper',	    Aperture photometry - 3FWHM - NIR BAND
 'flux_nir_stack_4fwhm_aper',	    Aperture photometry - 4FWHM - NIR BAND  
 'fluxerr_vis_1fwhm_aper',	    ERR Aperture photometry - 1FWHM - VIS BAND  
 'fluxerr_vis_2fwhm_aper',	    ERR Aperture photometry - 2FWHM - VIS BAND  
 'fluxerr_vis_3fwhm_aper',	    ERR Aperture photometry - 3FWHM - VIS BAND  
 'fluxerr_vis_4fwhm_aper',	    ERR Aperture photometry - 4FWHM - VIS BAND  
 'fluxerr_y_1fwhm_aper',	    ERR Aperture photometry - 1FWHM - NIR Y BAND
 'fluxerr_y_4fwhm_aper',	    ERR Aperture photometry - 4FWHM - NIR Y BAND
 'fluxerr_j_1fwhm_aper',	    ERR Aperture photometry - 1FWHM - NIR J BAND
 'fluxerr_j_4fwhm_aper',	    ERR Aperture photometry - 4FWHM - NIR J BAND
 'fluxerr_h_1fwhm_aper',	    ERR Aperture photometry - 1FWHM - NIR H BAND
 'fluxerr_h_4fwhm_aper',	    ERR Aperture photometry - 4FWHM - NIR H BAND
 'fluxerr_nir_stack_1fwhm_aper',    ERR Aperture photometry - 1FWHM - NIR BAND  
 'fluxerr_nir_stack_2fwhm_aper',    ERR Aperture photometry - 2FWHM - NIR BAND  
 'fluxerr_nir_stack_3fwhm_aper',    ERR Aperture photometry - 3FWHM - NIR BAND  
 'fluxerr_nir_stack_4fwhm_aper',    ERR Aperture photometry - 4FWHM - NIR BAND  
 'flux_segmentation',		    flux within the segmented pixels of a source 
 'fluxerr_segmentation',	    Uncertainty on flux_segmentation 
 'flux_detection_total',	    flux measured within a Kron aperture
 'fluxerr_detection_total',	    Uncertainty on flux_detection_total
 'flux_vis_sersic',		    fluxes from model-fitting single Sersic models on VIS 
 'flux_y_sersic',		    fluxes from model-fitting single Sersic models on Y
 'flux_j_sersic',		    fluxes from model-fitting single Sersic models on J 
 'flux_h_sersic',		    fluxes from model-fitting single Sersic models on H 
 'fluxerr_vis_sersic',		    Uncertainty on flux_XXX_sersic
 'fluxerr_y_sersic',		    Uncertainty on flux_XXX_sersic
 'fluxerr_j_sersic',		    Uncertainty on flux_XXX_sersic
 'fluxerr_h_sersic',		    Uncertainty on flux_XXX_sersic
 'flag_vis',			    Photometry flag (see below) 
 'flag_y',			    Photometry flag (see below) 
 'flag_j',			    Photometry flag (see below) 
 'flag_h',			    Photometry flag (see below) 
 'flag_nir_stack',		    Photometry flag (see below) 
 'flag_u_ext_megacam',		    Photometry flag (see below) (for MEGACAM Ext data)
 'flag_r_ext_megacam',     	    Photometry flag (see below) (for MEGACAM Ext data)
 'flag_i_ext_panstarrs',	    Photometry flag (see below) (for PANSTARR Ext data)
 'flag_g_ext_hsc',		    Photometry flag (see below) (for HSC Ext data)
 'flag_z_ext_hsc',		    Photometry flag (see below) (for HSC Ext data)
'deblended_flag',		    1 if photometry results from blending with another source
 'point_like_prob',		    Some probability that the object is point-like
 'spurious_flag',		    1 if spurious detection 
 'spurious_prob',		    Probability for the object to be spurious
 'det_quality_flag',		    Detection quality flag
 'kron_radius',			    Kron radius of object
 'fwhm',			    Value used for FWHM aperturne flux


## **Morphological information**

 'mu_max',			    peak surface brightness above the background.
 'mumax_minus_mag',		    related to the concentration of light at the peak versus the total magnitude 
 'semimajor_axis',		    the semi-major axis of the ellipse describing the object shape, in pixel units
 'ellipticity',			    the ellipticity of the ellipse describing the object shape
 'sersic_sersic_nir_axis_ratio',     Result from Sersic fit (by from MER Photometry)
 'sersic_sersic_nir_axis_ratio_err', Result from Sersic fit (by from MER Photometry)
 'sersic_sersic_nir_index',	     Result from Sersic fit (by from MER Photometry)
 'sersic_sersic_nir_index_err',	     Result from Sersic fit (by from MER Photometry)
 'sersic_sersic_nir_radius',	     Result from Sersic fit (by from MER Photometry)
 'sersic_sersic_nir_radius_err',     Result from Sersic fit (by from MER Photometry)
 'sersic_sersic_vis_axis_ratio',     Result from Sersic fit (by from MER Photometry)
 'sersic_sersic_vis_axis_ratio_err', Result from Sersic fit (by from MER Photometry)
 'sersic_sersic_vis_index',          Result from Sersic fit (by from MER Photometry)
 'sersic_sersic_vis_index_err',	     Result from Sersic fit (by from MER Photometry)
 'sersic_sersic_vis_radius',	     Result from Sersic fit (by from MER Photometry)
 'sersic_sersic_vis_radius_err',     Result from Sersic fit (by from MER Photometry)
 'sersic_visnir_duration',           Result from Sersic fit (by from MER Photometry)
 'sersic_visnir_flags',		     Result from Sersic fit (by from MER Photometry)
 'sersic_visnir_iterations',	     Result from Sersic fit (by from MER Photometry)
 'sersic_visnir_reduced_chi2',	     Result from Sersic fit (by from MER Photometry)
 'gini',			     Gini index (see https://ui.adsabs.harvard.edu/abs/2004AJ....128..163L) 
 'moment_20',			     M20 coef (https://ui.adsabs.harvard.edu/abs/2004AJ....128..163L)
 'moment_20_err',		     Uncertainty on M20
 'concentration',		     Concentration (https://ui.adsabs.harvard.edu/abs/2004AJ....128..163L)
 'concentration_err',		     Uncertainty on concentration 
 'smoothness',			     Smoothness
 'smoothness_err',		     Uncertainty on concentration 
 'segmentation_area',		     Area of the segmentation region for photometry

## **Lensing search Engines scores:** 
 'lens_score_a',    	    	      Score for Search engine A
 'lens_score_b',		      Score for Search engine B
 'lens_score_c',		      Score for Search engine C
 'lens_score_d',		      Score for Search engine D
 'lens_score_e',		      Score for Search engine E
 'lens_score_f'			      Score for Search engine F


## List of photometry flags:
1: Source contaminated by close neighbors or has bad pixels
2: Source blended with another one (must comply with PARENT_ID ≠ -1)
4: Source saturated
8: Source close to a border
128: Source within the VIS bright star mask
256: Source within the NIR bright star mask
512: Source within an extended object area
1024: Source skipped by the deblending algorithm due to large pixel size
	

## Detection Quality Flag
DET_QUALITY_FLAG contains more information than the single-band flags
1: Source contaminated by closer neighbors or has bad pixels
2: Source blended with another one (must comply with PARENT_ID ≠ -1)
4: Source saturated	
8: Source close to a border
	


