The catalog `q1_lens_search_EDFN_4students.csv` contains a sample of gravitationally lensed galaxies found by the Euclid telescope.

The plausibility for those systems to be gravitational lensing galaxies is given by a grade. The grading scheme is the following:
- grade A: Likely a lensed system
- grade B: Plausible lens system but the lensed features are less ubiquitous
- grade C: Unlikely to be a lens but some systems show features supporting a lnesed hypothesis. 

Your task:

Within a jupyter notebook: 

- Write a code that reads the table in a format you can manipulate 
- Which column provide the grade? How many objects of each grade is there in the table?
- Inspired by the example code provided in `example_cutout.py`, create small cutouts (typ15 x 15 arcsec) of 5 objects of each grade. 


Optional: 
- Make a plot that displays the distribution of the objects on the sky, using a different color code for grade A, B, and C.

NB: If you use non-python code (such as TOPCAT and Aladin) for some operations, mention it in the Notbeook together with a brief explanation of how you have proceeded. 
