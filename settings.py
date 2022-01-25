"""General settings."""

from pathlib import Path

from fooof import Bands

###################################################################################################
###################################################################################################

# Define path
PATH = Path('outputs/')

# Define standard band ranges
BANDS = Bands({'delta' : [2, 4],
               'theta' : [4, 8],
               'alpha' : [8, 13],
               'beta' : [13, 30]})

# Define standard band colours
BAND_COLORS = {'delta' : '#e8dc35',
               'theta' : '#46b870',
               'alpha' : '#1882d9',
               'beta'  : '#a218d9'}
# gamma color: '#e60026'
